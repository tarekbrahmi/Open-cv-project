import cv2
import numpy as np

# path
path = r'./icons.jpg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Creating kernel
kernel = np.ones((9, 9), np.uint8)

# Using cv2.erode() method
image = cv2.erode(image, kernel, borderType=cv2.BORDER_REFLECT)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
