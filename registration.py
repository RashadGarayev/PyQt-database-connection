# -*-coding: utf-8 -*-
from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sys
class window(QWidget):
        def __init__(self, parent=None):
            super(window, self).__init__(parent)
            self.setWindowTitle(u"First GUI")
            self.setWindowIcon(QIcon("C:\\Users\\xaos\\Desktop\\photo.jpg"))
            self.setGeometry(200,200,600,600)
            self.setFixedSize(600,600)
            self.setStyleSheet("background-color:white;")
            self.label=QLabel(self)
            self.label.setText("""
        Hello world
        Hello Pyqt
        Hello python
        """)
            self.label.setStyleSheet("color:red;"
                                     "font-size:14pt;"
                                     "font-family:Courier;")
            self.label.move(100,60)


            self.show()
            
            

if __name__ == '__main__':
    app = QApplication([])
    gui=window()
    app.exec_()




