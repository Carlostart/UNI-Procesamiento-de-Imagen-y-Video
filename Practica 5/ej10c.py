import numpy as np
from matplotlib import pyplot as plt
import cv2

img=np.ones(shape=(100,100));
for i in range(100):
    for j in range(100):
        if ((i-50)**2)+((j-50)**2)/(2**2)<300:
            img[i,j]=0
plt.subplot(1,2,1)
plt.imshow(img,'gray')

f = np.fft.fft2(img)
f1 = np.log(1+np.abs(f))
plt.subplot(121),plt.imshow(img, 'gray')
plt.title('Imagen de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(f1, 'jet')
plt.title('FFT'), plt.xticks([]), plt.yticks([]), plt.colorbar()
plt.show()

