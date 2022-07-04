import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('ngc4024l.tif',0)
I1 = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
I2 = I1
w,h = img.shape
for n in range(h):
    for m in range(w):
        I2[m,n] = 1*(I1[m,n]**2)
        if I2[m,n]>1:
            I2[m,n]=1
plt.subplot(1,2,1)
plt.imshow(I2,'gray')
plt.subplot(1,2,2)
plt.hist(I2.ravel(),256,[0,1])
plt.show()
