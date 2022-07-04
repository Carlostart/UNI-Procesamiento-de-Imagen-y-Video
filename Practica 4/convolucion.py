import numpy as np
import cv2

def convolucion(img, kernel):
    h, w = img.shape
    newverticalImage = np.zeros((h, w))

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            verticalimg = (kernel[0, 0] * img[i - 1, j - 1]) + \
                          (kernel[0, 1] * img[i - 1, j]) + \
                          (kernel[0, 2] * img[i - 1, j + 1]) + \
                          (kernel[1, 0] * img[i, j - 1]) + \
                          (kernel[1, 1] * img[i, j]) + \
                          (kernel[1, 2] * img[i, j + 1]) + \
                          (kernel[2, 0] * img[i + 1, j - 1]) + \
                          (kernel[2, 1] * img[i + 1, j]) + \
                          (kernel[2, 2] * img[i + 1, j + 1])

            newverticalImage[i - 1, j - 1] = verticalimg
    return newverticalImage