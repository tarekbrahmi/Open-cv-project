import cv2
import numpy as np
	
Img = np.zeros((512, 512, 3), np.uint8)

window_name = 'Image'
center_coordinates = (Img.shape[1]//2, Img.shape[0]//2)
radius = 100
color = (255, 0, 0)
thickness = 1
image = cv2.circle(Img, center_coordinates, radius, color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
