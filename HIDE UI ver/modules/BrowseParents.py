# coding=<utf-8>

from pathlib import Path
import os
import StateManagement as sm


def browse(path):
    p = Path(os.path.abspath(path))
    l = list(p.parents)

    hidden_list = sm.get_path_of_hiddenlist()
    rtn = []

    for ancestor in l:
        with open(hidden_list, 'r') as f:
            while True:
                s = f.readline().rstrip()
                if s == '': break
                if os.path.abspath(s) == os.path.abspath(ancestor):
                    if sm.get_state(ancestor):
                        rtn.append(ancestor)
                        break
    
    return rtn


def chk_ancestor_state(path):
    ancestor = browse(path)
    # print("ancestor: {}".format(ancestor))
    for al in ancestor:
        if sm.get_state(al):
            return False
    return True