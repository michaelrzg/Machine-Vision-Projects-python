# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 2: Histogram Equalization
# 6/12/2024

import matplotlib.pyplot as plottool
import cv2
from skimage import io
factor  = 1/(210-140)
def equalizationFunc(pixel):

    return 255 * ((pixel-150)/70)

mapPath = 'input/sat_map.png'
satmap = io.imread(mapPath)
greyrange = [0,256]
maxsize= [256]
hist = cv2.calcHist([satmap], [0], None, maxsize, greyrange)
out= satmap.copy()
plottool.imshow(out)
plottool.show()
plottool.plot(hist)
plottool.show()
factor  = 256/64
print(out.shape)
for k in range(0,satmap.shape[0]):
    for p in range(0,satmap.shape[1]):
        out[k][p] = equalizationFunc(satmap[k][p])
    
        

hist = cv2.calcHist([out], [0], None, maxsize, greyrange)

plottool.plot(hist)
plottool.show()

plottool.imshow(out)
plottool.show()