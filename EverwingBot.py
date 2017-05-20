from pynput.mouse import Button, Controller
import time
import cv2
import numpy as np
import ImageCapture
import ImageFinder

#Initial Delay Before Memeing Begins
##time.sleep(20)

mouse = Controller()
mouse.position = (625, 630)


last_time = time.time()
#mouse.release(Button.left)
count=1

#Loop Repeat
while True:
    ImageCapture.takeimage()
    img = ImageCapture.arr
    ImageFinder.findimage(img)
    print(time.time()-last_time)
    last_time = time.time()
    #Stop after cetain time
    count= count+1
    if count==500:
        break





    
