

import cv2
from skimage import io
import matplotlib.pyplot as plottool

def equalizationFunc(pixel):
    if pixel <150:
        pixel =0
    else:
        pixel -=150
    return 255 * (pixel/65)


greyrange = [0,256]
maxsize= [256]
satpath = 'input/sat_map.png'
satImage = io.imread(satpath)
print(satImage[0][0])
out = satImage.copy()
#satImage = cv2.cvtColor(satImage,cv2.)
plottool.imshow(satImage)
plottool.show()
hist = cv2.calcHist([satImage], [0], None, maxsize, greyrange)
plottool.plot(hist)
plottool.show()

for k in range(0,satImage.shape[0]):
    for p in range(0,satImage.shape[1]):
        out[k][p][0] = equalizationFunc(satImage[k][p][0])

plottool.imshow(out)
plottool.show()
hist = cv2.calcHist([out], [0], None, maxsize, greyrange)
plottool.plot(hist)
plottool.show()
for k in range(0,satImage.shape[0]):
    for p in range(0,satImage.shape[1]):
        out[k][p][1] = equalizationFunc(satImage[k][p][1])

plottool.imshow(out)
plottool.show()
hist = cv2.calcHist([out], [1], None, maxsize, greyrange)
plottool.plot(hist)
plottool.show()
for k in range(0,satImage.shape[0]):
    for p in range(0,satImage.shape[1]):
        out[k][p][2] = equalizationFunc(satImage[k][p][2])

plottool.imshow(out)
plottool.show()
hist = cv2.calcHist([out], [2], None, maxsize, greyrange)
plottool.plot(hist)
plottool.show()