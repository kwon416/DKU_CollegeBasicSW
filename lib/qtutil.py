from PyQt5.QtWidgets import *

class QtUtil:
    @staticmethod
    def clearLayout(layout : QLayout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    QtUtil.clearLayout(item.layout()) # 아이템이 레이아웃 일 경우 그 레이아웃도 비움.