"""
Importance of grayscaling 
    Dimension reduction: 
        For example, In RGB images there are three color channels and three dimensions
        while grayscale images are single-dimensional.
    Reduces model complexity: 
        Consider training neural articles on RGB images of 10x10x3 pixels. 
        The input layer will have 300 input nodes. On the other hand, the same neural network will 
        need only 100 input nodes for grayscale images.
    For other algorithms to work: 
        Many algorithms are customized to work only on grayscale images 
        e.g. Canny edge detection function 
        pre-implemented in the OpenCV library works on Grayscale images only.
"""
# we can grayscale image with 3  method
import cv2
image = cv2.imread('./icons.jpg')
image_copy = image.copy()


def gray_scale_image(img):
    col, row = img.shape[0:2]
    for c in range(col):
        for r in range(row):
            img[c, r] = sum(img[c, r])*0.33
    return img

# cv2.cvtColor() method is used to convert an image from one color space to another. 
# There are more than 150 color-space conversion methods available in OpenCV.
image_1=cv2.cvtColor(image_copy,cv2.COLOR_BGR2GRAY)
cv2.imshow("Method 1", image_1)
cv2.waitKey(0)
cv2.imshow("Method 2", gray_scale_image(image_copy))
cv2.waitKey(0)
cv2.imshow("Method 3", cv2.imread('./icons.jpg',0))
cv2.waitKey(0)
cv2.destroyAllWindows()
