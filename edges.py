import cv2
import numpy as np
import ImageCapture

e1 = cv2.getTickCount()
ImageCapture.takeimage()
boom = ImageCapture.boom

hsv = cv2.cvtColor(boom, cv2.COLOR_BGR2HSV)

lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(boom,boom, mask= mask)

edges = cv2.Canny(boom,100,200)
cv2.imwrite('boom81.png', edges)
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print(t)
    
    
   


