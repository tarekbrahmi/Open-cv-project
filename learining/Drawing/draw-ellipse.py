import cv2

# path
path = r'./draw-line.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Drow an ellipse at an image'

center_coordinates = (image.shape[1]//2, image.shape[0]//2)
# It contains tuple of two variables containing
# major and minor axis of ellipse (major axis length, minor axis length).
axesLength = (100, 50)

# Ellipse rotation angle in degrees.
angle = 90
# Starting angle of the elliptic arc in degrees.
startAngle = 0

# Ending angle of the elliptic arc in degrees.
endAngle = 360

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 1 px
thickness = 1

# Using cv2.ellipse() method
# Draw a ellipse with blue line borders of thickness of 1 px
image = cv2.ellipse(image, center_coordinates, axesLength, angle,
                    startAngle, endAngle, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
