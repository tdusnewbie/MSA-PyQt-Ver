import datetime
import sys

from PyQt5 import QtWidgets, QtCore, QtGui

def addToTreeWidget(value):
    name = "Demo " + str(value)
    cost = int(value) * 1000
    listParent = getListParent()
    parent = QtWidgets.QTreeWidgetItem([str(date)])
    if str(date) not in listParent:
        tw.addTopLevelItem(parent)
        QtWidgets.QTreeWidgetItem(parent,[name,str(cost)])
    else:
        index = listParent.index(str(date))
        parent = tw.topLevelItem(index)
        QtWidgets.QTreeWidgetItem(parent,[name,str(cost)])

def getListParent():
    listParent = []
    numberParent = tw.topLevelItemCount()
    for index in range(0,numberParent):
        parent = tw.topLevelItem(index)
        parentName = parent.text(0)
        listParent.append(parentName)
        print(parentName)

    return listParent

date = datetime.datetime.now().date()
time = datetime.datetime.now().time()

print(time.strftime("%I:%M %p"))
print(date.strftime("%d/%m/%Y"))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)

tw = QtWidgets.QTreeWidget()
tw.setHeaderLabels(["Name","Cost($)"])
tw.setAlternatingRowColors(True)
for i in range(0,10):
    addToTreeWidget(i)

layout.addWidget(tw)
window.show()
sys.exit(app.exec_())