import cv2 as cv
import numpy as np

image = cv.imread('week2/pic/cat.jpg',0)

kernel_size = 100
angle = 90

kernel = np.zeros((kernel_size, kernel_size))
kernel[int((kernel_size-1)/2), :] = np.ones(kernel_size)
kernel = cv.warpAffine(kernel, cv.getRotationMatrix2D((kernel_size/2-0.5, kernel_size/2-0.5),angle, 1.0),(kernel_size, kernel_size))
kernel = kernel / np.sum(kernel)

motion_blur = cv.filter2D(image, -1, kernel)

# cv.imshow('Original Image', image)
cv.imshow('Image', image)
cv.imshow('Motion Blurred Image', motion_blur)
cv.waitKey(0)
cv.destroyAllWindows()
