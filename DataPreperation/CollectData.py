import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import numpy as np
import cv2
from PIL import Image
import time
import pyautogui




def takeimage():
    global boom
    app = QApplication(sys.argv)
    screen = QGuiApplication.primaryScreen()
    desktopPixmap = screen.grabWindow(0,464,170,180,275)
    qimage1 = desktopPixmap.toImage()
    bytes =qimage1.bits().asstring(qimage1.byteCount())
    pilimg = Image.frombuffer("RGBA",(qimage1.width(),qimage1.height()),bytes,'raw', "RGBA", 0, 1)
    img = np.array(pilimg)
    boom = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

    return boom

time.sleep(10)

lasttime = time.time()

trainingData = []

FileNumber = 33

while True:
    x = pyautogui.position()[0]
    yah = takeimage()
    trainingData.append([yah, x])

    if len(trainingData) == 300:
        print(time.time() - lasttime)
        np.save('EwingData{}.npy'.format(FileNumber), trainingData)
        trainingData = []
        FileNumber += 1
        lasttime = time.time()

        
        
    
 
    


