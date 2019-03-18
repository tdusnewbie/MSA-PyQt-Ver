# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import sys
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from DialogAddBill import Ui_DialogAddBill
from DialogNewItem import Ui_DialogNewItem
from DialogNewType import Ui_DialogNewType
from DialogItemStatistic import Ui_DialogItemStatistic
from DialogBillStatistic import Ui_DialogBillStatistic
from DialogSignUp import Ui_DialogSignUp
from DialogUserInfo import Ui_DialogUserInfo
from DialogUserStatistic import Ui_DialogUserStatistic
from Model import Database
from ExportFile import *

class Ui_MainWindow(object):
    def __init__(self):
        self.isShowPass = True
        self.MainWindow = None

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 346)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.loginPage)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lblUsername = QtWidgets.QLabel(self.loginPage)
        self.lblUsername.setObjectName("lblUsername")
        self.gridLayout.addWidget(self.lblUsername, 2, 0, 1, 1)
        self.lblPassword = QtWidgets.QLabel(self.loginPage)
        self.lblPassword.setObjectName("lblPassword")
        self.gridLayout.addWidget(self.lblPassword, 3, 0, 1, 1)
        self.editPassword = QtWidgets.QLineEdit(self.loginPage)
        self.editPassword.setStyleSheet("")
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword.setObjectName("editPassword")
        self.gridLayout.addWidget(self.editPassword, 3, 1, 1, 1)
        self.btnShowPass = QtWidgets.QToolButton(self.loginPage)
        self.btnShowPass.setIcon(QtGui.QIcon("./Icon/icons8-eye-48.png"))
        self.btnShowPass.setIconSize(QtCore.QSize(16, 16))
        self.btnShowPass.setObjectName("btnShowPass")
        self.gridLayout.addWidget(self.btnShowPass, 3, 2, 1, 1)
        self.editUsername = QtWidgets.QLineEdit(self.loginPage)
        self.editUsername.setStyleSheet("")
        self.editUsername.setObjectName("editUsername")
        self.gridLayout.addWidget(self.editUsername, 2, 1, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLogin = QtWidgets.QPushButton(self.loginPage)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout.addWidget(self.btnLogin)
        self.btnSignUp = QtWidgets.QPushButton(self.loginPage)
        self.btnSignUp.setObjectName("btnSignUp")
        self.horizontalLayout.addWidget(self.btnSignUp)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.loginPage)
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.homePage)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnAddBill = QtWidgets.QPushButton(self.homePage)
        self.btnAddBill.setObjectName("btnAddBill")
        self.horizontalLayout_3.addWidget(self.btnAddBill)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btnFindItem = QtWidgets.QPushButton(self.homePage)
        self.btnFindItem.setObjectName("btnFindItem")
        self.horizontalLayout_3.addWidget(self.btnFindItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.treeBill = QtWidgets.QTreeWidget(self.homePage)
        self.treeBill.setObjectName("treeBill")
        self.treeBill.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.treeBill.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.treeBill.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.treeBill.headerItem().setTextAlignment(3, QtCore.Qt.AlignCenter)
        self.treeBill.headerItem().setTextAlignment(4, QtCore.Qt.AlignCenter)
        self.treeBill.headerItem().setTextAlignment(5, QtCore.Qt.AlignCenter)
        self.treeBill.headerItem().setTextAlignment(6, QtCore.Qt.AlignCenter)
        # self.treeBill.headerItem().setTextAlignment(7, QtCore.Qt.AlignCenter)
        self.treeBill.headerItem().setTextAlignment(7, QtCore.Qt.AlignCenter)
        self.treeBill.setStyleSheet("""
        QTreeWidget::item:!selected{
            border-bottom: 1px solid black;
            border-left: 1px solid black;
            border-top: 1px solid black;
            padding: 5px;
        }
        QTreeWidget::item:selected{}
        """)
        self.verticalLayout_2.addWidget(self.treeBill)
        self.stackedWidget.addWidget(self.homePage)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 750, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuStatistic = QtWidgets.QMenu(self.menuFile)
        self.menuStatistic.setObjectName("menuStatistic")
        self.menuExport_Excel_File = QtWidgets.QMenu(self.menuFile)
        self.menuExport_Excel_File.setObjectName("menuExport_Excel_File")
        self.menuUser = QtWidgets.QMenu(self.menuBar)
        self.menuUser.setObjectName("menuUser")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionShow_User_Info = QtWidgets.QAction(MainWindow)
        self.actionShow_User_Info.setObjectName("actionShow_User_Info")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionItem = QtWidgets.QAction(MainWindow)
        self.actionItem.setObjectName("actionItem")
        self.actionType_Item = QtWidgets.QAction(MainWindow)
        self.actionType_Item.setObjectName("actionType_Item")
        self.actionBill = QtWidgets.QAction(MainWindow)
        self.actionBill.setObjectName("actionBill")
        self.actionItem_Table = QtWidgets.QAction(MainWindow)
        self.actionItem_Table.setObjectName("actionItem_Table")
        self.actionBill_Table = QtWidgets.QAction(MainWindow)
        self.actionBill_Table.setObjectName("actionBill_Table")
        self.actionItem_File = QtWidgets.QAction(MainWindow)
        self.actionItem_File.setObjectName("actionItem_File")
        self.actionBill_File = QtWidgets.QAction(MainWindow)
        self.actionBill_File.setObjectName("actionBill_File")
        self.actionUser_List = QtWidgets.QAction(MainWindow)
        self.actionUser_List.setObjectName("actionUser_List")
        self.menuNew.addAction(self.actionItem)
        self.menuNew.addAction(self.actionType_Item)
        self.menuNew.addAction(self.actionBill)
        self.menuStatistic.addAction(self.actionItem_Table)
        self.menuStatistic.addAction(self.actionBill_Table)
        self.menuExport_Excel_File.addAction(self.actionItem_File)
        self.menuExport_Excel_File.addAction(self.actionBill_File)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.menuStatistic.menuAction())
        self.menuFile.addAction(self.menuExport_Excel_File.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuUser.addAction(self.actionUser_List)
        self.menuUser.addAction(self.actionShow_User_Info)
        self.menuUser.addSeparator()
        self.menuUser.addAction(self.actionLogin)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuUser.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.editUsername, self.editPassword)
        MainWindow.setTabOrder(self.editPassword, self.btnShowPass)
        MainWindow.setTabOrder(self.btnShowPass, self.btnLogin)
        MainWindow.setTabOrder(self.btnLogin, self.btnSignUp)
        MainWindow.setTabOrder(self.btnSignUp, self.btnFindItem)
        MainWindow.setTabOrder(self.btnFindItem, self.treeBill)
        MainWindow.setTabOrder(self.treeBill, self.btnAddBill)

        self.linkWidget()
        self.linkMenu()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Managing Selling Application"))
        self.lblUsername.setText(_translate("MainWindow", "User name:"))
        self.lblPassword.setText(_translate("MainWindow", "Password:"))
        self.btnShowPass.setText(_translate("MainWindow", "..."))
        self.btnLogin.setText(_translate("MainWindow", "Đăng nhập"))
        self.btnSignUp.setText(_translate("MainWindow", "Đăng kí"))
        self.btnAddBill.setText(_translate("MainWindow", "Thêm Đơn hàng"))
        self.btnFindItem.setText(_translate("MainWindow", "Tìm kiếm"))
        self.treeBill.headerItem().setText(0, _translate("MainWindow", "Thời gian tạo"))
        self.treeBill.headerItem().setText(1, _translate("MainWindow", "Mặt hàng"))
        self.treeBill.headerItem().setText(2, _translate("MainWindow", "Loại hàng"))
        self.treeBill.headerItem().setText(3, _translate("MainWindow", "ID"))
        self.treeBill.headerItem().setText(4, _translate("MainWindow", "Số lượng xuất"))
        self.treeBill.headerItem().setText(5, _translate("MainWindow", "Phương thức bán"))
        self.treeBill.headerItem().setText(6, _translate("MainWindow", "Thành giá"))
        # self.treeBill.headerItem().setText(7, _translate("MainWindow", "Người tạo"))
        self.treeBill.headerItem().setText(7, _translate("MainWindow", "Ghi chú"))
        self.menuFile.setTitle(_translate("MainWindow", "Tệp"))
        self.menuNew.setTitle(_translate("MainWindow", "Thêm mới ..."))
        self.menuStatistic.setTitle(_translate("MainWindow", "Thống kê"))
        self.menuExport_Excel_File.setTitle(_translate("MainWindow", "Xuất file Excel"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        self.actionExit.setText(_translate("MainWindow", "Thoát"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionShow_User_Info.setText(_translate("MainWindow", "Xem thông tin User"))
        self.actionLogin.setText(_translate("MainWindow", "Đăng xuất"))
        self.actionLogin.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))
        self.actionItem.setText(_translate("MainWindow", "Mặt hàng"))
        self.actionItem.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionType_Item.setText(_translate("MainWindow", "Loại hàng"))
        self.actionType_Item.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.actionBill.setText(_translate("MainWindow", "Đơn hàng"))
        self.actionBill.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.actionItem_Table.setText(_translate("MainWindow", "Bảng mặt hàng"))
        self.actionItem_Table.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionBill_Table.setText(_translate("MainWindow", "Bảng đơn hàng"))
        self.actionBill_Table.setShortcut(_translate("MainWindow", "Ctrl+Shift+V"))
        self.actionItem_File.setText(_translate("MainWindow", "File Mặt hàng"))
        self.actionBill_File.setText(_translate("MainWindow", "File Đơn hàng"))
        self.actionUser_List.setText(_translate("MainWindow", "Danh sách User"))
        self.actionUser_List.setShortcut(_translate("MainWindow", "Ctrl+Shift+U"))

    def linkWidget(self):
        # Link Button Widget
        self.btnLogin.clicked.connect(self.onLoginClick)
        self.btnFindItem.clicked.connect(self.onFindItemClick)
        self.btnShowPass.clicked.connect(self.onShowPassClick)
        self.btnSignUp.clicked.connect(self.onSignUpClick)
        self.btnAddBill.clicked.connect(self.onMenuAddBill)

    def linkMenu(self):
        self.actionExit.triggered.connect(self.onMenuExit)
        self.actionLogin.triggered.connect(self.onMenuLogOut)
        self.actionItem.triggered.connect(self.onMenuNewItem)
        self.actionType_Item.triggered.connect(self.onMenuNewType)
        self.actionBill.triggered.connect(self.onMenuAddBill)
        self.actionBill_Table.triggered.connect(self.onMenuStatisticBill)
        self.actionItem_Table.triggered.connect(self.onMenuStatisticItem)
        self.actionUser_List.triggered.connect(self.onMenuStatisticUser)
        self.actionShow_User_Info.triggered.connect(self.onMenuShowUserInfo)
        self.actionItem_File.triggered.connect(self.onMenuExportItem)
        self.actionBill_File.triggered.connect(self.onMenuExportBill)

    def onLoginClick(self):
        if len(self.editUsername.text()) != 0 and " " not in list(self.editUsername.text()):
            if self.checkAccount() == True:
                self.menuBar.setVisible(True)
                
                if self.editUsername.text() != "root":
                    self.actionUser_List.setVisible(False)
                else:
                    self.actionUser_List.setVisible(True)

                self.stackedWidget.setCurrentIndex(1)
                self.loadDataForHomePage()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Username hoặc Password không đúng !!")
                msg.setInformativeText("Xin hãy thử lại !!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec()
                return
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Username không thể để trống hoặc có chứa khoảng trắng!!")
            msg.setInformativeText("Xin hãy nhập Username hoặc xóa đi khoảng trắng !!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return

    def onFindItemClick(self):
        self.onMenuStatisticItem()
        
    def onShowPassClick(self):
        if self.isShowPass:
            self.editPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.isShowPass = False
        else:
            self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
            self.isShowPass = True

    def onSignUpClick(self):
        self.dialogSignUp = Ui_DialogSignUp()
        self.dialogSignUp.exec()

        if self.dialogSignUp.isAccept == 1:
            user = self.dialogSignUp.user
            self.editUsername.setText(user.username)
            self.editPassword.setText(user.passWord)
            self.btnLogin.setFocus()

        # Get return value of Dialog Sign Up
        while self.dialogSignUp.isAccept == -1:
            self.dialogSignUp.isAccept = 0
            self.dialogSignUp.exec()
            if self.dialogSignUp.isAccept  == 1:
                user = self.dialogSignUp.user
                self.editUsername.setText(user.username)
                self.editPassword.setText(user.passWord)
                self.btnLogin.setFocus()

    def onMenuAddBill(self):
        self.dialogAddBill = Ui_DialogAddBill(userCreate= self.editUsername.text())
        self.dialogAddBill.exec()

        if self.dialogAddBill.isAccept == 1:
            bill = self.dialogAddBill.bill
            self.addItemIntoTree(bill)

        while self.dialogAddBill.isAccept == -1:
            self.dialogAddBill.isAccept = 0
            self.dialogAddBill.exec()
    
    def onMenuNewItem(self):
        self.dialogNewItem = Ui_DialogNewItem()
        self.dialogNewItem.exec()

        # Get Value of Dialog New Item
        while self.dialogNewItem.isAccept == -1:
            self.dialogNewItem.isAccept = 0
            self.dialogNewItem.exec()

    def onMenuNewType(self):
        self.dialogNewType = Ui_DialogNewType()
        self.dialogNewType.exec()

        # Get Value of Dialog New Type
        while self.dialogNewType.isAccept == -1:
            self.dialogNewType.isAccept = 0
            self.dialogNewType.exec()

    def onMenuStatisticItem(self):
        self.dialogItemStatistic = Ui_DialogItemStatistic()
        self.dialogItemStatistic.show()

    def onMenuStatisticBill(self):
        self.dialogBillStatistic = Ui_DialogBillStatistic()
        self.dialogBillStatistic.show()

    def onMenuExit(self):
        self.MainWindow.onDestroy()

    def onMenuLogOut(self):
        self.stackedWidget.setCurrentIndex(0)
        self.menuBar.setVisible(False)
        self.treeBill.clear()

    def onMenuStatisticUser(self):
        self.dialogUserStatistic = Ui_DialogUserStatistic()
        self.dialogUserStatistic.show()

    def onMenuShowUserInfo(self):
        self.dialogShowUserInfo = Ui_DialogUserInfo(username=self.editUsername.text())
        self.dialogShowUserInfo.show()

    def onMenuExportItem(self):
        pathFile,_ = QtWidgets.QFileDialog.getSaveFileName(self.MainWindow,"Save file",".",
            "Excel files (*.xlsx)")
        exportFileItem(pathFile)

    def onMenuExportBill(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Tính năng đang thi công !!")
        msg.setInformativeText("Vui lòng thử lại sau")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        return

    def checkAccount(self):        
        username = self.editUsername.text()
        passWord = self.editPassword.text()

        data = Database()
        user = data.getUserInfo(username)
        if user.username == username and user.passWord == passWord:
            data.closeDatabase()
            return True
        else:
            data.closeDatabase()
            return False
        
    def addItemIntoTree(self,bill):
        listAttribute = [bill.createdTime,bill.nameItem,bill.nameType,bill.idBill,
                        str(bill.amount), bill.saleType, str(bill.price),bill.notice]
        listName = self.getListParentNameInTree()
        parent = QtWidgets.QTreeWidgetItem([bill.createdDate])
        if bill.createdDate not in listName:
            self.treeBill.addTopLevelItem(parent)
            QtWidgets.QTreeWidgetItem(parent,listAttribute)
            parent.setExpanded(True)
        else:
            index = listName.index(bill.createdDate)
            parent = self.treeBill.topLevelItem(index)
            QtWidgets.QTreeWidgetItem(parent,listAttribute)
            parent.setExpanded(True)

    def getListParentNameInTree(self):
        listParentName = []
        numberParent = self.treeBill.topLevelItemCount()
        for index in range(0,numberParent):
            parent = self.treeBill.topLevelItem(index)
            parentName = parent.text(0)
            listParentName.append(parentName)

        return listParentName

    def loadDataForHomePage(self):
        data = Database()
        date = datetime.datetime.now().date().strftime("%d/%m/%Y")
        listBill = data.getListBillAtDate(str(date))
        for bill in listBill:
            self.addItemIntoTree(bill)
        data.closeDatabase()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
