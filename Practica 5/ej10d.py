import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

img= np.zeros(shape=(100,100))
for x in range(100):
 for y in range(100):
    img[x,y]=(255-math.sqrt((x-150)**2+(y-150)**2/2))/255
plt.subplot(1,2,1)
plt.imshow(img,'gray')

f = np.fft.fft2(img)
f1 = np.fft.fftshift(f)
f2 = np.log(1+np.abs(f1))
plt.subplot(121),plt.imshow(img, 'gray')
plt.title('Imagen de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(f2, 'jet')
plt.title('FFT'), plt.xticks([]), plt.yticks([]), plt.colorbar()
plt.show()

