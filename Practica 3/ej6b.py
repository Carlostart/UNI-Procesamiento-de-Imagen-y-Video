import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Fig6.48(c).jpg')

plt.subplot(2,2,1)
plt.imshow(img)
plt.title('Input image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.hist(gray_scale.ravel(),256,[0,255])
plt.title('Input image')
plt.ylim(top=1250)

plt.subplot(2,2,2)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray_scale)
# clahe = cv2.createCLAHE()
# equalized = clahe.apply(gray_scale)
plt.imshow(equalized,'gray')
plt.title('Equialized image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.hist(equalized.ravel(),256,[0,255])
plt.title('Equialized image')
plt.ylim(top=1250)
plt.show()
