# -*- coding: utf-8 -*-

import sys
import encrypt, stealth, loginUI as login

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

if __name__ == '__main__':
    #로그인창 연결
    login.main_dialog.show()
    login.app.exec_()