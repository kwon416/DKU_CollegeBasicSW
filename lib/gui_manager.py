import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import main as crawl
import urllib.request

UI_DIR = "../ui/"

class HomeUI(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_DIR + "home.ui", self)
        self.newsBtn.clicked.connect(self.onclick_newsBtn)
        self.todayBtn.clicked.connect(self.onclick_todayBtn)
        self.noticeBtn.clicked.connect(self.onclick_noticeBtn)
    def onclick_newsBtn(self):
        widget.setCurrentWidget(UI.NEWS)
    def onclick_todayBtn(self):
        pass
    def onclick_noticeBtn(self):
        pass

class NewsUI(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_DIR + "news.ui", self)
        self.backBtn.clicked.connect(self.onclick_backBtn)
        data = crawl.CrawlingNews(1)
        for i in range(10):
            url = data.getImgUrl()[i]
            self.table.setItem(i, 0, QTableWidgetItem(url))
            imgData = urllib.request.urlopen(url).read()

            lbl = QLabel(self)
            pixmap = QPixmap()
            pixmap.loadFromData(imgData)
            lbl.setPixmap(pixmap)


        for i in range(10):
            self.table.setItem(i, 1, QTableWidgetItem(data.getTitle()[i]))
        for i in range(10):
            self.table.setItem(i, 2, QTableWidgetItem(data.getUrl()[i]))
        for i in range(10):
            self.table.setItem(i, 3, QTableWidgetItem(data.getViewCount()[i]))
        for i in range(10):
            self.table.setItem(i, 4, QTableWidgetItem(data.getDate()[i]))

    def onclick_backBtn(self):
        widget.setCurrentWidget(UI.HOME)

class UI:
    HOME : HomeUI
    NEWS : NewsUI
    @staticmethod
    def init():
        UI.HOME = HomeUI()
        UI.NEWS = NewsUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    UI.init()

    widget = QStackedWidget()
    widget.addWidget(UI.HOME)
    widget.addWidget(UI.NEWS)

    widget.setFixedSize(582, 409)

    widget.show()

    app.exec_()
