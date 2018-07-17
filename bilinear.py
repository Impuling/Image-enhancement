import numpy as np
from PIL import Image
from scipy.misc import imread, imshow
from scipy import ndimage
import matplotlib.pyplot as plt

def BilinearInterpolation(imArr, posX, posY):

    X_int = int(posX)
    Y_int = int(posY)
    X_float = posX - X_int
    Y_float = posY - Y_int
    X_int_inc = min(X_int+1, imArr.shape[0]-1)
    Y_int_inc = min(Y_int+1, imArr.shape[1]-1)

    bl = imArr[X_int, Y_int]
    br = imArr[X_int_inc, Y_int]
    tl = imArr[X_int, Y_int_inc]
    tr = imArr[X_int_inc, Y_int_inc]

    b = X_float*br + (1. - X_float)*bl
    t = X_float*tr + (1. - X_float)*tl
    result = int(Y_float*t + (1. - Y_float)*b + 0.5)

    return result

path = input("Path to picture: ")
img = Image.open(path, 'r')
img = img.convert('L') # преобразование в изображение в оттенках серого
imArr = np.asarray(img)
print(imArr.shape)
k = 2. 
newShape = list(map(int, [imArr.shape[0]*k, imArr.shape[1]*k]))
resultImg = np.empty(newShape, dtype = np.uint8)
rowScale = float(imArr.shape[0]) / float(resultImg.shape[0])  
colScale = float(imArr.shape[1]) / float(resultImg.shape[1])

for r in range(resultImg.shape[0]):
        for c in range(resultImg.shape[1]):
            old_r = r * rowScale 
            old_c = c * colScale
            resultImg[r, c] = BilinearInterpolation(imArr, old_r, old_c)
 
plt.imshow(np.uint8(resultImg), cmap = 'gray')
plt.show()