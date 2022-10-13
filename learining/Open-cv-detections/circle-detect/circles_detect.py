import cv2
import numpy as np

# Load image
image = cv2.imread('./area-cercles.jpg', 0)

# Set our filtering parameters
# Initialize parameter setting using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters ... to avoid point detection
params.filterByArea = True
params.minArea = 100

# Set Circularity filtering parameters .. to detect circles
params.filterByCircularity = True
params.minCircularity = 0.9

# Set Convexity filtering parameters ... to get complete circled shape
params.filterByConvexity = True
params.minConvexity = 0.2

# Set inertia filtering parameters ... to avoid elipse detections
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)
print("keypoints", keypoints)
# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular shape: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imwrite("./FiltredCircles.jpg", blobs)
