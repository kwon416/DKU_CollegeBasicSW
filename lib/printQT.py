import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 600)#창 기본크기
        self.setWindowTitle("크롤링 결과 창")

        btn = QPushButton(text="뒤로 가기", parent=self)
        btn.move(10, 10)
        btn.clicked.connect(self.back)

        btn = QPushButton("Quit", self)
        btn.move(110, 10)
        btn.clicked.connect(QApplication.instance().quit)

    def back(self):
        print('back')
app = QApplication(sys.argv)
window = MyWindow()
window.show()

app.exec_()