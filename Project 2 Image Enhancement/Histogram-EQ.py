# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 2: Histogram Equalization
# 6/12/2024

import matplotlib.pyplot as plottool
import cv2
from skimage import io

def equalizationFunc(pixel):

    return 255 * (pixel/50)

mapPath = 'input/university.png'
university = io.imread(mapPath)
university = cv2.cvtColor(university,cv2.COLOR_BGR2RGB)
greyrange = [0,256]
maxsize= [256]
hist = cv2.calcHist([university], [0], None, maxsize, greyrange)
out= university.copy()
plottool.imshow(out)
plottool.show()
plottool.plot(hist)
plottool.show()
factor  = 256/64
print(out.shape)
for k in range(0,university.shape[0]):
    for p in range(0,university.shape[1]):
        out[k][p] = equalizationFunc(university[k][p])
    
        

hist = cv2.calcHist([out], [0], None, maxsize, greyrange)

plottool.plot(hist)
plottool.show()

plottool.imshow(out)
plottool.show()
cv2.imwrite('output/hist/university/uniEqualized.png',out)
