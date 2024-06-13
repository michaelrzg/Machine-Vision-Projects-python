# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 2: Histogram Equalization
# 6/12/2024

# nessesary imports 
import cv2
from skimage import io
import matplotlib.pyplot as plottool

#define the equalization funciton for this image
# finding a function for this image was more challanging than the previous uni image
# by analizing the histogram we can see that the graph centers around the range (165,220) and has a range with of around 65
# we also see that there are a few outlier pixels in the extremes that would give us issues 
def equalizationFunc(pixel):
    # to account for low outliers that would give weird artifacts in the output, I use a simple if statement
    if pixel <150:
        #if the pixel is below our main range, set it equal to 0 to prevent strange artifacting
        pixel =0
    else:
        #else we subtract the pixel from out lower bound so that we dont lose any colors on the high end, and that we convert the problem back to a simple range expansion in one directoin
        pixel -=150
    # by using the same concept from the previous histogram eq file, we divide each pixel by our range, and scale the (0,1) result to (0,255) by multiplying
    return 255 * (pixel/65)

#define our color range and max color value for the histogram
colorrange = [0,256]
maxsize= [256]
#as usual we set path and use skimage to open file
satpath = 'input/sat_map.png'
satImage = io.imread(satpath)

#print(satImage[0][0])

#define out output image
out = satImage.copy()

#satImage = cv2.cvtColor(satImage,cv2.)

#sshow our input image before processing
plottool.imshow(satImage)
plottool.show()

#calculate histogram for first channel (R)
hist = cv2.calcHist([satImage], [0], None, maxsize, colorrange)
#plot histrogram to show our original image's R channel
plottool.plot(hist)
plottool.show()

#histogram correction for R 
for k in range(0,satImage.shape[0]):
    for p in range(0,satImage.shape[1]):
        out[k][p][0] = equalizationFunc(satImage[k][p][0])

#show output image after our R channel correction
plottool.imshow(out)
plottool.show()

#show equalized historgram for R channel after processing
hist = cv2.calcHist([out], [0], None, maxsize, colorrange)
plottool.plot(hist)
plottool.show()

#histogram correction for G
for k in range(0,satImage.shape[0]):
    for p in range(0,satImage.shape[1]):
        out[k][p][1] = equalizationFunc(satImage[k][p][1])

#show output image after G channel histogram equalization
plottool.imshow(out)
plottool.show()
# show equalized histogram for g values
hist = cv2.calcHist([out], [1], None, maxsize, colorrange)
plottool.plot(hist)
plottool.show()

#correct B values
for k in range(0,satImage.shape[0]):
    for p in range(0,satImage.shape[1]):
        out[k][p][2] = equalizationFunc(satImage[k][p][2])

#show resulting image
plottool.imshow(out)
plottool.show()

#show resulting histo
hist = cv2.calcHist([out], [2], None, maxsize, colorrange)
plottool.plot(hist)
plottool.show()