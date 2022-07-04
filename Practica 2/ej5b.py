import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('ngc4024l.tif',0)
plt.subplot(2,2,1)
plt.imshow(img,'gray')
plt.subplot(2,2,3)
plt.hist(img.ravel(),256,[0,255])

I1 = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
I2 = I1
a=0.5
c=220/255
for n in range(368):
 for m in range(174):
    if I1[m,n]<c:
        I2[m,n]=I1[m,n]*a
    else:
        I2[m,n]=a*c+(I1[m,n]-c)*(1-a*c)/(1-c);

plt.subplot(2,2,2)
plt.imshow(I2,'gray')
plt.subplot(2,2,4)
plt.hist(I2.ravel(),255,[0,1])
plt.show()