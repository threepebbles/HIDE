# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hide.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(743, 555)
        Dialog.setMinimumSize(QtCore.QSize(743, 555))
        Dialog.setMaximumSize(QtCore.QSize(743, 555))
        Dialog.setStyleSheet("")
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setGeometry(QtCore.QRect(-30, -6, 801, 561))
        self.widget_3.setMinimumSize(QtCore.QSize(300, 500))
        
        self.widget_3.setObjectName("widget_3")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(630, 60, 102, 316))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lock_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.lock_pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.lock_pushButton.setMaximumSize(QtCore.QSize(100, 100))
        self.lock_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        
        self.lock_pushButton.setText("")
        self.lock_pushButton.setObjectName("lock_pushButton")
        self.verticalLayout.addWidget(self.lock_pushButton)
        self.unlock_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.unlock_pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.unlock_pushButton.setMaximumSize(QtCore.QSize(100, 100))
        
        self.unlock_pushButton.setText("")
        self.unlock_pushButton.setObjectName("unlock_pushButton")
        self.verticalLayout.addWidget(self.unlock_pushButton)
        self.quit_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.quit_pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.quit_pushButton.setMaximumSize(QtCore.QSize(100, 100))
        
        self.quit_pushButton.setText("")
        self.quit_pushButton.setObjectName("quit_pushButton")
        self.verticalLayout.addWidget(self.quit_pushButton)
        self.Select_pushButton = QtWidgets.QPushButton(Dialog)
        self.Select_pushButton.setGeometry(QtCore.QRect(10, 60, 231, 51))
        self.Select_pushButton.setText("")
        self.Select_pushButton.setObjectName("Select_pushButton")
        self.Folder_widget = QtWidgets.QWidget(Dialog)
        self.Folder_widget.setGeometry(QtCore.QRect(10, 119, 300, 421))
        self.Folder_widget.setMinimumSize(QtCore.QSize(300, 400))
        self.Folder_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        
        self.Folder_widget.setObjectName("Folder_widget")
        self.Folder_pushButton = QtWidgets.QPushButton(Dialog)
        self.Folder_pushButton.setGeometry(QtCore.QRect(320, 60, 231, 51))
        self.Folder_pushButton.setText("")
        self.Folder_pushButton.setObjectName("Folder_pushButton")
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(330, 180, 281, 351))
        
        self.listWidget_2.setObjectName("listWidget_2")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(319, 119, 301, 421))
        self.widget_2.setObjectName("widget_2")
        self.listWidget_1 = QtWidgets.QListWidget(Dialog)
        self.listWidget_1.setGeometry(QtCore.QRect(20, 180, 281, 351))
        self.listWidget_1.setObjectName("listWidget_1")
        self.Delete_pushButton = QtWidgets.QPushButton(Dialog)
        self.Delete_pushButton.setGeometry(QtCore.QRect(250, 60, 61, 51))
        self.Delete_pushButton.setText("")
        self.Delete_pushButton.setObjectName("Delete_pushButton")
        self.Delete_pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.Delete_pushButton_2.setGeometry(QtCore.QRect(560, 60, 61, 51))
        self.Delete_pushButton_2.setText("")
        self.Delete_pushButton_2.setObjectName("Delete_pushButton_2")
        self.logout_pushButton = QtWidgets.QPushButton(Dialog)
        self.logout_pushButton.setGeometry(QtCore.QRect(632, 387, 101, 31))
        self.logout_pushButton.setText("")
        self.logout_pushButton.setObjectName("logout_pushButton")
        self.login_pushButton = QtWidgets.QPushButton(Dialog)
        self.login_pushButton.setGeometry(QtCore.QRect(632, 427, 101, 31))
        self.login_pushButton.setText("")
        self.login_pushButton.setObjectName("login_pushButton")
        self.re_pushButton = QtWidgets.QPushButton(Dialog)
        self.re_pushButton.setGeometry(QtCore.QRect(632, 467, 101, 41))
        self.re_pushButton.setText("")
        self.re_pushButton.setObjectName("re_pushButton")
        self.widget_3.raise_()
        self.layoutWidget.raise_()
        self.Select_pushButton.raise_()
        self.Folder_widget.raise_()
        self.Folder_pushButton.raise_()
        self.widget_2.raise_()
        self.listWidget_2.raise_()
        self.listWidget_1.raise_()
        self.Delete_pushButton.raise_()
        self.Delete_pushButton_2.raise_()
        self.logout_pushButton.raise_()
        self.login_pushButton.raise_()
        self.re_pushButton.raise_()

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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
