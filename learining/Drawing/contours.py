import cv2

image = cv2.imread('contours2.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 30, 200)
contours, hierarchy = cv2.findContours(image=edged,
                                       mode=cv2.RETR_EXTERNAL,
                                       method=cv2.CHAIN_APPROX_NONE)


print("Number of Contours found = " + str(len(contours)))
cv2.drawContours(image=image, contours=contours,
                 contourIdx=-1, color=(0, 255, 0), thickness=3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
