# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 2: Histogram Equalization
# 6/12/2024

#Import nessessary tools
import matplotlib.pyplot as plottool
import cv2
from skimage import io

#equalizaion function created to match the histogram for this image

def equalizationFunc(pixel):
    # to find formula, first i analized the histogram distrobution of the graph
    # at first glance, the graph is mostly centered around the range 0,50, meaning the max-min gives us a range of about 50.
    # by dividing each pixel value by 50, we get its ratio, and by then multiplying that ratio by 255, we get its corrected mapped value
    # the formula below does this
    return 255 * (pixel/50)

# image path
mapPath = 'input/university.png'

#read in image
university = io.imread(mapPath)

#color corect image from bgr
university = cv2.cvtColor(university,cv2.COLOR_BGR2RGB)

#define range and max value for histogram tool
greyrange = [0,256]
maxsize= [256]

# utilize cv2 to draw historgram data
hist = cv2.calcHist([university], [0], None, maxsize, greyrange)

#define output image and initilize it to university image
out= university.copy()

#display original image
plottool.imshow(out)
plottool.title("Original image:")
plottool.show()

#display original image's histogram distrobution
plottool.plot(hist)
plottool.title("Original image Histogram:")
plottool.show()


#print(out.shape)
#loop through the input image and apply the equalizaton function to each pixel's grey value, saving the value in the output image
for k in range(0,university.shape[0]):
    for p in range(0,university.shape[1]):
        #apply the formula to each pixel
        out[k][p] = equalizationFunc(university[k][p])
    
        
#calculate new histogram
hist = cv2.calcHist([out], [0], None, maxsize, greyrange)

#display histrogram
plottool.plot(hist)
plottool.title("Equalized Histogram:")
plottool.show()

#display corrected image
plottool.imshow(out)
plottool.title("Equalized Image:")
plottool.show()

#save image
cv2.imwrite('output/hist/university/uniEqualized.png',out)
