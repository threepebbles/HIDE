import sys
import HIDE_main
import requests
import Login, Passwd

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

CalUI = '../_uiFiles/login.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)
        self.setWindowTitle("WELCOME TO HIDE")

        self.widget.setStyleSheet('image:url(../image/login.png);border:0px;')

        self.pushButton.clicked.connect(self.login_NumClicked)

        self.pw2_pushButton.clicked.connect(self.pw2_NumClicked)
        self.pw2set_pushButton.clicked.connect(self.pw2set_NumClicked)

        global id, pwd, offpwd

    #login click
    def login_NumClicked(self):
        id = self.id_lineEdit.text()
        pwd = self.pw_lineEdit.text()
        if Login.chk_login(id, pwd):
            print('ok')
            QMessageBox.about(self, "LOGIN SUCCESS", "WELCOME TO HIDE")
            #로그인 성공 시 HIDE 열고 login 닫기
            HIDE_main.main_dialog.show()
            self.close()

        else:
            #로그인 실패
            print('out')
            QMessageBox.about(self, "LOGIN FAILED", "FAIL")
            #id, pwd 초기화
            self.id_lineEdit.clear()
            self.pw_lineEdit.clear()

    def pw2_NumClicked(self):
        offpwd = self.pwd_lineEdit.text()
        if Passwd.cmp_program_pw(offpwd):
            print('offline login')
            QMessageBox.about(self, "OFFLINE LOGIN", "WELCOME TO HIDE")
            #로그인 성공 시 HIDE 열고 login 닫기
            HIDE_main.main_dialog.show()
            self.close()

        else:
            #로그인 실패
            print('offline login fail')
            QMessageBox.about(self, "OFFLINE LOGIN FAILED", "FAIL")
            #pwd 초기화
            self.pwd_lineEdit.clear()
            
            
    def pw2set_NumClicked(self):
        print('pwd set')
        
        offpwd = self.pwd_lineEdit.text() #pwd 저장
        if len(offpwd) == 0:
            QMessageBox.about(self, "OFFLINE PASSWD SET", "FAIL")
        elif Passwd.chk_set_before():
            QMessageBox.about(self, "OFFLINE PASSWD SET", "ALREADY SET")
        else:
            Passwd.set_program_pw(offpwd)
        


app = QApplication(sys.argv)
main_dialog = MainDialog() #login 불러오기
#main_dialog.show()
#app.exec_()