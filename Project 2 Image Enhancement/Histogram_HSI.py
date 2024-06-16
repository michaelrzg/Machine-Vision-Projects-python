# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 5: HSI Equalization
# 6/16/2024

from skimage import io
import cv2
import matplotlib.pyplot as plottool

def equalizationFunc(pixel):
    # to account for low outliers that would give weird artifacts in the output, I use a simple if statement
    if pixel <150:
        #if the pixel is below our main range, set it equal to 0 to prevent strange artifacting
        pixel =0
    else:
        #else we subtract the pixel from out lower bound so that we dont lose any colors on the high end, and that we convert the problem back to a simple range expansion in one directoin
        pixel -=150
    # by using the same concept from the previous histogram eq file, we divide each pixel by our range, and scale the (0,1) result to (0,255) by multiplying
    return 255 * (pixel/70)
#define path
mapPath = 'input/sat_map.png'
# read in image using skimage.io
satMap = io.imread(mapPath)

#show original image
plottool.imshow(satMap)
plottool.show()
#convert colors to hsv color scale
satMap = cv2.cvtColor(satMap,cv2.COLOR_BGR2HSV)

#calculate initial histogram for hsi [i] element
hist = cv2.calcHist([satMap],[2],None, [256],[0,256])

#display original histogram
plottool.plot(hist)
plottool.title("Satmap I histogram distribution:")
plottool.savefig('output/hist/HSI/OriginalHist.png')
plottool.show()

#define output image
out = satMap.copy()

#histogram correction for I 
for k in range(0,satMap.shape[0]):
    for p in range(0,satMap.shape[1]):
        out[k][p][2] = equalizationFunc(satMap[k][p][2])

#calculate new corrected histogram
hist = cv2.calcHist([out],[2],None, [256],[0,256])

#plot new histogram 
plottool.plot(hist)
plottool.title("Satmap I Equalized histogram distribution:")
plottool.savefig('output/hist/HSI/CorrectedHist.png')
plottool.show()

#show image after I histogram correction
out = cv2.cvtColor(out,cv2.COLOR_HSV2BGR)
cv2.imwrite('output/hist/HSI/correctedSatMap.png',out)
plottool.imshow(out)
plottool.show()