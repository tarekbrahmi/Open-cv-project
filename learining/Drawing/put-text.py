import cv2

# path
path = r'./draw-line.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Put text at an image'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
# It is the coordinates of the bottom-left corner of the text string in the image.
# The coordinates are represented as tuples of two values
org = (image.shape[1]//2, image.shape[0]//2)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 1 px
thickness = 1

# This is an optional parameter.It gives the type of the line to be used.
lineType = cv2.LINE_AA

# This is an optional parameter. When it is true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.
bottomLeftOrigin = True

# Using cv2.putText() method
image = cv2.putText(img=image,
                    text='Drow Text',
                    org=org,
                    fontFace=font,
                    fontScale=fontScale,
                    color=color,
                    thickness=thickness,
                    lineType=lineType,
                    bottomLeftOrigin=bottomLeftOrigin
                    )
image = cv2.putText(img=image,
                    text='Drow Text',
                    org=org,
                    fontFace=font,
                    fontScale=fontScale,
                    color=color,
                    thickness=thickness,
                    lineType=lineType,
                    bottomLeftOrigin=not bottomLeftOrigin
                    )
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
