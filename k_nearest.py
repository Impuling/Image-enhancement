import numpy as np 
from PIL import Image
from scipy.misc import imread, imshow
from scipy import ndimage
import matplotlib.pyplot as plt 

def kNearest(imArr, k, posX, posY):

	summ = 0
	values = []
	out = []
	for r in range(max(0, int(posX)), min(imArr.shape[0], int(posX+k))):
		for c in range(max(0, int(posY-k)), min(imArr.shape[1], int(posY+k))):
			difference_x = posX - r
			difference_y = posY - c
			sqr = float(difference_x**2 + difference_y**2)
			values.append(imArr[r,c]) # яркость в точке
			out.append(sqr) # расстояния до точек

	values = np.array(values)
	out = np.array(out)
	temp = np.vstack([out, values])
	out = np.argsort(out)
	
	i = 0
	while i < k:
		elem = out[i]
		summ += temp[1, elem]
		i += 1

	result = summ/k
	return result



path = input("Path to picture: ")
img = Image.open(path, 'r')
img = img.convert('L')
imArr = np.asarray(img)
pix = img.load()
k = input("Enter k: ")
k = int(k)

newShape = list(map(int, [imArr.shape[0]*2, imArr.shape[1]*2]))
resultImg = np.empty(newShape, dtype = np.uint8)
rowScale = float(imArr.shape[0]) / float(resultImg.shape[0])
colScale = float(imArr.shape[1]) / float(resultImg.shape[1])

for r in range(resultImg.shape[0]):
        for c in range(resultImg.shape[1]):
            old_r = r * rowScale 
            old_c = c * colScale
            resultImg[r, c] = kNearest(imArr, k, old_r, old_c)
 			
plt.imshow(np.uint8(resultImg), cmap = 'gray')
plt.show()