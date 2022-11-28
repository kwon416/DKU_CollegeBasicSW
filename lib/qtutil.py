from PyQt5.QtWidgets import *

class QtUtil:
    @staticmethod
    def clearLayout(layout : QLayout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)