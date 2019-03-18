import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from MainWindow import Ui_MainWindow

class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI = Ui_MainWindow()
        self.setupUI()
        self.setWindowIcon(QtGui.QIcon("Icon\icon_app.png"))
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0,0,screen.width(), screen.height())


    def setupUI(self):
        self.UI.setupUi(self)
        self.UI.editUsername.setFocus()
        self.UI.menuBar.setVisible(False)
        
    def onDestroy(self):
        self.destroy()
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Application()
    w.show()
    
    sys.exit(app.exec_())
