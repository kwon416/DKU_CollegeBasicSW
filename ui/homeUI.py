import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("homeUI.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dkuBtn.clicked.connect(self.onclick_dku)
        self.etaBtn.clicked.connect(self.onclick_eta)

    def onclick_dku(self):
        print("단대 클릭함")

    def onclick_eta(self):
        print("에타 클릭함")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()