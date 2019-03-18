# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/dialogitemstatistic2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

import os
import sqlite3
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from Model import Database, Item, TypeItem

class Ui_DialogItemStatistic(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        
        self.listHistories = []
        self.completer = None
        self.listItem = []
        self.beforeItemChange = None
        self.beforeTypeChange = None
        self.isAddItem = False
        self.isAddType = False
        
        self.setupUi(self)
        
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0,0,screen.width(), screen.height())

    def setupUi(self, DialogItemStatistic):
        DialogItemStatistic.setObjectName("DialogItemStatistic")
        DialogItemStatistic.resize(865, 423)
        self.centralwidget = QtWidgets.QWidget(DialogItemStatistic)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableItem = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableItem.sizePolicy().hasHeightForWidth())
        self.tableItem.setSizePolicy(sizePolicy)
        self.tableItem.setStyleSheet("""
        QTableWidget::item:!selected{ 
            border: 1px solid black; 
        } 
        QTableWidget::item:selected{}
        """)
        self.tableItem.setObjectName("tableItem")
        self.tableItem.setColumnCount(2)
        self.tableItem.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableItem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableItem.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.tableItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddItem = QtWidgets.QToolButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddItem.sizePolicy().hasHeightForWidth())
        self.btnAddItem.setSizePolicy(sizePolicy)
        self.btnAddItem.setObjectName("btnAddItem")
        self.verticalLayout.addWidget(self.btnAddItem)
        self.btnDeleteItem = QtWidgets.QToolButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteItem.sizePolicy().hasHeightForWidth())
        self.btnDeleteItem.setSizePolicy(sizePolicy)
        self.btnDeleteItem.setObjectName("btnDeleteItem")
        self.verticalLayout.addWidget(self.btnDeleteItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableType = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableType.setStyleSheet("""
        QTableWidget::item:!selected{ 
            border: 1px solid black; 
        } 
        QTableWidget::item:selected{}
        """)
        self.tableType.setObjectName("tableType")
        self.tableType.setColumnCount(9)
        self.tableType.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableType.setHorizontalHeaderItem(8, item)
        self.horizontalLayout_3.addWidget(self.tableType)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnAddType = QtWidgets.QToolButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddType.sizePolicy().hasHeightForWidth())
        self.btnAddType.setSizePolicy(sizePolicy)
        self.btnAddType.setObjectName("btnAddType")
        self.verticalLayout_2.addWidget(self.btnAddType)
        self.btnDeleteType = QtWidgets.QToolButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteType.sizePolicy().hasHeightForWidth())
        self.btnDeleteType.setSizePolicy(sizePolicy)
        self.btnDeleteType.setObjectName("btnDeleteType")
        self.verticalLayout_2.addWidget(self.btnDeleteType)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.imgAvatar = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgAvatar.sizePolicy().hasHeightForWidth())
        self.imgAvatar.setSizePolicy(sizePolicy)
        self.imgAvatar.setFrameShape(QtWidgets.QFrame.Box)
        self.imgAvatar.setObjectName("imgAvatar")
        self.verticalLayout_4.addWidget(self.imgAvatar)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        DialogItemStatistic.setCentralWidget(self.centralwidget)

        self.retranslateUi(DialogItemStatistic)
        QtCore.QMetaObject.connectSlotsByName(DialogItemStatistic)

        self.setupWidget()
        self.linkWidget()

    def retranslateUi(self, DialogItemStatistic):
        _translate = QtCore.QCoreApplication.translate
        DialogItemStatistic.setWindowTitle(_translate("DialogItemStatistic", "Thống kê Mặt hàng"))
        self.lblFilter.setText(_translate("DialogItemStatistic", "Tìm kiếm với:"))
        self.lblFind.setText(_translate("DialogItemStatistic", "Nhập từ khóa:"))
        self.btnFind.setText(_translate("DialogItemStatistic", "Tìm kiếm"))
        self.groupBox.setTitle(_translate("DialogItemStatistic", "Danh sách mặt hàng:"))
        item = self.tableItem.horizontalHeaderItem(0)
        item.setText(_translate("DialogItemStatistic", "Mặt hàng"))
        item = self.tableItem.horizontalHeaderItem(1)
        item.setText(_translate("DialogItemStatistic", "ID mặt hàng"))
        self.btnAddItem.setText(_translate("DialogItemStatistic", "+"))
        self.btnDeleteItem.setText(_translate("DialogItemStatistic", "-"))
        self.groupBox_2.setTitle(_translate("DialogItemStatistic", "Danh sách loại hàng:"))
        item = self.tableType.horizontalHeaderItem(0)
        item.setText(_translate("DialogItemStatistic", "Loại hàng"))
        item = self.tableType.horizontalHeaderItem(1)
        item.setText(_translate("DialogItemStatistic", "ID loại hàng"))
        item = self.tableType.horizontalHeaderItem(2)
        item.setText(_translate("DialogItemStatistic", "Thuộc mặt hàng"))
        item = self.tableType.horizontalHeaderItem(3)
        item.setText(_translate("DialogItemStatistic", "Số lượng tồn"))
        item = self.tableType.horizontalHeaderItem(4)
        item.setText(_translate("DialogItemStatistic", "Giá lẻ"))
        item = self.tableType.horizontalHeaderItem(5)
        item.setText(_translate("DialogItemStatistic", "Giá sỉ"))
        item = self.tableType.horizontalHeaderItem(6)
        item.setText(_translate("DialogItemStatistic", "Giá vốn"))
        item = self.tableType.horizontalHeaderItem(7)
        item.setText(_translate("DialogItemStatistic", "Ghi chú"))
        item = self.tableType.horizontalHeaderItem(8)
        item.setText(_translate("DialogItemStatistic", "Hình ảnh"))
        self.btnAddType.setText(_translate("DialogItemStatistic", "+"))
        self.btnDeleteType.setText(_translate("DialogItemStatistic", "-"))
        self.groupBox_3.setTitle(_translate("DialogItemStatistic", "Hình ảnh:"))
        self.imgAvatar.setText(_translate("DialogItemStatistic", "No Image"))

    def setupWidget(self):
        listAttribute = ["Tên mặt hàng", "ID mặt hàng", "Tên loại hàng", "ID Loại hàng",
                        "Số lượng tồn", "Giá lẻ", "Giá sỉ", "Giá vốn",
                        "Ghi chú", "Hình ảnh"]
        for attribute in listAttribute:
            self.comboFilter.addItem(attribute)
        self.comboFilter.setCurrentIndex(0)
        data = Database()

        self.listItem = data.getListItemWithoutType()
        for item in self.listItem:
            self.addItemIntoTable(item)

        data.closeDatabase()

        self.tableItem.setCurrentCell(0,0)
        self.onCurrentItemCellChange(0,0,None,None)

        self.listHistories = self.loadHistories()
        self.completer = QtWidgets.QCompleter(self.listHistories)
        self.editFind.setCompleter(self.completer)

    def linkWidget(self):
        self.tableItem.currentCellChanged.connect(self.onCurrentItemCellChange)
        self.tableType.currentCellChanged.connect(self.onCurrentTypeCellChange)
        self.tableItem.cellActivated.connect(self.onItemCellActivate)
        self.tableType.cellActivated.connect(self.onTypeCellActivate)
        self.tableItem.cellChanged.connect(self.onItemCellContentChange)
        self.tableType.cellChanged.connect(self.onTypeCellContentChange)
        self.btnAddItem.clicked.connect(self.onAddItem)
        self.btnDeleteItem.clicked.connect(self.onDeleteItem)
        self.btnAddType.clicked.connect(self.onAddType)
        self.btnDeleteType.clicked.connect(self.onDeleteType)
        self.btnFind.clicked.connect(self.onFindItem)
        self.editFind.returnPressed.connect(self.onFindItem)
        self.comboFilter.currentIndexChanged.connect(self.onComboFilterChange)

    def onCurrentItemCellChange(self, row, col, prerow, precol):
        if row != prerow:
            self.tableType.clearSelection()
            self.tableType.clearContents()
            self.tableType.setRowCount(0)

            if self.tableItem.item(row,1) == None:
                return

            idItem = self.tableItem.item(row,1).text()
            data = Database()
            listType = data.getListTypeHasIDParent(idItem)
            for typeItem in listType:
                self.addTypeIntoTable(typeItem)

        if row == 1:
            self.beforeItemChange = self.tableItem.item(row,col).text()

        # self.tableType.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    
    def onCurrentTypeCellChange(self, row, col, prerow, precol):
        if self.tableType.item(row,8) == None:
            return
        if row == 1:
            self.beforeTypeChange = self.tableType.item(row,col).text()

        pathImage = self.tableType.item(row,8).text()
        print(pathImage)
        self.setImage(pathImage)

    def onItemCellActivate(self, row, col):
        cell = self.tableItem.item(row, col)
        print("In Item Table at row: %d and col: %d has content is: %s" % (row, col, cell.text()))

    def onTypeCellActivate(self, row, col):
        cell = self.tableType.item(row, col)
        print("In Type Table at (r-c): %d - %d has content is: %s" % (row, col, cell.text()))

    def onItemCellContentChange(self, row, col):
        if self.isAddItem:
            return
        
        cell = self.tableItem.item(row, col)
        print(cell.text())
        data = Database()
        if col == 0:
            data.updateItemName(self.tableItem.item(row, 1).text(),cell.text())
        elif col == 1:
            try:
                data.updateItemID(self.beforeItemChange,cell.text())
            except sqlite3.IntegrityError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("ID này đã tồn tại !!")
                msg.setInformativeText("Xin hãy chọn một ID khác và thử lại !!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec()
                data.closeDatabase()
                return
            else:
                data.updateAllTypeHasIDParent(cell.text())
                self.onCurrentItemCellChange(row,col,None,None)
        data.closeDatabase()

    def onTypeCellContentChange(self, row, col):
        if self.isAddType:
            return
        
        cell = self.tableType.item(row, col)
        data = Database()
        if col == 0:
            data.updateTypeName(self.tableType.item(row, 1).text(),cell.text())
        elif col == 1:
            try:
                data.updateItemID(self.beforeItemChange,cell.text())
            except sqlite3.IntegrityError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("ID này đã tồn tại !!")
                msg.setInformativeText("Xin hãy chọn một ID khác và thử lại !!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec()
                data.closeDatabase()
                return

        elif col == 3:
            try:
                test = int(cell.text())
            except ValueError:
                Msgbox = QtWidgets.QMessageBox()
                Msgbox.setText("Error, Giá trị này phải là số!")
                Msgbox.exec()
                cell.setText(str(0))
                return

            data.updateTypeAmount(self.tableType.item(row, 1).text(),cell.text())

        elif col == 4:
            try:
                test = float(cell.text())
            except ValueError:
                Msgbox = QtWidgets.QMessageBox()
                Msgbox.setText("Error, Giá trị này phải là số!")
                Msgbox.exec()
                cell.setText(str(0))                
                return

            data.updateTypeUnitPrice(self.tableType.item(row, 1).text(),cell.text())

        elif col == 5:
            try:
                test = float(cell.text())
            except ValueError:
                Msgbox = QtWidgets.QMessageBox()
                Msgbox.setText("Error, Giá trị này phải là số!")
                Msgbox.exec()
                cell.setText(str(0))
                return
                      
            data.updateTypeWholePrice(self.tableType.item(row, 1).text(),cell.text())

        elif col == 6:
            try:
                test = float(cell.text())
            except ValueError:
                Msgbox = QtWidgets.QMessageBox()
                Msgbox.setText("Error, Giá trị này phải là số!")
                Msgbox.exec()
                cell.setText(str(0))
                return

            data.updateTypeOriginPrice(self.tableType.item(row, 1).text(),cell.text())

        elif col == 7:
            data.updateTypeNotice(self.tableType.item(row, 1).text(),cell.text())

        elif col == 8:
            data.updateTypeImagePath(self.tableType.item(row, 1).text(),cell.text())


        data.closeDatabase()

    def onAddItem(self):
        date = datetime.datetime.now()
        newId = "IT-" + date.strftime("%d%m%Y%H%M%S")
        newItem = Item(idItem = newId)

        data = Database()
        while True:
            try:
                data.insertItem(newItem)
            except sqlite3.IntegrityError:
                date = date + datetime.timedelta(0,1)
                newId = "IT-" + date.strftime("%d%m%Y%H%M%S")
                newItem.idItem = newId

            else:
                break
        data.closeDatabase()
        self.addItemIntoTable(newItem)

    def onDeleteItem(self):
        currentRow = self.tableItem.currentRow()
        currentCol = self.tableItem.currentColumn()
        numberRow = self.tableItem.rowCount()
        if currentRow >= 0:
            idDel = self.tableItem.item(currentRow,1).text()
            data = Database()
            data.deleteItem(idDel)
            data.closeDatabase()
            self.tableItem.removeRow(currentRow)
            if currentRow == numberRow -1:
                self.tableItem.setCurrentCell(currentRow-1,currentCol)
            else:
                self.tableItem.setCurrentCell(currentRow,currentCol)
            

        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Bạn muốn xóa mặt hàng nào !!")
            msg.setInformativeText("Xin hãy chọn một mặt hàng trước khi xóa !!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return

    def onAddType(self):
        if self.comboFilter.currentIndex() > 1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Bạn hiện đang ở chế độ tìm kiếm !!")
            msg.setInformativeText("Thoát khỏi chế độ tìm kiếm để thực hiện chức năng này !!")
            msg.setDetailedText("Chọn tìm kiếm với 'Tên mặt hàng' hoặc 'ID mặt hàng' và chọn mặt hàng muốn thêm để thoát khỏi chế độ tìm kiếm!!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return

        row = self.tableItem.currentRow()
        if row >= 0 :
            idParent = self.tableItem.item(row,1).text()
            date = datetime.datetime.now()
            newId = "TY-" + date.strftime("%d%m%Y%H%M%S")
            newType = TypeItem(idType= newId, idParent = idParent, amount = 0,
                            unitPrice = 0, wholePrice = 0, originPrice = 0)

            data = Database()
            while True:
                try:
                    data.insertTypeItem(newType)
                except sqlite3.IntegrityError:
                    date = date + datetime.timedelta(0,1)
                    newId = "TY-" + date.strftime("%d%m%Y%H%M%S")
                    newType.idType = newId
                else:
                    break
            data.closeDatabase()
            self.addTypeIntoTable(newType)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Bạn muốn thực hiện điều này trong mặt hàng nào !!")
            msg.setInformativeText("Xin hãy chọn một mặt hàng trước khi thực hiện !!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return

    def onDeleteType(self):
        currentRow = self.tableType.currentRow()
        currentCol = self.tableType.currentColumn()
        numberRow = self.tableType.rowCount()
        if currentRow >= 0:
            idDel = self.tableType.item(currentRow,1).text()
            data = Database()
            data.deleteTypeItem(idDel)
            data.closeDatabase()
            self.tableType.removeRow(currentRow)
            if currentRow == numberRow -1:
                self.tableType.setCurrentCell(currentRow-1,currentCol)
            else:
                self.tableType.setCurrentCell(currentRow,currentCol)
            
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Bạn muốn xóa loại hàng nào !!")
            msg.setInformativeText("Xin hãy chọn một loại hàng trước khi xóa !!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return

    def onFindItem(self):
        newHis = self.editFind.text()
        if newHis not in self.listHistories and len(newHis) > 0:
            self.updateHistories(newHis)
        index = self.comboFilter.currentIndex()
        self.startFinding(index,newHis)

    def onComboFilterChange(self, index):            
        findingContent = self.editFind.text()
        self.startFinding(index, findingContent)

    ######## Support Function #######
    def addItemIntoTable(self,item):
        self.isAddItem = True
        rowPos = self.tableItem.rowCount()
        self.tableItem.insertRow(rowPos)
        self.tableItem.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(item.name))
        self.tableItem.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(item.idItem))
        self.isAddItem = False

    def addTypeIntoTable(self,typeItem):
        self.isAddType = True
        rowPos = self.tableType.rowCount()
        self.tableType.insertRow(rowPos)
        self.tableType.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(typeItem.name))
        self.tableType.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(typeItem.idType))
        self.tableType.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(typeItem.idParent))
        self.tableType.item(rowPos,2).setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableType.setItem(rowPos, 3, QtWidgets.QTableWidgetItem(str(typeItem.amount)))
        self.tableType.setItem(rowPos, 4, QtWidgets.QTableWidgetItem(str(typeItem.unitPrice)))
        self.tableType.setItem(rowPos, 5, QtWidgets.QTableWidgetItem(str(typeItem.wholePrice)))
        self.tableType.setItem(rowPos, 6, QtWidgets.QTableWidgetItem(str(typeItem.originPrice)))
        self.tableType.setItem(rowPos, 7, QtWidgets.QTableWidgetItem(typeItem.notice))
        self.tableType.setItem(rowPos, 8, QtWidgets.QTableWidgetItem(typeItem.imagePath))
        self.isAddType = False
        
    def setImage(self, pathImage):
        image = QtGui.QPixmap(pathImage).scaled(200,150)
        self.imgAvatar.setScaledContents(True)
        self.imgAvatar.setPixmap(image)

    def loadHistories(self):
        listHistory = []
        if os.path.isfile("Data/FindItemHistories.txt"):
            with open("Data/FindItemHistories.txt","r") as f:
                for line in f:
                    if line[-1] == '\n':
                        line = line[:-1]                   
                    listHistory.append(line)
        return listHistory

    def saveHistories(self):
        with open("Data/FindItemHistories.txt","w+") as f:
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
    
    def startFinding(self,index, findingContent):
        data = Database()
        self.tableItem.clearContents()
        self.tableItem.setRowCount(0)
        self.tableType.clearContents()
        self.tableType.setRowCount(0)

        listResult = []
        # Filter is Item name
        if index == 0:
            listResult = data.getListItemWithName(findingContent)
            for item in listResult:
                self.addItemIntoTable(item)

        # Filter is Item ID
        if index == 1:
            listResult = data.getListItemWithID(findingContent)
            for item in listResult:
                self.addItemIntoTable(item)

        # Filter is Type Name
        if index == 2:
            listResult = data.getListTypeWithName(findingContent)
            for typeItem in listResult:
                self.addTypeIntoTable(typeItem)

        # Filter is ID
        if index == 3:
            listResult = data.getListTypeWithID(findingContent)
            for typeItem in listResult:
                self.addTypeIntoTable(typeItem)

        # Filter is Amount
        if index == 4:
            listResult = data.getListTypeWithAmount(findingContent)
            for typeItem in listResult:
                self.addTypeIntoTable(typeItem)

        # Filter is Unit Price
        if index == 5:
            listResult = data.getListTypeWithUnitPrice(findingContent)
            for typeItem in listResult:
                self.addTypeIntoTable(typeItem)

        # Filter is WholePrice
        if index == 6:
            listResult = data.getListTypeWithWholePrice(findingContent)
            for typeItem in listResult:
                self.addTypeIntoTable(typeItem)

        # Filter is Origin Price
        if index == 7:
            listResult = data.getListTypeWithOriginPrice(findingContent)
            for typeItem in listResult:
                self.addTypeIntoTable(typeItem)

        # Filter is Notice
        if index == 8:
            listResult = data.getListTypeWithNotice(findingContent)
            for typeItem in listResult:
                self.addTypeIntoTable(typeItem)

        # Filter is Image Path
        if index == 9:
            listResult = data.getListTypeWithImagePath(findingContent)
            for typeItem in listResult:
                self.addTypeIntoTable(typeItem)

        data.closeDatabase()

    def closeEvent(self, event):
        self.saveHistories()
        print("is close")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogItemStatistic = Ui_DialogItemStatistic()
    DialogItemStatistic.show()
    sys.exit(app.exec_())
