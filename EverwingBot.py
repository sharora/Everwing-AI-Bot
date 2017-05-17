from pynput.mouse import Button, Controller
import time
import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui as pui
import wx

app = wx.App()

#Initial Delay Before Memeing Begins
##time.sleep(20)



mouse = Controller()
mouse.position = (625, 630)

last_time = time.time()
#mouse.release(Button.left)
count=1

#Loop Repeat
while True:
##    mouse.press(Button.left)
##    #Move Smoothly
##    for i in range(50):
##        time.sleep(0.00065)
##        mouse.move(5,0)
##    for i in range(50):
##        time.sleep(0.00065)
##        mouse.move(-5,0)
##
##    screen = np.array(ImageGrab.grab(bbox=(0,0,50,50)))
##    screen = np.array(pui.screenshot(region=(0,0,50,50)))
##    s = wx.ScreenDC()
##    w, h = s.Size.Get()
##    b = wx.EmptyBitmap(w, h)
##    m = wx.MemoryDCFromDC(s)
##    m.SelectObject(b)
##    m.Blit(0, 0, w, h, s, 0, 0)
##    del m
##    bb = b.ConvertToImage()
##    img_data = bb.GetData()
##    img_data_str = np.frombuffer(img_data, dtype='uint8')
##    img = img_data_str.reshape((h, w, 3))
##    cv2.imshow("boom", img)
##    

    print(time.time()-last_time)
    last_time = time.time()
    #Stop after cetain time
    count= count+1
    if count==100:
        break
    
##    screenlocation = pui.locateOnScreen('/Users/Shreyas/AI-Everwing-Bot/Coin.png')
##    print(screenlocation)




    
