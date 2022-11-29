import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import main as crawl
import urllib.request
import webbrowser
import ssl
from qtutil import QtUtil

ssl._create_default_https_context = ssl._create_unverified_context

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
        widget.setCurrentWidget(UI.TODAY)
    def onclick_noticeBtn(self):
        widget.setCurrentWidget(UI.NOTICE)

class ArticleUI(QDialog):

    ARTICLE_COUNT = 10

    def __init__(self):
        super().__init__()
        uic.loadUi(UI_DIR + "news.ui", self)

        self.backBtn.clicked.connect(self.onclick_backBtn)
        self.pageBtn_1.clicked.connect(self.onclick_pageBtn)
        self.pageBtn_2.clicked.connect(self.onclick_pageBtn)
        self.pageBtn_3.clicked.connect(self.onclick_pageBtn)
        self.pageBtn_4.clicked.connect(self.onclick_pageBtn)
        self.pageBtn_5.clicked.connect(self.onclick_pageBtn)

        self.articleIndex = 0

    def init_articleBox(self, index):
        self.articleIndex = index
        data = self.data[index]

        QtUtil.clearLayout(self.vboxLayout)

        h_layouts = [QHBoxLayout() for i in range(NewsUI.ARTICLE_COUNT)]

        for i in range(ArticleUI.ARTICLE_COUNT):
            img_url = data.getImgUrl()[i]
            img_data = urllib.request.urlopen(img_url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)
            img_label = QLabel()  # 이미지 레이블
            img_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))

            title_label = QLabel()  # 제목 레이블
            title_label.setText(data.getTitle()[i])
            title_label.setFixedSize(350, 40)

            date_viewcount_layout = QVBoxLayout()  # 날짜/조회수 묶어서 한 레이아웃으로.

            date_label = QLabel(data.getDate()[i])
            viewcount_label = QLabel(data.getViewCount()[i] + "회")  # 조회수 레이블
            font = date_label.font()
            font.setPointSize(8)
            date_label.setFont(font)
            viewcount_label.setFont(font)

            date_viewcount_layout.addWidget(date_label)
            date_viewcount_layout.addWidget(viewcount_label)

            link_btn = QPushButton("보기")
            link_btn.setFixedSize(40, 40)
            link_btn.clicked.connect(lambda: self.onclick_linkBtn(data.getUrl()[i]))

            h_layouts[i].addWidget(img_label)
            h_layouts[i].addWidget(title_label)
            h_layouts[i].addLayout(date_viewcount_layout)
            h_layouts[i].addWidget(link_btn)

        for layout in h_layouts:
            self.vboxLayout.addLayout(layout)

    def onclick_backBtn(self):
        widget.setCurrentWidget(UI.HOME)

    def onclick_pageBtn(self):
        btn: QPushButton = self.sender()
        i = int(btn.text()) - 1 # 데이터는 인덱스 기준이니까 1을 뺌
        self.init_articleBox(i)

    def onclick_linkBtn(self, url):
        btn: QPushButton = self.sender()
        i = btn.property("id")
        url = self.data[self.articleIndex].getUrl()[i]
        webbrowser.open(url)

class NewsUI(ArticleUI):
    def __init__(self):
        super().__init__()
        self.data = [ crawl.CrawlingNews(i) for i in range(1, 6) ]
        self.init_articleBox(0)

class TodayUI(ArticleUI):
    def __init__(self):
        super().__init__()
        self.data = [ crawl.CrawlingToday(i) for i in range(1, 6) ]
        self.init_articleBox(0)

class NoticeUI(ArticleUI):
    def __init__(self):
        super().__init__()
        self.data = [ crawl.CrawlingNotice(i) for i in range(1, 6) ]
        self.init_articleBox(0)


class UI:
    HOME : HomeUI
    NEWS : NewsUI
    TODAY : TodayUI
    NOTICE : NoticeUI
    @staticmethod
    def init():
        UI.HOME = HomeUI()
        UI.NEWS = NewsUI()
        UI.TODAY = TodayUI()
        # UI.NOTICE = NoticeUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    UI.init()

    widget = QStackedWidget()
    widget.addWidget(UI.HOME)
    widget.addWidget(UI.NEWS)
    widget.addWidget(UI.TODAY)
    # widget.addWidget(UI.NOTICE)

    widget.setFixedSize(585, 560)

    widget.show()

    app.exec_()
