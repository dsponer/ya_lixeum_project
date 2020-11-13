import sys
import os
from subwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class Alternative_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton_61.clicked.connect(self.change_mode)

    def change_mode(self):
        self.close()
        os.system('python main.py')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alternative_Window()
    ex.show()
    sys.exit(app.exec_())