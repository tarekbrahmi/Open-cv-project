import cv2
path = r'./draw-line.png'
image = cv2.imread(path)
window_name = 'Draw arrowed line at an image'
start_point = (0, 0)
end_point = (image.shape[1], image.shape[0]-10)
color = (0, 255, 0)
thickness = 1
image = cv2.arrowedLine(image, start_point, end_point,
									color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)