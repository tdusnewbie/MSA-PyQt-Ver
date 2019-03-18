# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/dialogaddbill.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import datetime
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from Model import Database, Bill


class Ui_DialogAddBill(QtWidgets.QDialog):
    def __init__(self, parent = None, userCreate = None):
        QtWidgets.QDialog.__init__(self, parent)

        self.headerID = "##"
        self.footerID = "##"
        self.indexType = 0
        self.userCreate = userCreate
        self.bill = None
        self.isAccept = 0

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))

    def setupUi(self, DialogAddBill):
        DialogAddBill.setObjectName("DialogAddBill")
        DialogAddBill.resize(447, 429)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogAddBill)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.editID = QtWidgets.QLineEdit(DialogAddBill)
        self.editID.setObjectName("editID")
        self.gridLayout.addWidget(self.editID, 2, 1, 1, 3)
        self.lblItem = QtWidgets.QLabel(DialogAddBill)
        self.lblItem.setObjectName("lblItem")
        self.gridLayout.addWidget(self.lblItem, 0, 0, 1, 1)
        self.spinAmount = QtWidgets.QSpinBox(DialogAddBill)
        self.spinAmount.setObjectName("spinAmount")
        self.gridLayout.addWidget(self.spinAmount, 3, 1, 1, 3)
        self.lblID = QtWidgets.QLabel(DialogAddBill)
        self.lblID.setObjectName("lblID")
        self.gridLayout.addWidget(self.lblID, 2, 0, 1, 1)
        self.lblType = QtWidgets.QLabel(DialogAddBill)
        self.lblType.setObjectName("lblType")
        self.gridLayout.addWidget(self.lblType, 1, 0, 1, 1)
        self.lblAmount = QtWidgets.QLabel(DialogAddBill)
        self.lblAmount.setObjectName("lblAmount")
        self.gridLayout.addWidget(self.lblAmount, 3, 0, 1, 1)
        self.comboItem = QtWidgets.QComboBox(DialogAddBill)
        self.comboItem.setObjectName("comboItem")
        self.gridLayout.addWidget(self.comboItem, 0, 1, 1, 3)
        self.comboType = QtWidgets.QComboBox(DialogAddBill)
        self.comboType.setObjectName("comboType")
        self.gridLayout.addWidget(self.comboType, 1, 1, 1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblImage = QtWidgets.QLabel(DialogAddBill)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImage.sizePolicy().hasHeightForWidth())
        self.lblImage.setSizePolicy(sizePolicy)
        self.lblImage.setObjectName("lblImage")
        self.verticalLayout.addWidget(self.lblImage)
        self.imgAvatar = QtWidgets.QLabel(DialogAddBill)
        self.imgAvatar.setFrameShape(QtWidgets.QFrame.Box)
        self.imgAvatar.setObjectName("imgAvatar")
        self.verticalLayout.addWidget(self.imgAvatar)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(DialogAddBill)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioCustom = QtWidgets.QRadioButton(self.groupBox)
        self.radioCustom.setObjectName("radioCustom")
        self.horizontalLayout.addWidget(self.radioCustom)
        self.radioUnit = QtWidgets.QRadioButton(self.groupBox)
        self.radioUnit.setObjectName("radioUnit")
        self.horizontalLayout.addWidget(self.radioUnit)
        self.radioWhole = QtWidgets.QRadioButton(self.groupBox)
        self.radioWhole.setObjectName("radioWhole")
        self.horizontalLayout.addWidget(self.radioWhole)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblTime = QtWidgets.QLabel(DialogAddBill)
        self.lblTime.setObjectName("lblTime")
        self.gridLayout_2.addWidget(self.lblTime, 1, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(DialogAddBill)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 1, 1, 1, 1)
        self.editPrice = QtWidgets.QLineEdit(DialogAddBill)
        self.editPrice.setObjectName("editPrice")
        self.gridLayout_2.addWidget(self.editPrice, 0, 1, 1, 1)
        self.lblPrice = QtWidgets.QLabel(DialogAddBill)
        self.lblPrice.setObjectName("lblPrice")
        self.gridLayout_2.addWidget(self.lblPrice, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.lblNotice = QtWidgets.QLabel(DialogAddBill)
        self.lblNotice.setObjectName("lblNotice")
        self.verticalLayout_2.addWidget(self.lblNotice)
        self.textNotice = QtWidgets.QPlainTextEdit(DialogAddBill)
        self.textNotice.setObjectName("textNotice")
        self.verticalLayout_2.addWidget(self.textNotice)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogAddBill)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DialogAddBill)
        self.buttonBox.accepted.connect(DialogAddBill.accept)
        self.buttonBox.rejected.connect(DialogAddBill.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAddBill)
        DialogAddBill.setTabOrder(self.comboItem, self.comboType)
        DialogAddBill.setTabOrder(self.comboType, self.editID)
        DialogAddBill.setTabOrder(self.editID, self.spinAmount)
        DialogAddBill.setTabOrder(self.spinAmount, self.radioCustom)
        DialogAddBill.setTabOrder(self.radioCustom, self.radioUnit)
        DialogAddBill.setTabOrder(self.radioUnit, self.radioWhole)
        DialogAddBill.setTabOrder(self.radioWhole, self.editPrice)
        DialogAddBill.setTabOrder(self.editPrice, self.dateTimeEdit)
        DialogAddBill.setTabOrder(self.dateTimeEdit, self.textNotice)

        self.setupWidget()
        self.linkWidget()

    def retranslateUi(self, DialogAddBill):
        _translate = QtCore.QCoreApplication.translate
        DialogAddBill.setWindowTitle(_translate("DialogAddBill", "Thêm Đơn Hàng"))
        self.lblItem.setText(_translate("DialogAddBill", "Mặt hàng:"))
        self.lblID.setText(_translate("DialogAddBill", "ID:"))
        self.lblType.setText(_translate("DialogAddBill", "Loại hàng:"))
        self.lblAmount.setText(_translate("DialogAddBill", "Số lượng xuất:"))
        self.lblImage.setText(_translate("DialogAddBill", "Hình ảnh:"))
        self.imgAvatar.setText(_translate("DialogAddBill", "No Image"))
        self.groupBox.setTitle(_translate("DialogAddBill", "Phương thức bán:"))
        self.radioCustom.setText(_translate("DialogAddBill", "Theo giá Vốn"))
        self.radioUnit.setText(_translate("DialogAddBill", "Theo giá lẻ"))
        self.radioWhole.setText(_translate("DialogAddBill", "Theo giá sỉ"))
        self.lblTime.setText(_translate("DialogAddBill", "Giờ tạo:"))
        self.lblPrice.setText(_translate("DialogAddBill", "Thành giá:"))
        self.lblNotice.setText(_translate("DialogAddBill", "Ghi chú:"))


    def setupWidget(self):
        data = Database()
        self.listItem = data.getListItem()
        for item in self.listItem:
            self.comboItem.addItem(item.name)
        
        self.spinAmount.setMinimum(1)

        self.dateTimeEdit.setDisplayFormat("dd/MM/yyyy hh:mm")
        date = datetime.datetime.now().date().strftime("%d/%m/%Y")
        time = datetime.datetime.now().time().strftime("%H:%M")
        # print(date + " " + time)
        now = QtCore.QDateTime.fromString(date + " " + time, "dd/MM/yyyy hh:mm")
        self.dateTimeEdit.setDateTime(now)

        self.radioUnit.setChecked(True)

        self.comboItem.setCurrentIndex(0)
        
        if len(self.listItem) != 0:
            self.listType = self.listItem[0].listType
            for typeItem in self.listType:
                self.comboType.addItem(typeItem.name)
            
            self.comboItem.setCurrentIndex(0)

            self.headerID = self.listItem[0].idItem
            if len(self.listType) != 0:
                self.footerID = self.listType[0].idType
                self.editPrice.setText(str(self.listType[0].unitPrice))
                self.spinAmount.setMaximum(self.listType[0].amount)
                self.onSetImage(self.listType[0].imagePath)

        
        idBill = self.headerID + "-" + self.footerID

        self.editID.setText(idBill)
          

    def linkWidget(self):
        self.comboItem.currentIndexChanged.connect(self.onChangeIndexOfItem)
        self.comboType.currentIndexChanged.connect(self.onChangeIndexOfType)
        self.spinAmount.valueChanged.connect(self.onChangeValueAmount)
        self.radioCustom.clicked.connect(self.onCheckRadio)
        self.radioUnit.clicked.connect(self.onCheckRadio)
        self.radioWhole.clicked.connect(self.onCheckRadio)
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)

    def onChangeIndexOfItem(self, index):
        self.comboType.clear()
        self.listType = self.listItem[index].listType
        self.headerID = self.listItem[index].idItem
        for typeItem in self.listType:
            self.comboType.addItem(typeItem.name)

    def onChangeIndexOfType(self, index):
        self.indexType = index
        self.footerID = self.listType[index].idType
        idBill = self.headerID + "-" + self.footerID
        self.editID.setText(idBill)
        self.spinAmount.setMaximum(self.listType[index].amount)
        if self.listType[index].amount <= 5:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Loại hàng này còn khá ít !!")
            msg.setInformativeText("Xin hãy lưu ý nhập thêm hàng về !!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()

        self.onSetImage(self.listType[index].imagePath)
        amount = self.spinAmount.text()
        self.onChangeValueAmount(amount)
        

    def onChangeValueAmount(self, value):
        if self.radioUnit.isChecked():
            price = self.listType[self.indexType].unitPrice * int(value)
        elif self.radioWhole.isChecked():
            price = self.listType[self.indexType].wholePrice * int(value)
        elif self.radioCustom.isChecked():
            price = self.listType[self.indexType].originPrice * int(value)

        self.editPrice.setText(str(price))

    def onCheckRadio(self):
        amount = self.spinAmount.text()
        self.onChangeValueAmount(amount)

    def onAccept(self):
        idBill = self.editID.text()
        if len(idBill) != 0 and " " not in list(idBill):
            # Create a new Type Item 
            self.bill = Bill()
            self.bill.nameItem = self.comboItem.currentText()
            self.bill.nameType = self.comboType.currentText()
            self.bill.idBill = idBill
            self.bill.amount = self.spinAmount.text()
            if self.radioCustom.isChecked():
                self.bill.saleType = self.radioCustom.text()
            elif self.radioUnit.isChecked():
                self.bill.saleType = self.radioUnit.text()
            elif self.radioWhole.isChecked():
                self.bill.saleType = self.radioWhole.text()

            self.bill.price = self.editPrice.text()
            
            date = self.dateTimeEdit.date()
            time = self.dateTimeEdit.time()

            date = date.toString("dd/MM/yyyy")
            time = time.toString("hh:mm:ss")

            self.bill.createdDate = date
            self.bill.createdTime = time

            self.bill.createdUser = self.userCreate

            self.bill.notice = self.textNotice.toPlainText()

            # Add new Bill into database
            data = Database()
            try:
                data.insertBill(self.bill)

            except sqlite3.IntegrityError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("ID này đã được một tài khoản khác sử dụng !!")
                msg.setText("Xin hãy chọn một ID khác !!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec()
                self.isAccept = -1
                return
            maxAmount = self.spinAmount.maximum()
            existedAmount = int(maxAmount) - int(self.spinAmount.text())
            print(existedAmount)
            data.updateTypeAmount(self.footerID, existedAmount)
            self.isAccept = 1

        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("ID Không thể để trống hoặc có chứa khoảng trắng !!!")
            msg.setInformativeText("Xin hãy thêm một ID hoặc xóa dấu khoảng trắng !!!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            self.isAccept = -1
    
    def onReject(self):
        self.isAccept = 0
        self.close()

    def onSetImage(self, pathImage):
        self.imgAvatar.setScaledContents(True)
        self.imgAvatar.setSizePolicy(QtWidgets.QSizePolicy.Ignored,QtWidgets.QSizePolicy.Ignored)
        self.imgAvatar.setPixmap(QtGui.QPixmap(pathImage))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.isAccept = 0
            self.close()

