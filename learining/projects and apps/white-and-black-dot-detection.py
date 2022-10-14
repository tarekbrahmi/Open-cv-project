import cv2
path = "black-white.jpg"

# reading the image in grayscale mode
gray = cv2.imread(path, 0)
image = cv2.imread(path)
# threshold
th, threshed_white = cv2.threshold(gray, 100, 255,
                                   cv2.THRESH_BINARY | cv2.THRESH_OTSU)

th, threshed_black = cv2.threshold(gray, 100, 255,
                                   cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
# findcontours
cnts_white = cv2.findContours(threshed_white, cv2.RETR_LIST,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]
cnts_black = cv2.findContours(threshed_black, cv2.RETR_LIST,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]
# filter by area .. black and white dots have same area
s1 = 1
s2 = 3
xcnts_white = []
xcnts_black = []

cv2.drawContours(image=image, contours=cnts_white,
                contourIdx=-1, color=(0, 255, 0), thickness=3)
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
for cnt in cnts_white:
    if s1 < cv2.contourArea(cnt) and cv2.contourArea(cnt)  < s2:
        xcnts_white.append(cnt)
for cnt in cnts_black:
    if s1 < cv2.contourArea(cnt) and cv2.contourArea(cnt) < s2:
        xcnts_black.append(cnt)
# printing output
print("\n(White:%d Black:%d) " % (len(cnts_white), len(cnts_black)))
