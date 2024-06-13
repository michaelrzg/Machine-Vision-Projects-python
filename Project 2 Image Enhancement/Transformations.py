# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 1: Transformation
# 6/11/2024

#nessessary imports
from skimage import io
import matplotlib.pyplot as plottool
import cv2
import math

#define image path
uniPath = 'input/university.png'

#create image object with skimage
image = io.imread(uniPath)

#color correction
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#define an output image as copy of input
out = image.copy()

# display input image
plottool.imshow(image)
plottool.show()

# log transformation with varying constant factors:
constant = [30,50,70,90,120,150]
#outer loop goes through each log constant
for k in range(6):
    
    # loop through each image pixel
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            #using the formula found in the slides :
            # s = T(r) = c * Log(1 + r) where r = greylevel
            # along with varying constants, we can see how the log transformation maps the narrow
            # range found in this image to a wider range 
            f = math.log10(1+ image[i][j][1]) *constant[k]
            
            #set pixel to this grey value
            out[i][j] = [f,f,f]
    #display results for each log run
    plottool.imshow(out)
    plottool.title(f'y = log(1+ x) * {constant[k]}')
    plottool.show()
    
    #save results with informative name
    cv2.imwrite(f'output/log/logConstant-{constant[k]}.png',out)
    
    #initilize/reset output image
    out=image.copy()
    
# power law transformation with varying gamma and y valyes:
# from the slides, we know that expanding narrow ranges utilizes a smaller y pwer, while narrowing utilized a larger y
# for this reason we are using smaller and smaller y values to see effect
yValue = [.9,.8,.7,.6,.5,.4]
#we define a few gamma levels to see difference
gamma = [1,1.5,2.2]

#outer loop goes through each gamma 
for l in range(3):
    # k loop goes through each y value
    for k in range(6):
        # i,j for each pixel in image
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                # using the formula from the lecture slides:
                # s = c * r^y
                # we apply this fomula with varying y values, and adjust for gamma by dividing each y value by a gamma level
                # we use the c values 255 to scale the range from 0,1 given by the power to 0,255
                f = math.pow(image[i][j][1]/255,(yValue[k]/gamma[l]))*255
                
                #set pixel grey level to function output
                out[i][j] = [f,f,f]
        #display this runs results
        plottool.imshow(out)
        plottool.title( f'y={yValue[k]}, gamma={gamma[l]}') 
        plottool.show()
        # save results with name contianing gamma and y value used
        cv2.imwrite(f'output/power/gamma-{gamma[l]}/yValue-{yValue[k]}.png',out)
        #reset output image for next run
        out=image.copy()


