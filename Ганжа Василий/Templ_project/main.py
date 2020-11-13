import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLabel, QPushButton
from main_window import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QFont
import shutil
import csv


class NoFileSelected(Exception):
    pass


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.labell = QLabel(self)
        self.pushButton_2.setText('Lines_and_but')
        self.btn_list = [self.pushButton_11, self.pushButton_7,
                         self.pushButton_8, self.pushButton_9, self.pushButton_10, self.pushButton_2]
        csv_file = open('templ.csv', encoding="utf8")
        reader = csv.reader(csv_file, delimiter=';', quotechar='"')
        title = next(reader)
        for i in reader:
            for j in range(len(self.btn_list)):
                if i[0] == self.btn_list[j].text():
                    break
                if j == len(self.btn_list) - 1:
                    self.butt = QPushButton(self.scrollAreaWidgetContents)
                    font = QFont()
                    font.setFamily("Rockwell")
                    font.setPointSize(10)
                    font.setBold(False)
                    font.setItalic(True)
                    font.setWeight(50)
                    self.butt.setFont(font)
                    self.butt.setObjectName(i[0])
                    self.butt.setText(i[0])
                    self.butt.clicked.connect(self.set_image)
                    self.verticalLayout.addWidget(self.butt)
        self.pushButton_8.clicked.connect(self.change_mode)
        self.pushButton_2.clicked.connect(self.set_image)
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
        try:
            self.statusbar.removeWidget(self.labell)
            self.statusbar.setStyleSheet('background: pink;')
            if not self.py_path:
                raise NoFileSelected
            name, ok_pressed = QInputDialog.getText(self, "Enter the path to the directory",
                "What the path?                                                                                                ")
            if ok_pressed:
                shutil.copy(self.py_path, name)
        except NoFileSelected:
            self.labell.setText('Choose Template pls .\/. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            self.statusbar.setStyleSheet('background: red;')
            self.statusbar.addWidget(self.labell)
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

    def edit_mode(self):
        if self.py_path:
            self.close()
            os.system('python ' + self.py_path)

    def add_new_template(self):
        csv_file = open('templ.csv', encoding="utf8")
        read = csv.reader(csv_file, delimiter=';', quotechar='"')
        wcsv_file = open('templ_files.csv', 'w', newline='', encoding='utf8')
        writer = csv.writer(
            wcsv_file, delimiter=';', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
        for row in read:
            writer.writerow(row)
        self.templ_name, ok_pressed = QInputDialog.getText(self, "Enter the template name",
                                                        "Name:                                                                                                 ")
        # /////////
        if ok_pressed and self.templ_name != '':
            self.img_path, ok_pressed = QInputDialog.getText(self, "Enter the name and path to the image directory (delimiter=',')",
                                                            "Image size - 1040 x 720                                                                                                         ")
            if ok_pressed and self.img_path != '':
                try:
                    self.img_path = self.img_path.split()
                    self.img_path = ''.join(self.img_path)
                    self.img_name, self.img_path = self.img_path.split(',')
                    shutil.copy(self.img_path + '\\' + self.img_name, 'Screens')
                    # /////////
                    self.py_path, ok_pressed = QInputDialog.getText(self, "Enter the name and path to the .py file (delimiter=',')",
                                                                    "What the name and path to the .py file?                                                               ")
                    self.py_path = self.py_path.split()
                    self.py_path = ''.join(self.py_path)
                    self.py_name, self.py_path = self.py_path.split(',')
                    self.py_path = self.py_path + '\\' + self.py_name
                    shutil.copy(self.py_path, 'py_files')
                    # /////////
                    self.ui_path, ok_pressed = QInputDialog.getText(self, "Enter the name and path to the .ui file (delimiter=',')",
                                                                    "What the name and path to the .ui file?                                                               ")
                    self.ui_path = self.ui_path.split()
                    self.ui_path = ''.join(self.ui_path)
                    self.ui_name, self.ui_path = self.ui_path.split(',')
                    self.ui_path = self.ui_path + '\\' + self.ui_name
                    shutil.copy(self.ui_path, 'py_files\yi_files')
                    self.butt = QPushButton(self.scrollAreaWidgetContents)
                    font = QFont()
                    font.setFamily("Rockwell")
                    font.setPointSize(10)
                    font.setBold(False)
                    font.setItalic(True)
                    font.setWeight(50)
                    self.butt.setFont(font)
                    self.butt.setObjectName(self.templ_name)
                    self.butt.setText(self.templ_name)
                    self.butt.clicked.connect(self.set_image)
                    self.verticalLayout.addWidget(self.butt)
                    writer.writerow([self.butt.text(), 'Screens\\' + self.img_name, 'py_files\\' + self.py_name,
                                     'py_files\yi_files\\' + self.ui_name])
                    wcsv_file.close()
                    csv_file.close()
                    shutil.copy('templ_files.csv', 'templ.csv')
                    self.pixmap = QPixmap('Screens\\' + self.img_name)
                    self.label_3.setPixmap(self.pixmap)
                except FileNotFoundError:
                    self.labell.setText(
                        'File or Directory Not Found <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    self.statusbar.setStyleSheet('background: red;')
                    self.statusbar.addWidget(self.labell)
                except Exception:
                    self.labell.setText(
                        'Error <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    self.statusbar.setStyleSheet('background: red;')
                    self.statusbar.addWidget(self.labell)

    def set_image(self):
        csv_file = open('templ.csv', encoding="utf8")
        reader = csv.reader(csv_file, delimiter=';', quotechar='"')
        for row in reader:
            if row[0] == self.sender().text():
                self.img_path, self.py_path, self.ui_path = row[1:]
        self.statusbar.removeWidget(self.labell)
        self.statusbar.setStyleSheet('background: pink;')

        self.pixmap = QPixmap(self.img_path)
        self.label_3.setPixmap(self.pixmap)
        self.label_3.setStyleSheet('background-color: rgb();')

    def py_download(self):
        try:
            self.statusbar.removeWidget(self.labell)
            self.statusbar.setStyleSheet('background: pink;')
            if not self.py_path:
                raise NoFileSelected
            name, ok_pressed = QInputDialog.getText(self, "Enter the path to the directory",
                                                "What the path?                                                                                                ")
            if ok_pressed:
                shutil.copy(self.py_path, name)
        except NoFileSelected:
            self.labell.setText('Choose Template pls .\/. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            self.statusbar.setStyleSheet('background: red;')
            self.statusbar.addWidget(self.labell)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec_())