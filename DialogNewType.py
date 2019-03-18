# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/dialognewtype.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from Model import Database, TypeItem, Item

class Ui_DialogNewType(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.isAccept = 0
        self.setupUi(self)
        
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))

    def setupUi(self, DialogNewType):
        DialogNewType.setObjectName("DialogNewType")
        DialogNewType.resize(560, 318)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogNewType)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblItem = QtWidgets.QLabel(DialogNewType)
        self.lblItem.setObjectName("lblItem")
        self.gridLayout.addWidget(self.lblItem, 0, 0, 1, 1)
        self.comboItem = QtWidgets.QComboBox(DialogNewType)
        self.comboItem.setObjectName("comboItem")
        self.gridLayout.addWidget(self.comboItem, 0, 1, 1, 1)
        self.lblName = QtWidgets.QLabel(DialogNewType)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 1, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(DialogNewType)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 1, 1, 1, 1)
        self.lblID = QtWidgets.QLabel(DialogNewType)
        self.lblID.setObjectName("lblID")
        self.gridLayout.addWidget(self.lblID, 2, 0, 1, 1)
        self.editID = QtWidgets.QLineEdit(DialogNewType)
        self.editID.setObjectName("editID")
        self.gridLayout.addWidget(self.editID, 2, 1, 1, 1)
        self.lblAmount = QtWidgets.QLabel(DialogNewType)
        self.lblAmount.setObjectName("lblAmount")
        self.gridLayout.addWidget(self.lblAmount, 3, 0, 1, 1)
        self.spinAmount = QtWidgets.QSpinBox(DialogNewType)
        self.spinAmount.setObjectName("spinAmount")
        self.gridLayout.addWidget(self.spinAmount, 3, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblImage = QtWidgets.QLabel(DialogNewType)
        self.lblImage.setObjectName("lblImage")
        self.gridLayout_2.addWidget(self.lblImage, 0, 0, 1, 1)
        self.editPath = QtWidgets.QLineEdit(DialogNewType)
        self.editPath.setObjectName("editPath")
        self.gridLayout_2.addWidget(self.editPath, 0, 1, 1, 1)
        self.btnBrowse = QtWidgets.QToolButton(DialogNewType)
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout_2.addWidget(self.btnBrowse, 0, 2, 1, 1)
        self.imgAvatar = QtWidgets.QLabel(DialogNewType)
        self.imgAvatar.setFrameShape(QtWidgets.QFrame.Box)
        self.imgAvatar.setObjectName("imgAvatar")
        self.gridLayout_2.addWidget(self.imgAvatar, 1, 0, 1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblUnit = QtWidgets.QLabel(DialogNewType)
        self.lblUnit.setObjectName("lblUnit")
        self.horizontalLayout.addWidget(self.lblUnit)
        self.editUnit = QtWidgets.QLineEdit(DialogNewType)
        self.editUnit.setObjectName("editUnit")
        self.horizontalLayout.addWidget(self.editUnit)
        self.lblWhole = QtWidgets.QLabel(DialogNewType)
        self.lblWhole.setObjectName("lblWhole")
        self.horizontalLayout.addWidget(self.lblWhole)
        self.editWhole = QtWidgets.QLineEdit(DialogNewType)
        self.editWhole.setObjectName("editWhole")
        self.horizontalLayout.addWidget(self.editWhole)
        self.lblOrigin = QtWidgets.QLabel(DialogNewType)
        self.lblOrigin.setObjectName("lblOrigin")
        self.horizontalLayout.addWidget(self.lblOrigin)
        self.editOrigin = QtWidgets.QLineEdit(DialogNewType)
        self.editOrigin.setObjectName("editOrigin")
        self.horizontalLayout.addWidget(self.editOrigin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lblNotice = QtWidgets.QLabel(DialogNewType)
        self.lblNotice.setObjectName("lblNotice")
        self.verticalLayout.addWidget(self.lblNotice)
        self.textNotice = QtWidgets.QPlainTextEdit(DialogNewType)
        self.textNotice.setObjectName("textNotice")
        self.verticalLayout.addWidget(self.textNotice)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogNewType)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.linkWidget()

        self.retranslateUi(DialogNewType)
        self.buttonBox.accepted.connect(DialogNewType.accept)
        self.buttonBox.rejected.connect(DialogNewType.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNewType)
        DialogNewType.setTabOrder(self.comboItem, self.editName)
        DialogNewType.setTabOrder(self.editName, self.editID)
        DialogNewType.setTabOrder(self.editID, self.spinAmount)
        DialogNewType.setTabOrder(self.spinAmount, self.editUnit)
        DialogNewType.setTabOrder(self.editUnit, self.editWhole)
        DialogNewType.setTabOrder(self.editWhole, self.editOrigin)
        DialogNewType.setTabOrder(self.editOrigin, self.editPath)
        DialogNewType.setTabOrder(self.editPath, self.btnBrowse)
        DialogNewType.setTabOrder(self.btnBrowse, self.textNotice)

        self.SetupWidget()

    def retranslateUi(self, DialogNewType):
        _translate = QtCore.QCoreApplication.translate
        DialogNewType.setWindowTitle(_translate("DialogNewType", "Thêm loại hàng"))
        self.lblItem.setText(_translate("DialogNewType", "Thuộc mặt hàng:"))
        self.lblName.setText(_translate("DialogNewType", "Tên loại hàng:"))
        self.lblID.setText(_translate("DialogNewType", "ID loại hàng:"))
        self.lblAmount.setText(_translate("DialogNewType", "Số lượng  tồn:"))
        self.lblImage.setText(_translate("DialogNewType", "Hình ảnh: "))
        self.btnBrowse.setText(_translate("DialogNewType", "..."))
        self.imgAvatar.setText(_translate("DialogNewType", "No Image"))
        self.lblUnit.setText(_translate("DialogNewType", "Giá lẻ:"))
        self.lblWhole.setText(_translate("DialogNewType", "Giá sỉ"))
        self.lblOrigin.setText(_translate("DialogNewType", "Giá vốn:"))
        self.lblNotice.setText(_translate("DialogNewType", "Ghi chú"))

    def linkWidget(self):
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)
        self.btnBrowse.clicked.connect(self.onBrowse)
        self.editPath.returnPressed.connect(self.onEditPathReturn)

    def SetupWidget(self):
        data = Database()
        self.listItem = data.getListItemWithoutType()
        for item in self.listItem:
            self.comboItem.addItem(item.name)

        data.closeDatabase()

        self.spinAmount.setMinimum(0)
        self.spinAmount.setMaximum(10**9)

        self.btnBrowse.setIcon(QtGui.QIcon("Image/icons8-browse-folder-50.png"))
        self.btnBrowse.setIconSize(QtCore.QSize(16,16))
        
        date = datetime.datetime.now().strftime("TY-%d%m%Y%H%M%S")
        self.editID.setText(date)

    def onAccept(self):
        idType = self.editID.text()
        if len(idType) != 0 and " " not in list(idType):
            # Create a new Type Item 
            typeItem = TypeItem()
            typeItem.name = self.editName.text()
            typeItem.idType = idType
            typeItem.idParent = self.listItem[self.comboItem.currentIndex()].idItem
            typeItem.amount = self.spinAmount.text()
            typeItem.unitPrice = self.editUnit.text()
            typeItem.wholePrice = self.editWhole.text()
            typeItem.originPrice = self.editOrigin.text()
            typeItem.imagePath = self.editPath.text()
            typeItem.notice = self.textNotice.toPlainText()

            # Add new Type Item into database
            data = Database()
            try:
                data.insertTypeItem(typeItem)
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
            msg.setText("ID Không thể để trống hoặc có chứa khoảng trắng !!")
            msg.setInformativeText("Xin hãy chọn một ID khác và thử lại !!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            self.isAccept = -1


    def onReject(self):
        self.isAccept = 0
        self.close()

    def onBrowse(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Choose Image",".",
            "Image files (*.png *.jpg *.gif)")

        self.editPath.setText(filePath)
        print(filePath)
        self.imgAvatar.setScaledContents(True)
        self.imgAvatar.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
        self.imgAvatar.setPixmap(QtGui.QPixmap(filePath))

    def onEditPathReturn(self):
        filePath = self.editPath.text()
        self.imgAvatar.setScaledContents(True)
        self.imgAvatar.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
        self.imgAvatar.setPixmap(QtGui.QPixmap(filePath))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.isAccept = 0
            self.close()