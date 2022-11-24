import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class_home = uic.loadUiType("home.ui")[0]
form_class_dkuMenu = uic.loadUiType("dku_menu.ui")[0]

class WindowClass(QMainWindow, form_class_home):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dkuBtn.clicked.connect(self.onclick_dku)
        self.etaBtn.clicked.connect(self.onclick_eta)

    def onclick_dku(self):
        self.hide()
        self.second = DkuMenu()
        self.second.exec()
        self.show()

    def onclick_eta(self):
        print("에타 클릭함")

class DkuMenu(QDialog, QWidget, form_class_dkuMenu):
    def __init__(self):
        super(DkuMenu, self).__init__()
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()