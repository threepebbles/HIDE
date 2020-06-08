# -*- coding: utf-8 -*-

import sys
import encrypt, stealth, StateManagement, login
import pkg_resources.py2_warn

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

colors = ['#f8cc00', '#f7f7f7', '#ffffff']

CalUI = '../_uiFiles/hide.ui'

class HideDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)
        self.setWindowTitle("HIDE")

        self.originlist()

        self.Select_pushButton.clicked.connect(self.select_NumClicked)
        self.Folder_pushButton.clicked.connect(self.folder_NumClicked)
        self.lock_pushButton.clicked.connect(self.lock_NumClicked)
        self.unlock_pushButton.clicked.connect(self.unlock_NumClicked)
        self.quit_pushButton.clicked.connect(self.quit_NumClicked)
        self.listWidget_1.itemClicked.connect(self.insertListWidget)
        self.listWidget_2.itemClicked.connect(self.insertListWidget2)

        self.Delete_pushButton.clicked.connect(self.delete_NumClicked)
        self.Delete_pushButton_2.clicked.connect(self.delete_NumClicked_2)

        self.logout_pushButton.clicked.connect(self.logout_NumClicked)
        self.login_pushButton.clicked.connect(self.login_NumClicked)

        self.re_pushButton.clicked.connect(self.refresh_NumClicked)

        self.widget_3.setStyleSheet('image:url(../image/background.png);border:0px;')
        self.widget_2.setStyleSheet('image:url(../image/filelist.png);border:0px;')
        self.Folder_widget.setStyleSheet('image:url(../image/path.png);border:0px;')

        self.lock_pushButton.setStyleSheet(
        '''
            QPushButton{image:url(../image/lock.png);border:0px;}
            QPushButton:hover{image:url(../image/lock_c.png);border:0px;}
        ''')
        self.unlock_pushButton.setStyleSheet(
        '''
            QPushButton{image:url(../image/unlock.png);border:0px;}
            QPushButton:hover{image:url(../image/unlock_c.png);border:0px;}
        ''')
        self.quit_pushButton.setStyleSheet(
        '''
            QPushButton{image:url(../image/quit.png);border:0px;}
            QPushButton:hover{image:url(../image/quit_c.png);border:0px;}
        ''')

        self.Select_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/select_b.png);border:0px;}
            ''')
        self.Folder_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/view_b.png);border:0px;}
            ''')
        self.Delete_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/trash.png);border:0px;}
            ''')
        self.Delete_pushButton_2.setStyleSheet(
            '''
                QPushButton{image:url(../image/trash.png);border:0px;}
            ''')
        self.logout_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/logout_bt.png);border:0px;}
            ''')
        self.login_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/login_bt.png);border:0px;}
            ''')
        self.re_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/refresh_1.png);border:0px;}
                QPushButton:hover{image:url(../image/refresh_2.png);border:0px;}
            ''')


    def lock_NumClicked(self):
        #hide on
        print('hide')
        passwd.main_dialog.show()
        #passwd.main_dialog.close()
        QMessageBox.about(self, "HIDE ON", "HIDE ON")
        stealth.do_stealth(nu, "111")
        se.setBackground(QColor(colors[0])) #색으로 on/off 구별

    def unlock_NumClicked(self):
        #hide off
        print('unhide')
        QMessageBox.about(self, "HIDE OFF", "HIDE OFF")
        stealth.un_stealth(nu, "111") #lock에 따라서, false일 때 기능 실패
        se.setBackground(QColor(colors[2]))

    def quit_NumClicked(self):
        #quit
        print('quit')
        QMessageBox.about(self, "Quit", "Quit")
        QCoreApplication.instance().quit()

    def select_NumClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        global item
        item = QListWidgetItem(fname[0])

        if StateManagement.register(fname[0], True):
            self.listWidget_1.addItem(fname[0])
        else:
            QMessageBox.about(self, "Duplicate", "Duplicate")

    def folder_NumClicked(self):
        fname = QFileDialog.getExistingDirectory(self)
        item = QListWidgetItem(fname)

        if StateManagement.register(fname, False):
            self.listWidget_2.addItem(fname)
        else:
            QMessageBox.about(self, "Duplicate", "Duplicate")

    def insertListWidget(self):
        global nu, se
        print(self.listWidget_1.currentItem().text())
        nu = self.listWidget_1.currentItem().text()
        se = self.listWidget_1.currentItem()

    def insertListWidget2(self):
        global nu, se
        print(self.listWidget_2.currentItem().text())
        nu = self.listWidget_2.currentItem().text()
        se = self.listWidget_2.currentItem()

    def delete_NumClicked(self):
        QMessageBox.about(self, "DELETE FILE PATH", "DELETE FILE PATH")
        # list delete
        self.removeItemRow = self.listWidget_1.currentRow()
        self.listWidget_1.takeItem(self.removeItemRow)
        StateManagement.delete(nu)

    def delete_NumClicked_2(self):
        QMessageBox.about(self, "DELETE FOLDER PATH", "DELETE FOLDER PATH")
        # list delete
        self.removeItemRow = self.listWidget_2.currentRow()
        self.listWidget_2.takeItem(self.removeItemRow)
        StateManagement.delete(nu)

    def logout_NumClicked(self):
        #online 상태일 때만 사용
        QMessageBox.about(self, "LOGOUT", "LOGOUT!")
        login.main_dialog.show()
        self.close()

    def login_NumClicked(self):
        #offline 상태일 때만 사용
        QMessageBox.about(self, "LOGIN", "LOGIN!")
        login.main_dialog.show()
        self.close()

    def refresh_NumClicked(self):
        self.listWidget_2.clear()
        self.listWidget_1.clear()
        self.originlist()

    def originlist(self):
        origin = StateManagement.get_path_of_hiddenlist()
        if not os.path.isfile(origin):
            f = open(origin,'w')
            f.close()

        op = open(origin, 'r')

        while True:
            t = op.readline()
            if t == '':
                op.close()
                return False
            if t.rstrip().split('?')[0] == 'file':
                item = QListWidgetItem(t.rstrip().split('?')[1])
                if StateManagement.get_state(t.rstrip().split('?')[1]) == True:
                    item.setBackground(QColor(colors[0]))
                else :
                    item.setBackground(QColor(colors[2]))
                self.listWidget_1.addItem(item)
            if t.rstrip().split('?')[0] == 'folder':
                item = QListWidgetItem(t.rstrip().split('?')[1])
                if StateManagement.get_state(t.rstrip().split('?')[1]) == True:
                    item.setBackground(QColor(colors[0]))
                else :
                    item.setBackground(QColor(colors[2]))
                self.listWidget_2.addItem(item)


app = QApplication(sys.argv)
main_dialog = HideDialog() #hide 불러오기
#main_dialog.show()
#app.exec_()