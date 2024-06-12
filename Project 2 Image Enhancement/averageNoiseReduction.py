# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 3: Noise Reduction via Average Filtering
# 6/12/2024

import cv2
from skimage import io
import matplotlib.pyplot as plottool
import math
def averageFilter(x,y,size):
    s =0
    for i in range(-int(size/2),int(size/2)):
       for j in range(-int(size/2),int(size/2)):
        s+= padded[x+i][y+i][0] / size**2
    return s 

filter_size = [3,5,7]
noisyAtriumPath = 'input/noisy_atrium.png'
noisyAtrium = io.imread(noisyAtriumPath)
noisyAtrium = cv2.cvtColor(noisyAtrium,cv2.COLOR_BGR2RGB)
print(noisyAtrium.shape)
plottool.imshow(noisyAtrium)
plottool.show()

for i in filter_size:
    padding = int(i/2)
    padded = cv2.copyMakeBorder(noisyAtrium,padding,padding,padding,padding,cv2.BORDER_CONSTANT,value=[0,0,0])
    out = padded.copy()
    print("Before")
    plottool.imshow(out)
    plottool.show()  
    for k in range (padding,noisyAtrium.shape[0]-padding):
        for j in range(padding,noisyAtrium.shape[1]-padding):
            V = averageFilter(k,j,i)
            out[k][j] = V
    print("after")
    cv2.imwrite(f'output/reduction/average/filtersize-{i}.png',out)
    plottool.imshow(out)
    plottool.show()        