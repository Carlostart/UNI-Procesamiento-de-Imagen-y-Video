import numpy as np
from matplotlib import pyplot as plt
import cv2

img=np.ones(shape=(100,100))
img[45:55,25:75]=0
plt.subplot(1,2,1)
plt.imshow(img,'gray')

f = np.fft.fft2(img)
f1 = np.fft.fftshift(f)
f2 = np.log(1+np.abs(f1))
plt.subplot(121),plt.imshow(img, 'gray')
plt.title('Imagen de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(f2, 'Greys_r')
plt.title('FFT'), plt.xticks([]), plt.yticks([])
plt.show()
