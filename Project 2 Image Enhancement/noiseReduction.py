# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 3: Noise Reduction via Average Filtering & Median Filtering
# 6/12/2024

import cv2
from skimage import io
import matplotlib.pyplot as plottool
import statistics

def averageFilter(x,y,size):
    s =0
    
    for i in range(-int(size/2),int(size/2)+1):
       for j in range(-int(size/2),int(size/2)+1):
        s+= padded[x+i][y+j][0] / size**2
    
    return s 

def medianFilter(x,y,size):
    
    s =[]
    
    for i in range(-int(size/2),int(size/2)+1):
       for j in range(-int(size/2),int(size/2)+1):
        s.append( padded[x+i][y+j][0])
    
    s.sort()
    
    return statistics.median(s)

filter_size = [3,5,7]

noisyAtriumPath = 'input/noisy_atrium.png'

noisyAtrium = io.imread(noisyAtriumPath)

noisyAtrium = cv2.cvtColor(noisyAtrium,cv2.COLOR_BGR2RGB)

#print(noisyAtrium.shape)

plottool.imshow(noisyAtrium)

plottool.show()

for i in filter_size:
    
    padding = int(i/2)
    padded = cv2.copyMakeBorder(noisyAtrium,padding,padding,padding,padding,cv2.BORDER_CONSTANT,value=[0,0,0])
    out = padded.copy()
    
    for k in range (padding,noisyAtrium.shape[0]-padding):
        for j in range(padding,noisyAtrium.shape[1]-padding):
            out[k][j] = averageFilter(k,j,i)           
    
    cv2.imwrite(f'output/reduction/average/filtersize-{i}.png',out)
    plottool.imshow(out)
    plottool.show()        

for i in filter_size:
    
    padding = int(i/2)
    padded = cv2.copyMakeBorder(noisyAtrium,padding,padding,padding,padding,cv2.BORDER_CONSTANT,value=[0,0,0])
    out = padded.copy() 
    
    for k in range (padding,noisyAtrium.shape[0]-padding):
        for j in range(padding,noisyAtrium.shape[1]-padding):
            out[k][j] = medianFilter(k,j,i)
           
    cv2.imwrite(f'output/reduction/median/filtersize-{i}.png',out)
    plottool.imshow(out)
    plottool.show()  