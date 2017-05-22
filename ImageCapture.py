import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import numpy as np
import cv2
from PIL import Image
import time
import math, random
from pynput.mouse import Button, Controller

time.sleep(15)

SENSITIVITY = 70

mouse = Controller()
mouse.press(Button.left)
mouse.position = (640, 630)


last_time = time.time()
def takeimage():
    global pilimg
    app = QApplication(sys.argv)
    screen = QGuiApplication.primaryScreen()
    desktopPixmap = screen.grabWindow(0,464,170,180,275)
    qimage1 = desktopPixmap.toImage()
    bytes =qimage1.bits().asstring(qimage1.byteCount())
    pilimg = Image.frombuffer("RGBA",(qimage1.width(),qimage1.height()),bytes,'raw', "RGBA", 0, 1)
    l = []
    s = []
    d = []
    lane1 = 0
    lane2 = 0
    lane3 = 0
    lane4 = 0
    lane5 = 0
    img = np.array(pilimg)
    boom = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('/Users/Shreyas/Desktop/fireball.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(boom,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
##        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        l.append(pt)

    template = cv2.imread('/Users/Shreyas/Desktop/orange.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(boom,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
##        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        s.append(pt)

    template = cv2.imread('/Users/Shreyas/Desktop/green.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(boom,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
##        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        d.append(pt)
    return l, s + d

lane = 3
d = 1
file = open("log.txt", "w")
while True:
    print(last_time-time.time())
    lane = math.floor( (mouse.position[0]-640) / 70 ) + 3
    last_time = time.time()
    l, h = takeimage()
    mouse.press(Button.left)
    if(len(l) > 0):
        z = l[0][0]
        x = math.floor( z / 70 ) + 1
        if x == lane:
            if lane == 1 or lane == 2:
                d=1
                mouse.move(SENSITIVITY, 0)
            elif lane == 5 or lane == 4:
                d=-1
                mouse.move(-SENSITIVITY, 0)
            else:
                mouse.move(d * SENSITIVITY, 0)
 


