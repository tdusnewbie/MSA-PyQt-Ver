# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/dialogsignup.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from Model import Database, User

class Ui_DialogSignUp(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.isShowPass = False
        self.isAccept = 0
        self.user = None
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))

    def setupUi(self, DialogSignUp):
        DialogSignUp.setObjectName("DialogSignUp")
        DialogSignUp.resize(347, 184)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSignUp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblName = QtWidgets.QLabel(DialogSignUp)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 0, 0, 1, 1)
        self.lblUsername = QtWidgets.QLabel(DialogSignUp)
        self.lblUsername.setObjectName("lblUsername")
        self.gridLayout.addWidget(self.lblUsername, 1, 0, 1, 1)
        self.lblPassword = QtWidgets.QLabel(DialogSignUp)
        self.lblPassword.setObjectName("lblPassword")
        self.gridLayout.addWidget(self.lblPassword, 2, 0, 1, 1)
        self.editPass = QtWidgets.QLineEdit(DialogSignUp)
        self.editPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPass.setObjectName("editPass")
        self.gridLayout.addWidget(self.editPass, 2, 1, 1, 1)
        self.btnShowPass = QtWidgets.QToolButton(DialogSignUp)
        self.btnShowPass.setObjectName("btnShowPass")
        self.btnShowPass.setIcon(QtGui.QIcon("./Icon/icons8-eye-48.png"))
        self.btnShowPass.setIconSize(QtCore.QSize(16,16))

        self.gridLayout.addWidget(self.btnShowPass, 2, 2, 1, 1)
        self.editUsername = QtWidgets.QLineEdit(DialogSignUp)
        self.editUsername.setObjectName("editUsername")
        self.gridLayout.addWidget(self.editUsername, 1, 1, 1, 2)
        self.editName = QtWidgets.QLineEdit(DialogSignUp)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogSignUp)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.linkWidget()

        self.retranslateUi(DialogSignUp)
        self.buttonBox.accepted.connect(DialogSignUp.accept)
        self.buttonBox.rejected.connect(DialogSignUp.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSignUp)
        DialogSignUp.setTabOrder(self.editName, self.editUsername)
        DialogSignUp.setTabOrder(self.editUsername, self.editPass)
        DialogSignUp.setTabOrder(self.editPass, self.btnShowPass)

    def retranslateUi(self, DialogSignUp):
        _translate = QtCore.QCoreApplication.translate
        DialogSignUp.setWindowTitle(_translate("DialogSignUp", "Đăng kí tài khoản"))
        self.lblName.setText(_translate("DialogSignUp", "Họ và tên:"))
        self.lblUsername.setText(_translate("DialogSignUp", "Username: "))
        self.lblPassword.setText(_translate("DialogSignUp", "Password:"))
        self.btnShowPass.setText(_translate("DialogSignUp", "..."))

    def linkWidget(self):
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)
        self.btnShowPass.clicked.connect(self.onShowPass)

    def onAccept(self):
        if len(self.editUsername.text()) !=0 and " " not in list(self.editUsername.text()):
            self.user = User()
            self.user.name = self.editName.text()
            self.user.username = self.editUsername.text()
            self.user.passWord = self.editPass.text()

            data = Database()
            try:
                data.insertUser(self.user)
            except sqlite3.IntegrityError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Your username has already existed !!!")
                msg.setInformativeText("Please choose another username !!!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec()
                self.isAccept = -1
                return
            self.isAccept = 1
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Your username cannot be empty or has space in there !!!")
            msg.setInformativeText("Please choose another username !!!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            self.isAccept = -1

    def onReject(self):
        self.isAccept = 0
        self.close()

    def onShowPass(self):
        self.isShowPass = not self.isShowPass
        if self.isShowPass:
            self.editPass.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.editPass.setEchoMode(QtWidgets.QLineEdit.Password)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.isAccept = 0 
            self.close()