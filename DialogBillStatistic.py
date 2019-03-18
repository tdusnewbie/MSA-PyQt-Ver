# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/dialogbillstatistic2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import os

from PyQt5 import QtCore, QtGui, QtWidgets

from Model import Database, Bill


class Ui_DialogBillStatistic(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.listHistories = []
        self.completer = None
        self.setupUi(self)
        
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))
        
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0,0,screen.width(), screen.height())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblFilter = QtWidgets.QLabel(self.centralwidget)
        self.lblFilter.setObjectName("lblFilter")
        self.horizontalLayout.addWidget(self.lblFilter)
        self.comboFilter = QtWidgets.QComboBox(self.centralwidget)
        self.comboFilter.setObjectName("comboFilter")
        self.horizontalLayout.addWidget(self.comboFilter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblFind = QtWidgets.QLabel(self.centralwidget)
        self.lblFind.setObjectName("lblFind")
        self.horizontalLayout.addWidget(self.lblFind)
        self.editFind = QtWidgets.QLineEdit(self.centralwidget)
        self.editFind.setObjectName("editFind")
        self.horizontalLayout.addWidget(self.editFind)
        self.btnFind = QtWidgets.QPushButton(self.centralwidget)
        self.btnFind.setObjectName("btnFind")
        self.horizontalLayout.addWidget(self.btnFind)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeBill = QtWidgets.QTreeWidget(self.centralwidget)
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
        self.verticalLayout.addWidget(self.treeBill)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setupWidget()
        self.linkWidget()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thống kê Đơn hàng"))
        self.lblFilter.setText(_translate("MainWindow", "Tìm kiếm theo:"))
        self.lblFind.setText(_translate("MainWindow", "Nhập từ khóa: "))
        self.btnFind.setText(_translate("MainWindow", "Tìm kiếm"))
        self.treeBill.headerItem().setText(0, _translate("MainWindow", "Ngày tạo"))
        self.treeBill.headerItem().setText(1, _translate("MainWindow", "Mặt hàng"))
        self.treeBill.headerItem().setText(2, _translate("MainWindow", "Loại hàng"))
        self.treeBill.headerItem().setText(3, _translate("MainWindow", "ID"))
        self.treeBill.headerItem().setText(4, _translate("MainWindow", "Số lượng xuất"))
        self.treeBill.headerItem().setText(5, _translate("MainWindow", "Phương thức bán"))
        self.treeBill.headerItem().setText(6, _translate("MainWindow", "Thành giá"))
        # self.treeBill.headerItem().setText(7, _translate("MainWindow", "User Create"))
        self.treeBill.headerItem().setText(7, _translate("MainWindow", "Ghi chú"))

    def setupWidget(self):
        style = """
        QTreeWidget::item:!selected{
            border-bottom: 1px solid black;
            border-left: 1px solid black;
            border-top: 1px solid black;
            padding: 5px;
        }
        QTreeWidget::item:selected{}
        """
        self.treeBill.setStyleSheet(style)
        listAttribute = ["Item Name", "Type Name", "ID", 
                        "Amount", "Sale Type", "Price", 
                        "Created Date", "Created Time",
                        "Notice"]
        for attribute in listAttribute:
            self.comboFilter.addItem(attribute)

        data = Database()
        listBill = data.getAllListBill()
        for bill in listBill:
            self.addBillIntoTree(bill)
        data.closeDatabase()

        self.comboFilter.setCurrentIndex(0)
        
        self.listHistories = self.loadHistories()
        self.completer = QtWidgets.QCompleter(self.listHistories)
        self.editFind.setCompleter(self.completer)
  
    def linkWidget(self):
        self.btnFind.clicked.connect(self.onClickFindBill)
        self.comboFilter.currentIndexChanged.connect(self.onChangeFilter)
        self.editFind.returnPressed.connect(self.onClickFindBill)

    def onClickFindBill(self):
        newHis = self.editFind.text()
        if newHis not in self.listHistories and len(newHis) > 0:
            self.updateHistories(newHis)
        index = self.comboFilter.currentIndex()
        self.startFinding(index,newHis)

    def onChangeFilter(self, index):
        newHis = self.editFind.text()
        self.startFinding(index,newHis)

    def startFinding(self, index, newHis):
        data = Database()
        self.treeBill.clear()
        # Filter is Item name
        if index == 0:
            listResult = data.getListBillWithItemName(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        # Filter is Type name
        if index == 1:
            listResult = data.getListBillWithTypeName(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        # Filter is ID
        if index == 2:
            listResult = data.getListBillWithIDBill(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        # Filter is Amount
        if index == 3:
            listResult = data.getListBillWithAmount(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        # Filter is Sale Type
        if index == 4:
            listResult = data.getListBillWithSaleType(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        # Filter is Price
        if index == 5:
            listResult = data.getListBillWithPrice(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        # # Filter is Created User
        # if index == 6:
        #     listResult = data.getListBillWithUserCreate(newHis)
        #     for bill in listResult:
        #         self.addBillIntoTree(bill)
        # Filter is Created Date
        if index == 6:
            listResult = data.getListBillAtDate(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        # Filter is Created Time
        if index == 7:
            listResult = data.getListBillAtTime(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        # Filter is Notice
        if index == 8:
            listResult = data.getListBillWithNotice(newHis)
            for bill in listResult:
                self.addBillIntoTree(bill)
        data.closeDatabase()
    def addBillIntoTree(self, bill):
        listAttribute = [bill.createdTime,bill.nameItem,bill.nameType,
                        bill.idBill, str(bill.amount), bill.saleType, 
                        str(bill.price), bill.notice]
        
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

    def loadHistories(self):
        listHistory = []
        if os.path.isfile("Data/FindBillHistories.txt"):
            with open("Data/FindBillHistories.txt","r") as f:
                for line in f:
                    if line[-1] == '\n':
                        line = line[:-1]                   
                    listHistory.append(line)
        return listHistory

    def saveHistories(self):
        with open("Data/FindBillHistories.txt","w+") as f:
            for item in self.listHistories:
                f.write(str(item) + "\n")

    def updateHistories(self, newHis):
        if len(self.listHistories) >= 50:
            self.listHistories = self.listHistories[1:]
            self.listHistories.append(newHis)
        else:
            self.listHistories.append(newHis)
        
        self.completer = QtWidgets.QCompleter(self.listHistories)
        self.editFind.setCompleter(self.completer)
        
    def closeEvent(self, event):
        self.saveHistories()
        print("is close")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_DialogBillStatistic()
    MainWindow.show()
    sys.exit(app.exec_())
