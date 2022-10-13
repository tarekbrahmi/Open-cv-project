import numpy as np
import cv2

# Width and height of the black window
width = 400  # X
height = 300  # Y

# Create a black window of 400 x 300
img = np.zeros((height, width, 3), np.uint8)

# Three vertices(tuples) of the triangle
p1 = (width//2, 5)
p2 = (width-5, height-5)
p3 = (5, height-5)

# Drawing the triangle with the help of lines
# on the black window With given points
# cv2.line is the inbuilt function in opencv library
cv2.line(img, p1, p2, (255, 0, 0), 3)
cv2.line(img, p2, p3, (255, 0, 0), 3)
cv2.line(img, p1, p3, (255, 0, 0), 3)

# finding centroid using the following formula
# (X, Y) = (x1 + x2 + x3//3, y1 + y2 + y3//3)
centroid = ((p1[0]+p2[0]+p3[0])//3, (p1[1]+p2[1]+p3[1])//3)

# Drawing the centroid on the window
cv2.circle(img, centroid, 4, (0, 255, 0))

# Three vertices(tuples) of the triangle
p4 = (5, 5)
p5 = (width-5, 5)
p6 = (width//2, height-5)

# Drawing the triangle with the help of lines
# on the black window With given points
# cv2.line is the inbuilt function in opencv library
cv2.line(img, p4, p5, (0, 255, 0), 2)
cv2.line(img, p5, p6, (0, 255, 0), 2)
cv2.line(img, p4, p6, (0, 255, 0), 2)

centroid2 = ((p4[0]+p5[0]+p6[0])//3, (p4[1]+p5[1]+p6[1])//3)
cv2.circle(img=img, center=centroid2, radius=3, color=(0, 0, 255), thickness=1)

# image is the title of the window
cv2.imshow("Draw a triangle with his centroid", img)
cv2.waitKey(0)
