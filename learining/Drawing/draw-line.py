import cv2
path = r'./draw-line.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Draw line in an image'

# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 0)

# End coordinate, here (width, height)
# represents the bottom right corner of image
end_point = (image.shape[1], image.shape[0])

# Green color in BGR
color = (0, 255, 0)

# Line thickness of 9 px
thickness = 1

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)

# # Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
