"""
    image proccessing 
        Scaling
        Rotating
        Shifting
        Edge Detection
"""
import cv2
import numpy as np
image = cv2.imread('./icons.jpg')

# Scaling image ... Scaling operation increases/reduces size of an image.
(height, width) = image.shape[:2]
scaled_image = cv2.resize(src=image, dsize=(
    height//2, width//2), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Scaling(resize) Image", scaled_image)
cv2.waitKey(0)

# Rotating image
rotation_matrix = cv2.getRotationMatrix2D(
    center=(width//2, height//2), angle=45, scale=1)

rotated_image = cv2.warpAffine(
    src=image, M=rotation_matrix, dsize=(width, height))
cv2.imshow("Rotating Image", rotated_image)
cv2.waitKey(0)

# Shifting image
# Create translation matrix.
# If the shift is (x, y) then matrix would be
# M = [1 0 x]
#     [0 1 y]
# Let's shift by (5, 5).
shifting_matrix = np.float32([[1, 0, 5], [0, 1, 5]])
shifted_image = cv2.warpAffine(
    src=image, M=shifting_matrix, dsize=(width, height))
cv2.imshow("Shifting Image", shifted_image)
cv2.waitKey(0)

# Edge Detection in an image ... detection involves detecting sharp edges in the image
cv2.imshow("Edge Detection in an image", cv2.Canny(
    image=image, threshold1=100, threshold2=100))
cv2.waitKey(0)

# Laplacian Gradient
# Laplacian filter.
laplacian = cv2.Laplacian(src=image, ddepth=cv2.CV_64F)
cv2.imshow("Laplacian filter", laplacian)
cv2.waitKey(0)
# Sobel : Derivative along 'x' direction.
sobelx = cv2.Sobel(src=image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
cv2.imshow("Derivative along 'x' direction", sobelx)
cv2.waitKey(0)
# Sobel : Derivative along 'y' direction.
sobely = cv2.Sobel(src=image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
cv2.imshow("Derivative along 'y' direction", sobely)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
