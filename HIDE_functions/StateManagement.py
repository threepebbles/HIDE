# coding=<utf-8>


import hashlib, os


_LINK_DIRECTORY = os.path.abspath(os.path.join(os.path.join('C:/Users/' + os.getenv('USERNAME')), 'Links/link.{59031a47-3f72-44a7-89c5-5595fe6b30ee}'))


# get path name of target list
def get_path_of_hiddenlist():
    if not os.path.isdir(os.path.abspath(os.path.join(os.path.join('C:/Users/' + os.getenv('USERNAME')), 'Links/link.{59031a47-3f72-44a7-89c5-5595fe6b30ee}'))):
        os.mkdir(os.path.abspath(os.path.join(os.path.join('C:/Users/' + os.getenv('USERNAME')), 'Links/link.{59031a47-3f72-44a7-89c5-5595fe6b30ee}')))

    f = os.path.abspath(os.path.join(_LINK_DIRECTORY, hashname('C:/' + os.getenv('USERNAME') + 'hidden entry')))
    if not os.path.isfile(f):
        t = open(f, 'w')
        t.close()
    return f


# get hashname
def hashname(path):
    h = hashlib.sha256('{}HIDEENTRY'.format(os.path.abspath(path)).encode()).hexdigest()
    return h


# get target state
def get_state(path):
    f = os.path.abspath(os.path.join(_LINK_DIRECTORY, hashname(path)))
    state = False
    with open(f, 'r') as o:
        state = o.readline().rstrip()
    return True if state == 'ON' else False


# check overlap register
def chk_overlap(path): 
    # 중복이면 True
    f = get_path_of_hiddenlist()
    o = open(f, 'r')
    while True:
        t = o.readline()
        if t == '': 
            o.close()
            return False
        if os.path.abspath(t.rstrip().split('?')[1]) == os.path.abspath(path):
            o.close()
            return True


# register file or folder to target list
def register(path, file=False):
    path = os.path.abspath(path)
    f = get_path_of_hiddenlist()
    
    if chk_overlap(path):
        return False

    with open(f, 'a') as o:
        o.write('{}?{}\n'.format('file' if file else 'folder', path))
    return recover_state(path)


# delete file or folder to target list
def delete(path):
    try:
        path = os.path.abspath(path)
        f1 = get_path_of_hiddenlist()
        f2 = f1+'1'
        with open(f1, 'r') as o1:
            with open(f2, 'w') as o2:
                while True:
                    t = o1.readline()
                    if t == '': break
                    if t.rstrip().split('?')[1] == path:
                        continue
                    o2.write(t)
        os.remove(f1)
        os.rename(f2, f1)

        f = os.path.join(_LINK_DIRECTORY, hashname(path))
        os.remove(f)
        return True
    except Exception as e:
        return False


# change target to hidden state
def stealth_state(path):
    try:
        f = os.path.join(_LINK_DIRECTORY, hashname(path))
        with open(f, 'w') as o:
            o.write('ON')
        return True
    except Exception as e:
        return False


# change target to recover state
def recover_state(path):
    try:
        f = os.path.join(_LINK_DIRECTORY, hashname(path))
        with open(f, 'w') as o:
            o.write('OFF')
        return True
    except Exception as e:
        return False