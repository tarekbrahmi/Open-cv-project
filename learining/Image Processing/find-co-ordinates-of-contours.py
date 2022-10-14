import cv2
font = cv2.FONT_HERSHEY_COMPLEX
original_image = cv2.imread('contours.jpg', cv2.IMREAD_COLOR)

# Reading same image in another
# variable and converting to gray scale.
image_to_proccess = cv2.imread('contours.jpg', cv2.IMREAD_GRAYSCALE)

# Converting image to a binary image
# ( black and white only image).
_, threshold = cv2.threshold(image_to_proccess, 29, 255, cv2.THRESH_BINARY)

# Detecting contours in image.
contours, _= cv2.findContours(threshold, cv2.RETR_TREE,
							cv2.CHAIN_APPROX_SIMPLE)
print('all contours',len(contours))
cv2.imshow('image with threashold',threshold)
cv2.waitKey(0)
# Going through every contours found in the image.
for position,cnt in enumerate(contours) :
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
	# draws boundary of contours.
    cv2.drawContours(original_image, [approx], 0, (0, 0, 255), 1)

# 	# Used to flatted the array containing
# 	# the co-ordinates of the vertices.
    positions = approx.ravel()
    i = 0

    for j in positions :
        if(i % 2 == 0):
            x = positions[i]
            y = positions[i + 1]

            # String containing the co-ordinates.
            string = str(x) + " " + str(y)

            if(i == 0):
                # text on topmost co-ordinate.
                cv2.putText(original_image, "contour %d"%(position), (x, y),
                                font, 0.5, (255, 0, 0))
            else:
                # text on remaining co-ordinates.
                cv2.putText(original_image, string, (x, y),
                        font, 0.5, (0, 255, 0))
        i = i + 1

cv2.imshow('Original image', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
