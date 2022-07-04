import cv2
import matplotlib.pyplot as plt
import numpy as np
import convolucion as cnv

img = cv2.imread('coins.png',0)
img_gaussian = cv2.GaussianBlur(img,(3,3),0)

sobelx = cv2.Sobel(img_gaussian,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img_gaussian,cv2.CV_64F,0,1,ksize=3)

abs_sobel64f = np.absolute(sobelx)
sobelx = np.uint8(abs_sobel64f)

abs_sobel64f = np.absolute(sobely)
sobely = np.uint8(abs_sobel64f)

sobel = np.sqrt(pow(sobelx, 2.0) + pow(sobely, 2.0))

retval, sobel = cv2.threshold(sobel,130,255,cv2.THRESH_BINARY)

plt.subplot(1,3,1)
plt.imshow(sobel, 'gray')
plt.title('Sobel')
plt.xticks([])
plt.yticks([])

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewittx = cnv.convolucion(img_gaussian, kernelx)
prewitty = cnv.convolucion(img_gaussian, kernely)

prewitt = mag = np.sqrt(pow(prewitty, 2.0) + pow(prewittx, 2.0))

retval, prewitt = cv2.threshold(prewitt,100,255,cv2.THRESH_BINARY)


plt.subplot(1,3,2)
plt.imshow(prewitt , 'gray')
plt.title('Prewitt')
plt.xticks([])
plt.yticks([])

canny = cv2.Canny(img,100,200)

plt.subplot(1,3,3)
plt.imshow(canny , 'gray')
plt.title('Canny')
plt.xticks([])
plt.yticks([])


plt.show()
