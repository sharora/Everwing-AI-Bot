import numpy as np

newfile = []
for b in range(30,33):
    file = np.load('EwingData{}.npy'.format(b))
    for l in range(300):
        newfile.append(file[l])
        

    
np.save('TestData.npy', newfile)



##data = np.load("EwingData.npy")
##print(len(data))
