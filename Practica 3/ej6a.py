import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('5.2.09.tiff')

plt.subplot(2,3,1)
plt.imshow(img)
plt.title('Input image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,4)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.hist(gray_scale.ravel(),256,[0,255])
plt.title('Input image')
plt.ylim(top=1250)

plt.subplot(2,3,2)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray_scale)
plt.imshow(equalized,'gray')
plt.title('Equialized image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,5)
plt.hist(equalized.ravel(),256,[0,255])
plt.title('Equialized image')
plt.ylim(top=1250)

plt.subplot(2,3,3)
result=gray_scale-equalized
plt.imshow(result,'gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,6)
plt.hist(result.ravel(),256,[0,255])
plt.ylim(top=1250)
plt.show()