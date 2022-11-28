import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
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

    ARTICLE_COUNT = 10
    
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_DIR + "news.ui", self)
        self.backBtn.clicked.connect(self.onclick_backBtn)
        data = crawl.CrawlingNews(1)
        h_layouts = [QHBoxLayout() for i in range(NewsUI.ARTICLE_COUNT)]
        for i in range(NewsUI.ARTICLE_COUNT):
            img_url = data.getImgUrl()[i]
            img_data = urllib.request.urlopen(img_url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)
            img_label = QLabel() # 이미지 레이블
            img_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))

            title_label = QLabel() # 제목 레이블
            title_label.setText(data.getTitle()[i])
            title_label.setFixedSize(300, 40)

            date_viewcount_layout = QVBoxLayout() # 날짜/조회수 묶어서 한 레이아웃으로.

            date_label = QLabel(data.getDate()[i])
            date_label.setFixedSize(80, 40)
            viewcount_label = QLabel(data.getViewCount()[i]+"회") # 조회수 레이블
            viewcount_label.setFixedSize(40, 40)

            date_viewcount_layout.addWidget(date_label)
            date_viewcount_layout.addWidget(viewcount_label)

            link_btn = QPushButton("보기")
            link_btn.setFixedSize(40, 40)

            h_layouts[i].addWidget(img_label)
            h_layouts[i].addWidget(title_label)
            h_layouts[i].addLayout(date_viewcount_layout)
            h_layouts[i].addWidget(link_btn)

        for layout in h_layouts:
            self.vboxLayout.addLayout(layout)

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

    widget.setFixedSize(585, 536)

    widget.show()

    app.exec_()
