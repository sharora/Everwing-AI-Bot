import time
import numpy as np
import wx

app = wx.App()


s = wx.ScreenDC()
w, h = s.Size.Get()
b = wx.EmptyBitmap(w, h)
m = wx.MemoryDCFromDC(s)
m.SelectObject(b)
m.Blit(0, 0, w, h, s, 0, 0)
m.SelectObject(wx.NullBitmap)
b.SaveFile("screenshot.png", wx.BITMAP_TYPE_PNG)
