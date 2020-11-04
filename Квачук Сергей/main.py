import sys
import cv2

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer


class Videolink(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('videolink_main.ui', self)

        self.timerVideo = QTimer(self)

        self.startbtn.clicked.connect(self.startTime)
        self.endbtn.clicked.connect(self.endTime)
        self.cap = cv2.VideoCapture(cv2.CAP_DSHOW, 0)
        self.cap.set(3, 480)
        self.cap.set(4, 640)
        self.cap.set(5, 30)

    def viewCam(self):
        ret, image = self.cap.read()
        im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = im.shape
        step = channel * width
        qImg = QImage(im.data, width, height, step, QImage.Format_RGB888)
        self.ui.screen.setPixmap(QPixmap.fromImage(qImg))

    def startTime(self):
        self.timerVideo.start()
        self.timerVideo.timeout.connect(self.viewCam)

    def endTime(self):
        self.timerVideo.stop()
        self.screen.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = Videolink()
    exe.show()
    sys.exit(app.exec())
