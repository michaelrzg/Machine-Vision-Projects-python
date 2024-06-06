from skimage import io
import matplotlib.pyplot as plottool
import cv2
def filter(bits, x):
    if bits==1:
        if x>127:
            return 255
        return 0
    val = 256 / bits
    return val * int(x/val)
    

path = 'apple.jpeg'
image = io.imread(path)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
out = image.copy()
plottool.imshow(image)
plottool.show()

for divisor in range (7,0,-1):
    for k in range(0,image.shape[0]):
        for j in range(0, image.shape[1]):
            v = filter(divisor,int(image[k][j][0]))
            out[k][j] = [v,v,v]
    plottool.imshow(out)
    plottool.show()
    out = image.copy()