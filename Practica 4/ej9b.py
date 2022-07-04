import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('saturno.tif',0)

row,col= img.shape
mean = 0
var = 10
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col))
gauss = gauss.reshape(row,col)
noisy = img + gauss

plt.subplot(1,3,1)
plt.imshow(noisy,'gray')
plt.title('ruido gaussiano')
plt.xticks([])
plt.yticks([])

avg = cv2.blur(noisy,(3,3))

plt.subplot(1,3,2)
plt.imshow(avg,'gray')
plt.title('suavizado')
plt.xticks([])
plt.yticks([])

lap = cv2.Laplacian(avg, cv2.CV_64F)
sharp = avg - 0.7*lap

plt.subplot(1,3,3)
plt.imshow(sharp,'gray')
plt.title('sharpened')
plt.xticks([])
plt.yticks([])
plt.show()