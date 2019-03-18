# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialognewitem.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from Model import Item, Database

class Ui_DialogNewItem(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.isAccept = 0
        self.setupUi(self)
        
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))


    def setupUi(self, DialogNewItem):
        DialogNewItem.setObjectName("DialogNewItem")
        DialogNewItem.resize(337, 145)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogNewItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblIName = QtWidgets.QLabel(DialogNewItem)
        self.lblIName.setObjectName("lblIName")
        self.gridLayout.addWidget(self.lblIName, 0, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(DialogNewItem)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 1)
        self.lblID = QtWidgets.QLabel(DialogNewItem)
        self.lblID.setObjectName("lblID")
        self.gridLayout.addWidget(self.lblID, 1, 0, 1, 1)
        self.editID = QtWidgets.QLineEdit(DialogNewItem)
        self.editID.setObjectName("editID")
        self.gridLayout.addWidget(self.editID, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogNewItem)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogNewItem)
        self.buttonBox.accepted.connect(DialogNewItem.accept)
        self.buttonBox.rejected.connect(DialogNewItem.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNewItem)
        
        self.setupWidget()
        self.linkWidget()

    def retranslateUi(self, DialogNewItem):
        _translate = QtCore.QCoreApplication.translate
        DialogNewItem.setWindowTitle(_translate("DialogNewItem", "Thêm mặt hàng"))
        self.lblIName.setText(_translate("DialogNewItem", "Tên mặt hàng:"))
        self.lblID.setText(_translate("DialogNewItem", "ID:"))

    def setupWidget(self):
        date = datetime.datetime.now().strftime("IT-%d%m%Y%H%M%S")
        self.editID.setText(date)

    def linkWidget(self):
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)

    def onAccept(self):
        if len(self.editID.text()) and " " not in list(self.editID.text()):
            
            item = Item()
            item.name = self.editName.text()
            item.idItem = self.editID.text()

            data = Database()
            try:
                data.insertItem(item)
            except sqlite3.IntegrityError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("ID này đã tồn tại !!")
                msg.setInformativeText("Xin hãy chọn một ID khác và thử lại !!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec()
                self.isAccept = -1
                return
            self.isAccept = 1
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("ID này đã tồn tại !!")
            msg.setInformativeText("Xin hãy chọn một ID khác và thử lại !!")
            msg.setStandardButton(QtWidgets.QMessageBox.Ok)
            exec()
            self.isAccept = -1


    def onReject(self):
        self.isAccept = 0
        self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.isAccept = 0
            self.close()