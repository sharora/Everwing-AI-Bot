from pynput.mouse import Button, Controller
import time
import cv2
import numpy as np
import ImageCapture
import ImageFinder
import random
import os
import neat


#Initial Delay Before Memeing Begins
time.sleep(10)


mouse = Controller()
mouse.press(Button.left)
mouse.position = (625, 630)


count=1
goodguys = []
badguys = []
stop = []
firetemp = '/Users/Shreyas/Desktop/GameElements/fireball.png'
greentemp = '/Users/Shreyas/Desktop/GameElements/green.png'
redtemp = '/Users/Shreyas/Desktop/GameElements/orange.png'
exitfunc = '/Users/Shreyas/Desktop/GameElements/exitim.png'
Templates ={firetemp:badguys, greentemp:goodguys, redtemp:goodguys, exitfunc:stop}


    



#Loop Repeat
while True:
    goodguys = []
    badguys = []
    stop = []
    e1 = cv2.getTickCount()
    ImageCapture.takeimage()
    boom = ImageCapture.boom
    for i,j in Templates.items():
        img = cv2.imread(i, 0)
        ImageFinder.findimage(boom, img)
        l = ImageFinder.l
        if len(l) > 0:
            obj = l[0::4]
            j.append(obj)
            print(obj)
    if len(stop) > 0:
            print('hello')
            break
    e2 = cv2.getTickCount()
    t = (e2 - e1) / cv2.getTickFrequency()
    print(t)
           
##    print(time.time()-last_time)
##    last_time = time.time()
    #Stop after cetain time
    count= count+1
    if count==500:
        break





    
