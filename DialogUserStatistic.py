# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialoguserstatistic.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from Model import Database, User

class Ui_DialogUserStatistic(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.isAcceptDelete = False
        self.beforeChange = None
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(631, 192)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblName = QtWidgets.QLabel(Dialog)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 0, 0, 1, 1)
        self.lblPass = QtWidgets.QLabel(Dialog)
        self.lblPass.setObjectName("lblPass")
        self.gridLayout.addWidget(self.lblPass, 2, 0, 1, 1)
        self.editPass = QtWidgets.QLineEdit(Dialog)
        self.editPass.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editPass.setObjectName("editPass")
        self.gridLayout.addWidget(self.editPass, 2, 1, 1, 1)
        self.editName = QtWidgets.QLineEdit(Dialog)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 1)
        self.lblUsername = QtWidgets.QLabel(Dialog)
        self.lblUsername.setObjectName("lblUsername")
        self.gridLayout.addWidget(self.lblUsername, 1, 0, 1, 1)
        self.editUsername = QtWidgets.QLineEdit(Dialog)
        self.editUsername.setObjectName("editUsername")
        self.gridLayout.addWidget(self.editUsername, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAddUser = QtWidgets.QPushButton(Dialog)
        self.btnAddUser.setObjectName("btnAddUser")
        self.horizontalLayout.addWidget(self.btnAddUser)
        self.btnDeleteUser = QtWidgets.QPushButton(Dialog)
        self.btnDeleteUser.setObjectName("btnDeleteUser")
        self.horizontalLayout.addWidget(self.btnDeleteUser)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tableUser = QtWidgets.QTableWidget(Dialog)
        self.tableUser.setObjectName("tableUser")
        self.tableUser.setColumnCount(3)
        self.tableUser.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableUser.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableUser.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableUser.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_2.addWidget(self.tableUser)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.editName, self.editUsername)
        Dialog.setTabOrder(self.editUsername, self.editPass)
        Dialog.setTabOrder(self.editPass, self.btnAddUser)
        Dialog.setTabOrder(self.btnAddUser, self.btnDeleteUser)
        Dialog.setTabOrder(self.btnDeleteUser, self.tableUser)

        self.setupWidget()
        self.linkWidget()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Danh sách User"))
        self.lblName.setText(_translate("Dialog", "Họ và tên:"))
        self.lblPass.setText(_translate("Dialog", "Password: "))
        self.lblUsername.setText(_translate("Dialog", "Username: "))
        self.btnAddUser.setText(_translate("Dialog", "Thêm User"))
        self.btnDeleteUser.setText(_translate("Dialog", "Xóa User"))
        item = self.tableUser.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Họ tên"))
        item = self.tableUser.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Username"))
        item = self.tableUser.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Password"))

    def setupWidget(self):
        data = Database()
        listUser = data.getListUser()
        for user in listUser:
            self.addUserIntoTable(user)
        data.closeDatabase()

    def linkWidget(self):
        self.btnAddUser.clicked.connect(self.onAddUser)
        self.btnDeleteUser.clicked.connect(self.onDeleteUser)
        self.tableUser.cellChanged.connect(self.onCellChange)
        self.tableUser.cellClicked.connect(self.onCellClick)
        self.tableUser.cellDoubleClicked.connect(self.onDoubleClickCell)

    def onAddUser(self):
        data = Database()
        
        user = User()
        user.name = self.editName.text()
        user.username = self.editUsername.text()
        user.passWord = self.editPass.text()

        try:
            data.insertUser(user)
        except sqlite3.IntegrityError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Your username has already existed !!!")
            msg.setInformativeText("Please choose another username !!!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return

        self.addUserIntoTable(user)
        data.closeDatabase()
        
        self.editName.clear()
        self.editPass.clear()
        self.editUsername.clear()

    def onDeleteUser(self):
        rowDelete = self.tableUser.currentRow()
        print(rowDelete)
        if rowDelete == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Delete This User ??")
            msg.setText("You can not delete Root user ")
            msg.setInformativeText("Please try again with the other user !!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return
        if rowDelete == -1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Which User ??")
            msg.setText("You have not choose user you wanna delete ")
            msg.setInformativeText("Please choose one user to delete!!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return

        def message(i):
            if i.text() == "&Cancel":
                self.isAcceptDelete = False
            elif i.text() == "&OK":
                self.isAcceptDelete = True
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Delete This User ??")
        msg.setText("You really want to delete this user ??")
        msg.setInformativeText("You can not undo this process!! Really want to do this ???")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(message)
        msg.exec()
        
        if self.isAcceptDelete: 
            print(rowDelete)
            data = Database()
            username = self.tableUser.item(rowDelete,1).text()
            print(username)
            data.deleteUser(username)
            self.tableUser.removeRow(rowDelete)
        else:
            return 

    def onCellChange(self, row, col):
        dataChange = self.tableUser.item(row, col).text()

        if col == 1:
            if dataChange != self.beforeChange:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Không thể sửa Username !!")
                msg.setInformativeText("Vui lòng thử lại !!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec()
                self.tableUser.item(row,col).setText(self.beforeChange)
                return
            else:
                return
        username = self.tableUser.item(row, 1).text()
        data = Database()
        if col == 0:
            data.updateNameOfUser(username,dataChange)
        if col == 2:
            data.updatePassOfUser(username,dataChange)
        data.closeDatabase()

    def onCellClick(self,row, col):
        user = User()
        user.name = self.tableUser.item(row,0).text()
        user.username = self.tableUser.item(row,1).text()
        user.passWord = self.tableUser.item(row,2).text()

        self.editName.setText(user.name)
        self.editUsername.setText(user.username)
        self.editPass.setText(user.passWord)

    def onDoubleClickCell(self, row, col):
        self.beforeChange = self.tableUser.item(row,col).text()
        print(self.beforeChange)

    def addUserIntoTable(self, user):
        rowPos = self.tableUser.rowCount()
        self.tableUser.insertRow(rowPos)
        self.tableUser.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(user.name))
        self.tableUser.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(user.username))
        self.tableUser.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(user.passWord))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()