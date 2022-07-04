import math
import numpy as np
import cv2
import matplotlib.pyplot as plt
import regiongrowing as rg

#  Representación de imágenes digitales monocromáticas
# a)

a=150;
b=150;

M=300; N=300;

I= np.zeros(shape=(M,N))
for x in range(1,M):
 for y in range(1,N):
    I[x,y]=(255-math.sqrt((x-a)**2+(y-b)**2))/255

plt.imshow(I,'gray')
plt.show()


I2=np.ones(shape=(30,30))
I2[5:24,13:17]=0
plt.imshow(I2,'gray')
plt.show()

I3=cv2.imread('circuit.tif');
plt.subplot(2,1,1)
plt.imshow(I3)
y=40
x=60
h=90
w=100

I3=I3[y:y+h, x:x+w]
plt.subplot(2,1,2)
plt.imshow(I3)
plt.show()

I4=cv2.imread('Galaxia.jpg',0)
plt.subplot(2,1,1)
plt.imshow(I4,'gray')
I4_=I4*1.3+50
plt.subplot(2,1,2)
plt.imshow(I4_,'gray')
plt.show()


height = I4.shape[0]
width = I4.shape[1]
reduction = 20 # percentage
scale = int(reduction/2)
centerX,centerY=int(height/2),int(width/2)
radiusX,radiusY= int(scale*height/100),int(scale*width/100)

minX,maxX=centerX-radiusX,centerX+radiusX
minY,maxY=centerY-radiusY,centerY+radiusY

cropped = I4[minX:maxX, minY:maxY]
cv2.imshow('sin modificar el tamaño',cropped)

resized_cropped = cv2.resize(cropped, (width, height))
plt.imshow(resized_cropped,'gray')
plt.show()
cv2.destroyAllWindows()

image_center = tuple(np.array(resized_cropped.shape[1::-1]) / 2)
rot_mat = cv2.getRotationMatrix2D(image_center, 30, 1.0)
result = cv2.warpAffine(resized_cropped, rot_mat, resized_cropped.shape[1::-1], flags=cv2.INTER_LINEAR)

plt.imshow(result,'gray')
plt.show()

y=101
x=52

I5=cv2.imread('text.tif',0)
mask1 = rg.region_growing(I5,[int(x),int(y)], 80)

y=115
x=196

mask2 = rg.region_growing(I5,[int(x),int(y)], 70)

# # Input image
plt.imshow(mask1+mask2,'gray')
plt.show()