""" 
Intensity transformations are applied on images for contrast manipulation or image thresholding.

    The following are commonly used intensity transformations:
        Image Negatives (Linear)
        Log Transformations
        Power-Law (Gamma) Transformations
        Piecewise-Linear Transformation Functions
"""
import cv2
import numpy as np

img = cv2.imread('icons.jpg')

# Apply log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)

# Specify the data type.
log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imshow('Log Transformations', log_transformed)
cv2.waitKey(0)
