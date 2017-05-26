import numpy as np
import cv2
import ImageCapture

def findimage(boom, template):
    global l
    l = []
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(boom,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        l.append(pt)
        







    





