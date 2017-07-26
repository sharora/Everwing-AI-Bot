import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from torchvision import transforms
import tqdm
import torch.optim as optim
import time
import torch.utils.data as data_utils
import matplotlib.pyplot as plt


epochs = 4
data = np.load("Data/TrainData.npy")
image = data[:,0]
tenMov = torch.Tensor(data[:,1])
tenMov = tenMov.float()
tenImg = torch.stack([torch.from_numpy(i) for i in image])
tenImg = tenImg.unsqueeze(1)
train = data_utils.TensorDataset(tenImg, tenMov)
train_loader = data_utils.DataLoader(train, batch_size=64, shuffle=True)
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


criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
l = time.time()

lossdata = []

net.train()

for i in range(epochs):
    print("yo")
    for i, data in enumerate(train_loader, 0):
        Img, Mov = data
        Img = Img.float()
        Mov = Mov.float()
        Mov = Mov.sub(465)
        Mov = Mov.div(350)
        Img, Mov = Variable(Img), Variable(Mov)
        optimizer.zero_grad()
        outputs = net(Img)
        loss = criterion(outputs, Mov)
        error = loss.data.numpy()
        lossdata.append(error)
        print(error)
        loss.backward()
        optimizer.step()
        
print('Finished Training')


testdata = np.load("Data/TestData1.npy")
testimage = testdata[:,0]
testMov = torch.Tensor(testdata[:,1])
testMov = testMov.float()
timage = torch.stack([torch.from_numpy(m) for m in testimage])
timage = timage.unsqueeze(1)
test = data_utils.TensorDataset(timage, testMov)
test_loader = data_utils.DataLoader(test, batch_size=64, shuffle=True)

net.eval()
testloss = []

for data in test_loader:
    Img, Mov = data
    Img = Img.float()
    Mov = Mov.float()
    Mov = Mov.sub(465)
    Mov = Mov.div(350)
    Img, Mov = Variable(Img), Variable(Mov)
    optimizer.zero_grad()
    outputs = net(Img)
    loss = criterion(outputs, Mov)
    error = loss.data.numpy()
    testloss.append(error)
    print(error)
    
    
    




