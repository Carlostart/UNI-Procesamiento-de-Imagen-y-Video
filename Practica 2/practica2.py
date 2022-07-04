import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('spine_grises.tif',0)
plt.subplot(1,2,1)
plt.imshow(img,'gray')
plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,255])
plt.show()


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


img=cv2.imread('ngc4024l.tif',0)
I1 = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
a=0.5 ;
c=220/255 ;
for n in range(368):
 for m in range(174):
    if I1[m,n]<c:
        I2[m,n]=I1[m,n]*a
    else:
        I2[m,n]=a*c+(I1[m,n]-c)*(1-a*c)/(1-c);

plt.subplot(1,2,1)
plt.imshow(I2,'gray')
plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,255])
plt.show()