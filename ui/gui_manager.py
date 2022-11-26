import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class HomeUI(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("home.ui", self)
        self.newsBtn.clicked.connect(self.onclick_newsBtn)
        self.todayBtn.clicked.connect(self.onclick_todayBtn)
        self.noticeBtn.clicked.connect(self.onclick_noticeBtn)
    def onclick_newsBtn(self):
        widget.setCurrentWidget(UI.TEST)
    def onclick_todayBtn(self):
        pass
    def onclick_noticeBtn(self):
        pass
class TestUI(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)
        self.testBtn.clicked.connect(self.onclick_testBtn)

    def onclick_testBtn(self):
        widget.setCurrentWidget(UI.HOME)

class UI:
    HOME : HomeUI
    TEST : TestUI
    @staticmethod
    def init():
        UI.HOME = HomeUI()
        UI.TEST = TestUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    UI.init()

    widget = QStackedWidget()
    widget.addWidget(UI.HOME)
    widget.addWidget(UI.TEST)

    widget.setFixedSize(464, 284)

    widget.show()

    app.exec_()
