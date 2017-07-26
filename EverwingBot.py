from pynput.mouse import Button, Controller
import time
import cv2
import numpy as np
import ImageCapture
import random
import os
import torch
import torch.utils.data as data_utils
import torch.nn.functional as F
import torch.nn as nn
from torch.autograd import Variable

time.sleep(10)
mouse = Controller()
mouse.position = (625, 600)

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.bn1 = nn.BatchNorm2d(8)
        self.conv2 = nn.Conv2d(8, 16, 5)
        self.conv3 = nn.Conv2d(16, 32, 5)
        self.bn3 = nn.BatchNorm2d(32)
        self.conv4 = nn.Conv2d(32, 64, 5)
        self.fc1 = nn.Linear(64 * 3 * 6, 400)
        self.fc2 = nn.Linear(400, 84)
        self.bn4 = nn.BatchNorm1d(84)
        self.fc3 = nn.Linear(84, 1)

    def forward(self, x):
        x = self.pool(F.elu(self.bn1(self.conv1(x))))
        x = self.pool(F.elu(self.conv2(x)))
        x = self.pool(F.elu(self.bn3(self.conv3(x))))
        x = self.pool(F.elu(self.conv4(x)))
        x = x.view(-1, 64 * 3 * 6)
        x = F.elu(self.fc1(x))
        x = F.dropout(x, p=0.68, training=self.training)
        x = F.elu(self.bn4(self.fc2(x)))
        x = F.dropout(x, p=0.68, training=self.training)
        x = self.fc3(x)
        return x
       

net = Net()

net.load_state_dict(torch.load('ewing.pkl'))

net.eval()

old = 625
lasttime = time.time()
t = lasttime
mouse.press(Button.left)
for i in range(1000):
    boom = ImageCapture.takeimage()
    img = cv2.resize(boom,(165,108))
    img = torch.from_numpy(img)
    img = img.unsqueeze(0)
    img = img.unsqueeze(1)
    img = img.float()
    img = Variable(img)
    output = net(img)
    output = output.data
    output = output.mul(350)             
    output = output.add(465)
    output = output.numpy()
    movement = (output - old) * 1
    movement = movement + output
    mouse.press(Button.left)
    mouse.position = (movement, 640)
    old = movement
    lasttime = time.time()





    
