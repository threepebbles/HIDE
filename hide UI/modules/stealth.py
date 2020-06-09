# coding=<utf-8>

import os, shutil, hashlib
import win32api, win32con
import encrypt, BrowseParents as bp
import StateManagement as sm

_LIST_DIRECTORY = os.path.abspath(os.path.join('C:/Users/이은영', 'HIDE list'))
_LINK_DIRECTORY = os.path.abspath(os.path.join('C:/Users/이은영',
                                               'Links/link.{59031a47-3f72-44a7-89c5-5595fe6b30ee}'))


def get_hashed_path(path):
    return hashlib.sha256(path.encode()).hexdigest()


# _directory 경로가 이미 생성되어있어야 함
# main 파일에서 생성시켜놔야함
def create_list_file(path, key):
    if not os.path.isdir(_LIST_DIRECTORY):
        os.mkdir(_LIST_DIRECTORY)
    if not os.path.isdir(_LINK_DIRECTORY):
        os.mkdir(_LINK_DIRECTORY)

    tmp_file_name = get_hashed_path(path + key)
    tmp_file = os.path.join(_LIST_DIRECTORY, tmp_file_name)
    return tmp_file


# stealth 기능
def do_stealth(path, key='capstone2hide'):
    global f  # 주어진 인자 path에 대해서 수행되는 모든 링크 내용을 기록하는 파일

    path = os.path.abspath(path)

    if not bp.chk_ancestor_state(path):
        return False

    tmp_file = create_list_file(path, key)
    key = encrypt.make_pass(path, key)
    f = open(tmp_file, 'w')
    file_or_folder = 'folder' if os.path.isdir(path) else 'file'
    f.write('{}\n'.format(file_or_folder))  # 첫줄 key

    rtn = False
    if os.path.isfile(path):
        rtn = file_stealth(path)
    elif os.path.isdir(path):
        rtn = dir_stealth(path)
    f.close()

    if not rtn:
        os.remove(tmp_file)
        return False
    if not encrypt.encrypt_file(key, tmp_file):  # 암호화 실패
        # 지금 생성된 link 파일 삭제
        if os.path.isdir(path):
            del_linkdir(tmp_file)
        else:
            del_linkfile(tmp_file)
        os.remove(tmp_file)  # list 파일 삭제
        return False
    elif rtn and os.path.isfile(path):
        os.remove(path)
    elif rtn and os.path.isdir(path):
        shutil.rmtree(path)

    sm.stealth_state(path)
    return rtn


def del_linkfile(list_file):
    with open(list_file, 'r') as lfile:
        line = lfile.readline()

        line = lfile.readline()
        line = line.split('?')
        os.remove(os.path.abspath(line[2]))
    return


def del_linkdir(list_file):
    with open(list_file, 'r') as lfile:
        line = lfile.readline()

        while True:
            line = lfile.readline()
            if line == '': break
            line = line.split('?')
            if line[0] != 'DIR':
                os.remove(os.path.abspath(line[2]))
    return


def file_stealth(path):
    try:
        # 하드 링크될 파일의 이름
        link_name = os.path.join(_LINK_DIRECTORY, path.replace(':', '_').replace('\\', '__'))
        link_name = link_name.replace('\\', '/')
        # 링크파일의 이름(경로) 해시
        hash_name = get_hashed_path(link_name)
        link_name = os.path.join(_LINK_DIRECTORY, hash_name)

        # 파일 하드링크
        os.link(path, link_name)

        # 링크 내역 저장
        # [파일속성, 원본경로, 링크경로]
        data = [str(win32api.GetFileAttributes(path)), path, link_name]
        f.write("{}\n".format('?'.join(data)))

        # read only 해제
        win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_NORMAL)
    except Exception as e:
        print(e)
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
            folderpath = os.path.join(rootpath, folder)
            f.write("DIR?{}?{}\n".format(win32api.GetFileAttributes(folderpath), folderpath))
    return True


def find_list(path):
    if not os.path.isdir(_LIST_DIRECTORY):
        return None

    listdir = os.path.abspath(_LIST_DIRECTORY)
    root, _, files = list(os.walk(listdir))[0]
    for file in files:
        if file == tmp_file_name:
            list_path = os.path.join(root, file)
            return os.path.abspath(list_path)


# stealth 해제 기능
def un_stealth(path, key='capstone2hide'):
    global tmp_file_name

    path = os.path.abspath(path)

    if not bp.chk_ancestor_state(path):
        return False

    # _LIST_DIRECTORY 밑에 path의 해시값과 일치하는 파일이 존재하는지 확인
    tmp_file_name = get_hashed_path(path + key)
    if not os.path.isfile(os.path.join(_LIST_DIRECTORY, tmp_file_name)):
        return False

    # 저장되어있는 list file 검색
    tmp_file = find_list(path)
    if not tmp_file: return False

    # list파일을 복호화
    key = encrypt.make_pass(path, key)
    if not encrypt.decrypt_file(key, tmp_file):
        print('decrypt error')
        return False

    # list파일에서 읽어와서 모든 파일, 폴더에 대해서 역으로 복구
    f = open(tmp_file, 'r')

    # 복구 대상이 디렉토리이면 생성
    first = f.readline().rstrip()
    if first == 'folder':
        os.mkdir(path)

    # 한줄씩 입력받으면서
    # 입력 내용이 폴더면, 해당 경로에 폴더 생성
    # 입력 내용이 파일이면, 하드링크했던 파일에서 원본으로 하드링크로 복구 + 파일속성까지
    while True:
        line = f.readline().rstrip().split('?')
        if not line[0]: break  # EOF

        if line[0].isdigit():  # 파일
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
        elif line[0] == 'DIR':  # 폴더
            _, attr, origin = line
            # 원본 폴더 복구
            os.mkdir(origin)
            # 폴더 속성 복구
            win32api.SetFileAttributes(origin, int(attr))

    f.close()
    os.remove(tmp_file)
    sm.recover_state(path)
    return True