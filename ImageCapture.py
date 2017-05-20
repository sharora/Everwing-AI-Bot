import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import numpy as np
import cv2
from PIL import Image


def takeimage():
    global pilimg
    app = QApplication(sys.argv)
    screen = QGuiApplication.primaryScreen()
    desktopPixmap = screen.grabWindow(0,458,170,180,275)
    img = desktopPixmap.toImage()
    qimage1 = QtGui.QImage(img)
    bytes=qimage1.bits().asstring(qimage1.byteCount())
    pilimg = Image.frombuffer("L",(qimage1.width(),qimage1.height()),bytes,'raw', "L", 0, 1)
    return pilimg
 

    
pilimg = takeimage()
    

    
    
   


    

