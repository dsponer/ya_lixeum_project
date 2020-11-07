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
        self.templdict = {self.pushButton_2: ['Template_project\Screens\di.JPG', 'Template_project\py_files\screen.py', 'Template_project\dialog_with_buttons_bottom.ui']
                        }
        self.labell = QLabel(self)
        self.pushButton_8.clicked.connect(self.change_mode)
        self.pushButton_2.clicked.connect(self.set_image_di)
        self.pushButton_7.clicked.connect(self.py_download)
        self.pushButton_9.clicked.connect(self.ui_download)
        self.pushButton_11.clicked.connect(self.add_new_template)
        self.pushButton_10.clicked.connect(self.edit_mode)
        self.statusbar.setStyleSheet('background: pink;')
        self.py_path = False
        self.ui_path = False


    def change_mode(self):
        self.close()
        os.system('python sup.py')

    def ui_download(self):
        self.statusbar.removeWidget(self.labell)
        self.statusbar.setStyleSheet('background: pink;')
        name, ok_pressed = QInputDialog.getText(self, "Enter the path to the directory",
                                                "What the path?                                                                                                ")
        if ok_pressed:
            try:
                shutil.copy(self.ui_path, name)
            except shutil.SameFileError:
                self.labell.setText('The Same Files <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                self.statusbar.setStyleSheet('background: red;')
                self.statusbar.addWidget(self.labell)
            except FileNotFoundError:
                self.labell.setText('File or Directory Not Found <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                self.statusbar.setStyleSheet('background: red;')
                self.statusbar.addWidget(self.labell)

    def edit_mode(self):
        if self.py_path:
            self.close()
            os.system('python ' + self.py_path)

    def add_new_template(self):
        self.templ_name, ok_pressed = QInputDialog.getText(self, "Enter the template name",
                                                        "Name:                                                                                                 ")
        # /////////
        if ok_pressed and self.templ_name != '':
            self.img_path, ok_pressed = QInputDialog.getText(self, "Enter the name and path to the image directory (delimiter=',')",
                                                            "Image size - 1040 x 720                                                                               ")
            if ok_pressed and self.img_path != '':
                self.img_path = self.img_path.split()
                self.img_path = ''.join(self.img_path)
                self.img_name, self.img_path = self.img_path.split(',')
                shutil.copy(self.img_path + '\\' + self.img_name, 'Template_project\Screens')
                # /////////
                self.py_path, ok_pressed = QInputDialog.getText(self, "Enter the name and path to the .py file (delimiter=',')",
                                                                "What the name and path to the .py file?                                                               ")
                self.py_path = self.py_path.split()
                self.py_path = ''.join(self.py_path)
                self.py_name, self.py_path = self.py_path.split(',')
                shutil.copy(self.py_path + '\\' + self.py_name, 'Template_project\py_files')
                # /////////
                self.ui_path, ok_pressed = QInputDialog.getText(self, "Enter the name and path to the .ui file (delimiter=',')",
                                                                "What the name and path to the .ui file?                                                               ")
                self.ui_path = self.ui_path.split()
                self.ui_path = ''.join(self.ui_path)
                self.ui_name, self.ui_path = self.ui_path.split(',')
                shutil.copy(self.ui_path + '\\' + self.ui_name, 'Template_project\yi_files')
                # /////////
                # self.butt = QPushButton(self.scrollAreaWidgetContents)
                # self.butt.setObjectName(self.templ_name)
                # self.butt.setText(self.templ_name)
                # self.verticalLayout.addWidget(self.butt)
                # /////////
                self.templdict[self.butt] = ['Template_project\Screens\\' + self.img_name, 'Template_project\py_files\\' + self.py_name, 'Template_project\yi_files\\' + self.ui_name]
                # /////////
                self.pixmap = QPixmap(self.templdict[self.butt][0])
                self.label_3.setPixmap(self.pixmap)

    def set_image_di(self):
        self.statusbar.removeWidget(self.labell)
        self.statusbar.setStyleSheet('background: pink;')
        self.img_path, self.py_path, self.ui_path = self.templdict[self.sender()]
        self.pixmap = QPixmap(self.img_path)
        self.label_3.setPixmap(self.pixmap)

    def py_download(self):
        self.statusbar.removeWidget(self.labell)
        self.statusbar.setStyleSheet('background: pink;')
        name, ok_pressed = QInputDialog.getText(self, "Enter the path to the directory",
                                                "What the path?                                                                                                ")
        if ok_pressed:
            try:
                shutil.copy(self.py_path, name)
            except shutil.SameFileError:
                self.labell.setText('The Same Files .\/. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                self.statusbar.setStyleSheet('background: red;')
                self.statusbar.addWidget(self.labell)
            except FileNotFoundError:
                self.labell.setText('File Not Found .\/. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                self.statusbar.setStyleSheet('background: red;')
                self.statusbar.addWidget(self.labell)
            except Exception:
                self.labell.setText('Error .\/. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                self.statusbar.setStyleSheet('background: red;')
                self.statusbar.addWidget(self.labell)

    def mouse(self):
        print('Yep')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec_())