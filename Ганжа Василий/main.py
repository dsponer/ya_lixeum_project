import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel
from main_window import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import shutil


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton_8.clicked.connect(self.change_mode)
        self.pushButton_2.clicked.connect(self.set_image_di)
        self.pushButton_7.clicked.connect(self.py_download)
        self.statusBar.setStyleSheet('background: pink;')
        self.labell = QLabel(self)

    def change_mode(self):
        self.statusBar.removeWidget(self.labell)
        self.statusBar.setStyleSheet('background: pink;')
        self.close()
        os.system('python sup.py')

    def set_image_di(self):
        self.statusBar.removeWidget(self.labell)
        self.statusBar.setStyleSheet('background: pink;')
        self.pixmap = QPixmap('di.JPG')
        print(self.pixmap)
        self.label_3.setPixmap(self.pixmap)

    def py_download(self):
        self.statusBar.removeWidget(self.labell)
        self.statusBar.setStyleSheet('background: pink;')
        name, ok_pressed = QInputDialog.getText(self, "Enter the path to the directory",
                                                "What the path?")
        if ok_pressed:
            try:
                shutil.copy('screen.py', name)
            except shutil.SameFileError:
                self.labell.setText('The Same Files -----------------------------------------------------')
                self.statusBar.setStyleSheet('background: red;')
                self.statusBar.addWidget(self.labell)
            except FileNotFoundError:
                self.labell.setText('File Not Found -----------------------------------------------------')
                self.statusBar.setStyleSheet('background: red;')
                self.statusBar.addWidget(self.labell)
            except Exception:
                self.labell.setText('Error -----------------------------------------------------')
                self.statusBar.setStyleSheet('background: red;')
                self.statusBar.addWidget(self.labell)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec_())
