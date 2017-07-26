import numpy as np
import cv2

data = np.load("Data/TestData.npy")

img = data[:,0]
counter = 0

newdata = []


for i in img:
    resize = cv2.resize(i,(165,108))
    newdata.append([resize, data[counter][1]])
    counter += 1
    

np.save('TestData1.npy', newdata)
    
