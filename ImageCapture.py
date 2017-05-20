import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import numpy as np
import cv2



def takeimage():
    global arr
    app = QApplication(sys.argv)
    screen = QGuiApplication.primaryScreen()
    desktopPixmap = screen.grabWindow(0,458,170,180,275)
    img = desktopPixmap.toImage()
    incomingImage = img.convertToFormat(4)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  #  Copies the data
    return arr

    # Note the different width height parameter order!
    arr = np.ndarray(shape  = (img_size.height(), img_size.width(), img.depth()//8),
                     buffer = buffer, 
                     dtype  = np.uint8)

    
arr = takeimage()
    

    
    
   


    

