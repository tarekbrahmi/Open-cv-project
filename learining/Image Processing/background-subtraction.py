"""
Background Subtraction 
    has several use cases in everyday life, It is being used for object segmentation, security enhancement, pedestrian tracking, counting the number of visitors, 
    number of vehicles in traffic etc. It is able to learn and identify the foreground mask.
"""
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
	ret, frame = cap.read()

	fgmask = fgbg.apply(frame)

	cv2.imshow('fgmask', fgmask)
	cv2.imshow('frame',frame )

	
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
	

cap.release()
cv2.destroyAllWindows()
