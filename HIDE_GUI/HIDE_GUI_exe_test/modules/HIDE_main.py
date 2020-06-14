# -*- coding: utf-8 -*-

import sys
import encrypt, stealth, StateManagement, loginUI as login
import Login
# import pkg_resources.py2_warn

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5 import uic
import os
import hide_ui

colors = ['#f8cc00', '#ffffff']

# CalUI = '../_uiFiles/hide.ui'

class HideDialog(QDialog, hide_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, None)
        # uic.loadUi(CalUI, self)
        self.setupUi(self)
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

        root_path = getattr(sys, '_MEIPASS')
        # print('root_path: ', root_path)

        self.widget_3.setStyleSheet('image:url(' + os.path.join(root_path, 'background.png').replace("\\", "/") +');border:0px;')
        self.widget_2.setStyleSheet('image:url(' + os.path.join(root_path, 'path.png').replace("\\", "/") + ');border:0px;')
        self.Folder_widget.setStyleSheet('image:url(' + os.path.join(root_path, 'filelist.png').replace("\\", "/") + ');border:0px;')

        self.lock_pushButton.setStyleSheet(
        '''
            QPushButton{image:url(''' + os.path.join(root_path, 'lock.png').replace("\\", "/") + ''');border:0px;}
            QPushButton:hover{image:url(''' + os.path.join(root_path, 'lock_c.png').replace("\\", "/") + ''');border:0px;}
        ''')
        self.unlock_pushButton.setStyleSheet(
        '''
            QPushButton{image:url(''' + os.path.join(root_path, 'unlock.png').replace("\\", "/") + ''');border:0px;}
            QPushButton:hover{image:url(''' + os.path.join(root_path, 'lock_c.png').replace("\\", "/") + ''');border:0px;}
        ''')
        self.quit_pushButton.setStyleSheet(
        '''
            QPushButton{image:url(''' + os.path.join(root_path, 'quit.png').replace("\\", "/") + ''');border:0px;}
            QPushButton:hover{image:url(''' + os.path.join(root_path, 'quit_c.png').replace("\\", "/") + ''');border:0px;}
        ''')

        self.Select_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(''' + os.path.join(root_path, 'select_b.png').replace("\\", "/") + ''');border:0px;}
            ''')
        self.Folder_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(''' + os.path.join(root_path, 'view_b.png').replace("\\", "/") + ''');border:0px;}
            ''')
        self.Delete_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(''' + os.path.join(root_path, 'trash.png').replace("\\", "/") + ''');border:0px;}
            ''')
        self.Delete_pushButton_2.setStyleSheet(
            '''
                QPushButton{image:url(''' + os.path.join(root_path, 'trash.png').replace("\\", "/") + ''');border:0px;}
            ''')
        self.logout_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(''' + os.path.join(root_path, 'logout_bt.png').replace("\\", "/") + ''');border:0px;}
            ''')
        self.login_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(''' + os.path.join(root_path, 'login_bt.png').replace("\\", "/") + ''');border:0px;}
            ''')
        self.re_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(''' + os.path.join(root_path, 'refresh_1.png').replace("\\", "/") + ''');border:0px;}
                QPushButton:hover{image:url(''' + os.path.join(root_path, 'refresh_2.png').replace("\\", "/") + ''');border:0px;}
            ''')

    def refresh_NumClicked(self):
        self.listWidget_2.clear()
        self.listWidget_1.clear()
        self.originlist()

    def lock_NumClicked(self):
        global nu, se, file_selected

        if('nu' in globals() and 'file_selected' in globals()):
            if(file_selected==True):
                #hide on
                if(stealth.do_stealth(nu)==False):
                    onmsg = QMessageBox()
                    onmsg.setText("　　Hide Fails!　　　")
                    onmsg.setWindowTitle("Error")
                    onmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                    onmsg.exec_()
                    se.setBackground(QColor(colors[1])) # hide off
                    print('Failed to hide')
                else:
                    onmsg = QMessageBox()
                    onmsg.setText("　　Hide On!　　　")
                    onmsg.setWindowTitle("HIDE ON")
                    onmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                    onmsg.exec_()
                    se.setBackground(QColor(colors[0])) # hide on
                    print('Success to hide on') 
            else:
                onmsg = QMessageBox()
                onmsg.setText("　　There is no selected file!　　　")
                onmsg.setWindowTitle("Error")
                onmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                onmsg.exec_()
                print('Please, select file')
        else:
            onmsg = QMessageBox()
            onmsg.setText("　　There is no selected file!　　　")
            onmsg.setWindowTitle("Error")
            onmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
            onmsg.exec_()
            print('Please, select file')
        
        if('file_selected' in globals()):
            file_selected = False


    def unlock_NumClicked(self):
        global nu, se, file_selected

        if('nu' in globals() and 'file_selected' in globals()):
            if(file_selected==True):
                #hide off
                if(stealth.un_stealth(nu)==False):
                    offmsg = QMessageBox()
                    offmsg.setText("　　Hide Fails!　　　")
                    offmsg.setWindowTitle("Error")
                    offmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                    offmsg.exec_()
                    se.setBackground(QColor(colors[0]))
                    print('Failed to hide')
                else:
                    print('unhide')
                    offmsg = QMessageBox()
                    offmsg.setText("　　Hide Off!　　　")
                    offmsg.setWindowTitle("HIDE OFF")
                    offmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                    offmsg.exec_()
                    se.setBackground(QColor(colors[1]))
                    print('Success to hide off') 
            else:
                offmsg = QMessageBox()
                offmsg.setText("　　There is no selected file!　　　")
                offmsg.setWindowTitle("Error")
                offmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                offmsg.exec_()
                print('Please, select file')
        else:
            offmsg = QMessageBox()
            offmsg.setText("　　There is no selected file!　　　")
            offmsg.setWindowTitle("Error")
            offmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
            offmsg.exec_()
            print('Please, select file')

        if('file_selected' in globals()):
            file_selected = False

    def delete_NumClicked(self):
        global nu, file_selected

        if('nu' in globals() and 'file_selected' in globals()):
            if(file_selected==True):
                delmsg = QMessageBox()
                delmsg.setText("　　Delete File Path!　　　")
                delmsg.setWindowTitle("DELETE FILE PATH")
                delmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                delmsg.exec_()
                # list delete
                self.removeItemRow = self.listWidget_1.currentRow()
                self.listWidget_1.takeItem(self.removeItemRow)
                StateManagement.delete(nu)
            else:
                delmsg = QMessageBox()
                delmsg.setText("　　There is no selected files!　　　")
                delmsg.setWindowTitle("Error")
                delmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                delmsg.exec_()
                print('Please, select file')    
        else:
            delmsg = QMessageBox()
            delmsg.setText("　　There is no selected files!　　　")
            delmsg.setWindowTitle("Error")
            delmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
            delmsg.exec_()
            print('Please, select file')

        if('file_selected' in globals()):
            file_selected = False

    def delete_NumClicked_2(self):
        global nu, file_selected

        if('nu' in globals() and 'file_selected' in globals()):
            if(file_selected==True):
                del2msg = QMessageBox()
                del2msg.setText("　　Delete Folder Path!　　　")
                del2msg.setWindowTitle("DELETE FOLDER PATH")
                del2msg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                del2msg.exec_()
                # list delete
                self.removeItemRow = self.listWidget_2.currentRow()
                self.listWidget_2.takeItem(self.removeItemRow)
                StateManagement.delete(nu)
            else:
                del2msg = QMessageBox()
                del2msg.setText("　　There is no selected files!　　　")
                del2msg.setWindowTitle("Error")
                del2msg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
                del2msg.exec_()
                print('Please, select file')
        else:
            del2msg = QMessageBox()
            del2msg.setText("　　There is no selected files!　　　")
            del2msg.setWindowTitle("Error")
            del2msg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
            del2msg.exec_()
            print('Please, select file')

        if('file_selected' in globals()):
            file_selected = False

    def quit_NumClicked(self):
        #quit
        print('quit')
        quimsg = QMessageBox()
        quimsg.setText("　　Quit!　　　")
        quimsg.setWindowTitle("QUIT")
        quimsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
        quimsg.exec_()
        QCoreApplication.instance().quit()

    def select_NumClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0] == '':
            return

        global item
        item = QListWidgetItem(fname[0])

        if StateManagement.register(fname[0], True):
            self.listWidget_1.addItem(fname[0])
        else:
            dumsg = QMessageBox()
            dumsg.setText("　　Duplicate!　　　")
            dumsg.setWindowTitle("DUPLICATE")
            dumsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
            dumsg.exec_()

    def folder_NumClicked(self):
        fname = QFileDialog.getExistingDirectory(self)
        if fname == '':
            return
        item = QListWidgetItem(fname)

        if StateManagement.register(fname, False):
            self.listWidget_2.addItem(fname)
        else:
            dumsg = QMessageBox()
            dumsg.setText("　　Duplicate!　　　")
            dumsg.setWindowTitle("DUPLICATE")
            dumsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
            dumsg.exec_()

    def insertListWidget(self):
        global nu, se, file_selected
        file_selected = True
        print(self.listWidget_1.currentItem().text())
        nu = self.listWidget_1.currentItem().text()
        se = self.listWidget_1.currentItem()

    def insertListWidget2(self):
        global nu, se, file_selected
        file_selected = True
        print(self.listWidget_2.currentItem().text())
        nu = self.listWidget_2.currentItem().text()
        se = self.listWidget_2.currentItem()

    def logout_NumClicked(self):
        #online 상태일 때만 사용
        logmsg = QMessageBox()
        logmsg.setText("　　LogOut!　　　")
        logmsg.setWindowTitle("LOGOUT")
        logmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
        logmsg.exec_()

        Login.logout()
        login.main_dialog.show()
        self.close()

    def login_NumClicked(self):
        #offline 상태일 때만 사용
        logmsg = QMessageBox()
        logmsg.setText("　　LogIn!　　　")
        logmsg.setWindowTitle("LOGIN")
        logmsg.setFont(QFont("Noto Sans KR", 12, QFont.Bold, italic=False))
        logmsg.exec_()

        login.main_dialog.show()
        self.close()

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
                    item.setBackground(QColor(colors[1]))
                self.listWidget_1.addItem(item)
            if t.rstrip().split('?')[0] == 'folder':
                item = QListWidgetItem(t.rstrip().split('?')[1])
                if StateManagement.get_state(t.rstrip().split('?')[1]) == True:
                    item.setBackground(QColor(colors[0]))
                else :
                    item.setBackground(QColor(colors[1]))
                self.listWidget_2.addItem(item)


app = QApplication(sys.argv)
main_dialog = HideDialog() #hide 불러오기
#main_dialog.show()
#app.exec_()