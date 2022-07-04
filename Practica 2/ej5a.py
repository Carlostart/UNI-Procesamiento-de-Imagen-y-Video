import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('spine_grises.tif',0)
I1 = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
I2 = I1
for n in range(490):
 for m in range(367):
     I2[m,n]=I1[m,n]*255/63
     if I2[m,n]<1:
        I2[m,n]=0
plt.subplot(1,2,1)
plt.imshow(I2,'gray')
plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,255])
plt.show()
