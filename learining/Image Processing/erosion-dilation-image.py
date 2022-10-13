"""
    Uses of Erosion and Dilation: 
        Erosion: 
            It is useful for removing small white noises.
            Used to detach two connected objects etc.
        Dilation:
            In cases like noise removal, erosion is followed by dilation. 
            Because, erosion removes white noises, but it also shrinks our object. 
            So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
            It is also useful in joining broken parts of an object.
"""
import cv2
import numpy as np


img = cv2.imread('./icons.jpg', 0)

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5, 5), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)
