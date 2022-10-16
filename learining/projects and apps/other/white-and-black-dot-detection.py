import cv2
import numpy as np
path = "black-white.jpg"

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByCircularity = True
params.minCircularity = 0.9

params.filterByConvexity = True
params.minConvexity = 0.2

params.filterByInertia = True
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)

image = cv2.imread(path, 0)

black_keypoints = detector.detect(image)
white_keypoints = detector.detect(cv2.bitwise_not(src=image))
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, white_keypoints, blank, (0, 0, 255),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


text = "white shape: " + str(len(white_keypoints))
cv2.putText(blobs, text, (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

blobs = cv2.drawKeypoints(blobs, black_keypoints, blank, (0, 255, 0),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

text_ = "black shape: " + str(len(black_keypoints))
cv2.putText(blobs, text_, (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

cv2.imshow("results", blobs)
cv2.waitKey(0)
