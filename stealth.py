"""
1. 경로가 인자로 주어짐
2. 파일인지 디렉토리인지 검사
3-1. 파일일 경우 그 파일에 대해 은닉
3-2. 디렉토리일 경우 해당 디렉토리 아래를 모두 순회하면서 모든 파일을 은닉
4. 파일의 은닉
    a) 원본 파일을 하드링크한 새로운 파일을 생성 후 원본 파일은 제거 mklink /h hardcopy test.txt
        // 해당 파일의 속성을 저장해주어야 함
        // 읽기 전용인지, 숨김파일인지 등등 일반 파일인지에 따라서 삭제 방법과 검색 방법이 다름
        // 파일삭제는 del, 파일검색은 dir, 폴더삭제는 rmdir
    b) 원본 파일의 경로와 입력키를 해시한 값으로 임시파일 생성
    c) 임시파일 안에는 입력키와 원본파일의 경로, 하드링크한 파일의 경로가 암호화되어있음
    d) 복호화시 요청된 원본파일과 키를 기반으로 경로가 저장된 임시파일을 탐색
    e) 임시파일을 찾게되면 복호화 했을 떄 원본 파일의 경로, 하드링크한 파일의 경로를 얻어옴
    f) 얻어온 하드링크 파일의 경로를 원본 파일 경로로 하드링크 후 하드링크 파일은 제거
---
추가해야할 부분
list파일 암호화, key사용법, 적용할해시, 
list파일 이름지정방식, link파일 이름지정방식,
list폴더, link폴더 자동지정 경로
"""
import os, shutil, hashlib
import win32api, win32con

def get_hashed_path(path):
    return hashlib.sha256(path.encode()).hexdigest()

def create_list_file(path, key):
    if not os.path.isdir(_list_directory):
        os.mkdir(_list_directory)
    if not os.path.isdir(_link_directory):
        os.mkdir(_link_directory)

    # tmp_file = _list_directory + '/' + hash(path) # 은닉하려는 경로의 해시를 이용해서 파일이름을 생성 ######
    tmp_file_name = get_hashed_path(path + key)
    tmp_file = os.path.join(_list_directory, tmp_file_name)
    return tmp_file

# stealth 기능
def do_stealth(path, key):
    global f # 주어진 인자 path에 대해서 수행되는 모든 링크 내용을 기록하는 파일
    
    path = os.path.abspath(path)
    tmp_file = create_list_file(path, key)
    f = open(tmp_file, 'w')
    file_or_folder = 'folder' if os.path.isdir(path) else 'file'
    f.write('{} {}\n'.format(key, file_or_folder)) # 첫줄 key

    rtn = False
    if os.path.isfile(path):
        rtn = file_stealth(path)
    elif os.path.isdir(path):
        rtn = dir_stealth(path)
    f.close()

    if not rtn:
        os.remove(tmp_file)
    elif rtn and os.path.isfile(path):
        os.remove(path)
    elif rtn and os.path.isdir(path):
        shutil.rmtree(path)
    
    # list파일 암호화
    return rtn

def file_stealth(path):
    try:
        # 하드 링크될 파일의 이름
        link_name = os.path.join(_link_directory, path.replace(':', '_').replace('\\', '__'))
        link_name = link_name.replace('\\', '/')

        # 링크파일의 이름(경로) 해시
        hash_name = get_hashed_path(link_name)
        link_name = os.path.join(_link_directory, hash_name)
        
        # 파일 하드링크
        os.link(path, link_name)

        # 링크 내역 저장
        # [파일속성, 원본경로, 링크경로]
        data = [str(win32api.GetFileAttributes(path)), path, link_name]
        f.write("{}\n".format('?'.join(data)))

        # read only 해제
        win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_NORMAL)
    except:
        return False
    return True


def dir_stealth(path):
    # 입력된 경로의 하위 모든 파일 및 폴더에 대해서 수행
    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(path, root)
        for file in files:
            filepath = os.path.join(rootpath, file)
            if not file_stealth(filepath):
                return False
        
        for folder in dirs:
            # 폴더 경로 저장
            # [DIR, 폴더속성, 폴더경로]
            # 폴더 옵션 설정 못찾음 #######################
            folderpath = os.path.join(rootpath, folder)
            f.write("DIR?{}?{}\n".format(win32api.GetFileAttributes(folderpath), folderpath))
    return True


def find_list(path, key):
    if not os.path.isdir(_list_directory):
        return None
    
    listdir = os.path.abspath(_list_directory)
    root, _, files = list(os.walk(listdir))[0]
    for file in files:
        if file == tmp_file_name:
            list_path = os.path.join(root, file)
            return os.path.abspath(list_path)


# stealth 해제 기능
def un_stealth(path, key):
    global tmp_file_name

    # _list_directory 밑에 path의 해시값과 일치하는 파일이 존재하는지 확인
    path = os.path.abspath(path)
    tmp_file_name = get_hashed_path(path + key)
    if not os.path.isfile(os.path.join(_list_directory, tmp_file_name)):
        return False

    # 저장되어있는 list file 검색
    tmp_file = find_list(path, key)
    if not tmp_file: return False

    # list파일을 복호화
    # 코드 작성 필요 ######################################################

    # list파일에서 읽어와서 모든 파일, 폴더에 대해서 역으로 복구
    f = open(tmp_file, 'r')
    # 첫줄 키가 일치한지 확인
    first = f.readline().rstrip().split()
    if key != first[0]: return False

    # 복구 대상이 디렉토리이면 생성
    if first[1] == 'folder':
        os.mkdir(path)

    # 한줄씩 입력받으면서
    # 입력 내용이 폴더면, 해당 경로에 폴더 생성
    # 입력 내용이 파일이면, 하드링크했던 파일에서 원본으로 하드링크로 복구 + 파일속성까지
    while True:
        line = f.readline().rstrip().split('?')
        if not line[0]: break # EOF

        if line[0].isdigit(): # 파일
            attr, origin, hardlink = line
            # 원본 파일 복구
            os.link(hardlink, origin)
            # read only 해제
            win32api.SetFileAttributes(hardlink, win32con.FILE_ATTRIBUTE_NORMAL)
            # 링크 파일 제거
            os.remove(hardlink)
            # 파일 속성 복구
            win32api.SetFileAttributes(origin, win32con.FILE_ATTRIBUTE_NORMAL)
            win32api.SetFileAttributes(origin, int(attr))
        elif line[0] == 'DIR': # 폴더
            _, attr, origin = line
            # 원본 폴더 복구
            os.mkdir(origin)
            # 폴더 속성 복구
            win32api.SetFileAttributes(origin, int(attr))

    f.close()
    os.remove(tmp_file)
    return True



# 경로 하드코딩말고..#########################################################
# _list_directory = "C:/Users/psm34/Desktop/capstone/list" 
# _link_directory = "C:/Users/psm34/Desktop/capstone/link"
_list_directory = os.path.join(os.getcwd(), '../list') #"C:/Users/psm34/Desktop/capstone/list" 
_link_directory = os.path.join(os.getcwd(), '../link') #"C:/Users/psm34/Desktop/capstone/link"

do_stealth("C:/Users/psm34/Desktop/capstone/test1", 'tempkey') 
# un_stealth("C:/Users/psm34/Desktop/capstone/test1", 'tempkey')