import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
import time
import numpy as np
import cv2


last_time = time.time()


def takeimage():
    app = QApplication(sys.argv)
    screen = QGuiApplication.primaryScreen()
    desktopPixmap = screen.grabWindow(0)
    img = np.array(desktopPixmap)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
##    cv2.imshow('boom', img)
##    cv2.waitkey(0)

while True:
    takeimage()
    print(time.time()-last_time)
    last_time = time.time()

    

