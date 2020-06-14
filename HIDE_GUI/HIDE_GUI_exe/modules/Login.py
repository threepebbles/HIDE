# coding=<utf-8>


import requests, websocket, json
import os, hashlib, time, threading
import StateManagement as sm
import encrypt, stealth, sys


_API_HOST = "http://34.64.186.183:8000"
_LOGIN_PATH = "/rest-auth/login/"
_LOGOUT_PATH = "/rest-auth/logout/"
_CREATE_PATH = "/hide/myfile/rest/create/"
_DELETE_PATH = "/hide/myfile/rest/delete/"
_DIRECTORY = os.path.abspath(os.path.join(os.path.join('C:/Users/' + os.getenv('USERNAME')), 'Links/link.{59031a47-3f72-44a7-89c5-5595fe6b30ee}'))
_USERDATA_PATH = os.path.join(_DIRECTORY,
                            hashlib.sha256(' '.join([os.getenv('USERNAME'),'HIDEUSERDATA']).encode()).hexdigest())


def get_userdata():
    key = encrypt.make_pass(_USERDATA_PATH, 'capstone2HIDE')
    encrypt.decrypt_file(key, _USERDATA_PATH)
    
    uid = upw = ''
    # 복호화
    with open(_USERDATA_PATH, 'r') as o:
        uid = o.readline().rstrip()
        upw = o.readline().rstrip()
    
    encrypt.encrypt_file(key, _USERDATA_PATH)
    return uid, upw


def set_userdata(username, password):
    if not os.path.isdir(os.path.abspath(os.path.join(os.path.join('C:/Users/' + os.getenv('USERNAME')), 'Links/link.{59031a47-3f72-44a7-89c5-5595fe6b30ee}'))):
        os.mkdir(os.path.abspath(os.path.join(os.path.join('C:/Users/' + os.getenv('USERNAME')), 'Links/link.{59031a47-3f72-44a7-89c5-5595fe6b30ee}')))

    with open(_USERDATA_PATH, 'w') as f:
        f.write('{}\n{}'.format(username, password))
    try:
        enckey = encrypt.make_pass(_USERDATA_PATH, 'capstone2HIDE')
        encrypt.encrypt_file(enckey, _USERDATA_PATH)
    except Exception as e:
        print(e)
        print('logindata')
        os.remove(_USERDATA_PATH)
        return False
    return True


def send_statements():
    try:
        # delete list
        delete_url = _API_HOST + _DELETE_PATH
        res = s.post(delete_url)

        if res.status_code == 200:
            # new updated list
            path = sm.get_path_of_hiddenlist()
            print('path of sm.get_path_of_hiddenlist() : {}'.format(path))
            update_url = _API_HOST + _CREATE_PATH
            with open(path, 'r') as f:
                while True:
                    l = f.readline()
                    if l == "": break

                    p = os.path.abspath(l.rstrip().split('?')[1])
                    print(p)
                    stm = sm.get_state(p)

                    res = s.post(update_url, data={'file_path':p, 'state':stm})
        return True
        
    except Exception as e:
        print(e)    
        return False


def periodical_send():
    while True:
        send_statements()
        if chk_logout(): # 로그아웃 된 상태면 True return
            ws.close()
            sys.exit()
        time.sleep(20)


def chk_login(uid, upw):
    try:
        url = _API_HOST + _LOGIN_PATH
        login_data = {'username': uid, "password": upw}

        resp = requests.post(url, data=login_data)
        if resp.status_code != 200:
            return False
        
        return set_userdata(uid, upw)
    except Exception as e:
        print(e)
        return False


def chk_logout():
    if os.path.isfile(_USERDATA_PATH):
        return False # 로그아웃 안 된 상태
    else: 
        return True # 로그아웃 된 상태


def login(uid = "", upw = ""):
    global s, ws

    url = _API_HOST + _LOGIN_PATH
    ws_url = "ws://34.64.186.183:8000/ws/chat/1/"

    if uid == "":
        # 아이디 비밀번호가 저장된 파일이 존재하면 그 파일에서 아이디 비밀번호 입력받고
        if os.path.isfile(_USERDATA_PATH):
            uid, upw = get_userdata()

        # 아이디 비밀번호가 저장된 파일이 존재하지 않는다면 사용자가 로그인에 성공하게 되어야 회원 정보가 저장됨
        else:
            return False

    login_data = {'username': uid, "password": upw}

    s = requests.Session()
    resp = s.post(url, data=login_data)
    print(resp.status_code)
    if resp.status_code != 200:
        return False

    my_cookie = resp.headers['Set-Cookie']

    try:
        import thread
    except ImportError:
        import _thread as thread


    # 서버 명령 수신
    def on_message(ws, message):
        print('[server]: '+message)
        payload = json.loads(message) # you can use json.loads to convert string to json
        
        target = payload['file_path']
        state = payload['file_state']
        print(target, state)
        
        if state == True:
            stealth.do_stealth(target) 
        else:
            stealth.un_stealth(target)


    def on_error(ws, error):
        print(error)


    def on_close(ws):
        print("### socket closed ###")


    def on_open(ws):
        print('connect')

        st = threading.Thread(target=periodical_send)
        st.daemon = True
        st.start()
        # parent thread is waiting server's packet


    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                cookie=my_cookie,
                                )
    ws.on_open = on_open
    ws.run_forever()

    return True


def logout():
    url = _API_HOST + _LOGOUT_PATH

    if os.path.isfile(_USERDATA_PATH):
        os.remove(_USERDATA_PATH)
        return True
    return False