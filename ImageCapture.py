import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import numpy as np
import cv2
from PIL import Image
import time
##import math, random
##from pynput.mouse import Button, Controller

##
##SENSITIVITY = 70
##
##mouse = Controller()
##mouse.press(Button.left)
##mouse.position = (640, 630)
##
##
##last_time = time.time()


def takeimage():
    global boom
    app = QApplication(sys.argv)
    screen = QGuiApplication.primaryScreen()
    desktopPixmap = screen.grabWindow(0,464,170,180,275)
    qimage1 = desktopPixmap.toImage()
    bytes =qimage1.bits().asstring(qimage1.byteCount())
    pilimg = Image.frombuffer("RGBA",(qimage1.width(),qimage1.height()),bytes,'raw', "RGBA", 0, 1)
    img = np.array(pilimg)
    boom = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return boom

boom = takeimage()

##lane = 3
##d = 1
##while True:
##    print(last_time-time.time())
##    lane = math.floor( (mouse.position[0]-640) / 70 ) + 3
##    last_time = time.time()
##    l, h = takeimage()
##    mouse.press(Button.left)
##    if(len(l) > 0):
##        z = l[0][0]
##        x = math.floor( z / 70 ) + 1
##        if x == lane:
##            if lane == 1 or lane == 2:
##                d=1
##                mouse.move(SENSITIVITY, 0)
##            elif lane == 5 or lane == 4:
##                d=-1
##                mouse.move(-SENSITIVITY, 0)
##            else:
##                mouse.move(d * SENSITIVITY, 0)
 


