import sys
from PyQt5.QtWidgets import *
import main as Crawl


class MyApp(QWidget, QLabel):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 800, 200)
        self.initUI()

    def initUI(self):
        self.news = Crawl.CrawlingNews(1)

        self.openExternalLinks()

        self.tableWidget = QTableWidget()
        self.tableWidget.resize(10,10)
        self.tableWidget.setRowCount(len(self.news.getTitle()))
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(['이미지', '제목', '링크', '조회수', '등록일자'])
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        for i in range(10):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.news.getImgUrl()[i]))
        for i in range(10):
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.news.getTitle()[i]))
        for i in range(10):

            self.tableWidget.setItem(i, 2, QTableWidgetItem(self.news.getUrl()[i]))
        for i in range(10):
            self.tableWidget.setItem(i, 3, QTableWidgetItem(self.news.getViewCount()[i]))
        for i in range(10):
            self.tableWidget.setItem(i, 4, QTableWidgetItem(self.news.getDate()[i]))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(100, 100, 1200, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())