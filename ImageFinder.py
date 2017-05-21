import numpy as np
import cv2


def findimage(img):
    l = []
    boom = np.array(img)
    template = cv2.imread('/Users/Shreyas/Everwing-AI-Bot/GameElements/Coin.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(boom,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.60
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(boom, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        l.append(pt)
    w = [x[0] for x in l]
    v = [x[1] for x in l]
    x = np.mean(w)
    y = np.mean(v)
    cv2.imwrite('boom45.png', boom)
    





