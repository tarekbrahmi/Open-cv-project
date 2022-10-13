import cv2

image = cv2.imread('contours2.jpg')


# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(image=edged,
                                       mode=cv2.RETR_EXTERNAL,
                                       method=cv2.CHAIN_APPROX_NONE)


print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image=image, contours=contours,
                 contourIdx=-1, color=(0, 255, 0), thickness=3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
