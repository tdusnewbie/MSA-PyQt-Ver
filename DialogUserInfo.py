# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialoguserinfo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Model import Database, User

class Ui_DialogUserInfo(QtWidgets.QDialog):
    def __init__(self, parent = None, username = None):
        QtWidgets.QDialog.__init__(self, parent)
        
        self.username = username
        self.beforeChange = None
        self.passEditted = False
        self.nameEditted = False
        
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 222)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lblUsername = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUsername.sizePolicy().hasHeightForWidth())
        self.lblUsername.setSizePolicy(sizePolicy)
        self.lblUsername.setObjectName("lblUsername")
        self.gridLayout.addWidget(self.lblUsername, 1, 0, 1, 1)
        self.lblName = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblName.sizePolicy().hasHeightForWidth())
        self.lblName.setSizePolicy(sizePolicy)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 0, 0, 1, 1)
        self.editUsername = QtWidgets.QLineEdit(self.groupBox)
        self.editUsername.setObjectName("editUsername")
        self.gridLayout.addWidget(self.editUsername, 1, 1, 1, 1)
        self.lblPass = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPass.sizePolicy().hasHeightForWidth())
        self.lblPass.setSizePolicy(sizePolicy)
        self.lblPass.setObjectName("lblPass")
        self.gridLayout.addWidget(self.lblPass, 2, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(self.groupBox)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 1)
        self.editPass = QtWidgets.QLineEdit(self.groupBox)
        self.editPass.setObjectName("editPass")
        self.gridLayout.addWidget(self.editPass, 2, 1, 1, 1)
        self.btnEditPass = QtWidgets.QToolButton(self.groupBox)
        self.btnEditPass.setObjectName("btnEditPass")
        self.gridLayout.addWidget(self.btnEditPass, 2, 2, 1, 1)
        self.btnEditName = QtWidgets.QToolButton(self.groupBox)
        self.btnEditName.setObjectName("btnEditName")
        self.gridLayout.addWidget(self.btnEditName, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.editName, self.btnEditName)
        Dialog.setTabOrder(self.btnEditName, self.editUsername)
        Dialog.setTabOrder(self.editUsername, self.editPass)
        Dialog.setTabOrder(self.editPass, self.btnEditPass)
        
        self.setupWidget()
        self.linkWidget()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Thông tin User"))
        self.groupBox.setTitle(_translate("Dialog", "User Information"))
        self.lblUsername.setText(_translate("Dialog", "Username:"))
        self.lblName.setText(_translate("Dialog", "Họ và tên:"))
        self.lblPass.setText(_translate("Dialog", "Password"))
        self.btnEditPass.setText(_translate("Dialog", "..."))
        self.btnEditName.setText(_translate("Dialog", "..."))

    def setupWidget(self):
        data = Database()
        user = data.getUserInfo(self.username)
        
        self.btnEditName.setIcon(QtGui.QIcon("./Icon/icons8-pencil-26.png"))
        self.btnEditName.setIconSize(QtCore.QSize(16,16))
        self.btnEditPass.setIcon(QtGui.QIcon("./Icon/icons8-pencil-26.png"))
        self.btnEditPass.setIconSize(QtCore.QSize(16,16))

        self.editName.setText(user.name)
        self.editUsername.setText(user.username)
        self.editPass.setText(user.passWord)

        self.editName.setReadOnly(True)
        self.editUsername.setReadOnly(True)
        self.editPass.setReadOnly(True)

    def linkWidget(self):
        self.btnEditName.clicked.connect(self.onAllowEditNameOfUser)
        self.btnEditPass.clicked.connect(self.onAllowEditPassOfUser)
        self.editName.editingFinished.connect(self.onReturnEditName)
        self.editPass.editingFinished.connect(self.onReturnEditPass)
        self.buttonBox.accepted.connect(self.onAccept)

    def onAllowEditNameOfUser(self):
        self.editPass.setReadOnly(True)
        self.editName.setReadOnly(False)
        self.beforeChange = self.editName.text()
        self.editName.setFocus()

    def onAllowEditPassOfUser(self):
        self.editName.setReadOnly(True)
        self.editPass.setReadOnly(False)
        self.beforeChange = self.editName.text()
        self.editPass.setFocus()

    def onReturnEditName(self):
        nameChanged = self.editName.text()
        if self.beforeChange != nameChanged:
            self.nameEditted = True
        self.editName.setReadOnly(True)

    def onReturnEditPass(self):
        passChanged = self.editPass.text()
        if self.beforeChange != passChanged:
            self.passEditted = True
        self.editPass.setReadOnly(True)

    def onAccept(self):
        data = Database()
        if self.nameEditted:
            nameChanged = self.editName.text()
            data.updateNameOfUser(self.username,nameChanged)
        
        if self.passEditted:
            passChanged = self.editPass.text()
            data.updatePassOfUser(self.username,passChanged)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()