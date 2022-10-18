import cv2
import numpy as np
from skimage.filters import threshold_local
import imutils
from skimage import measure
path = "./test_videos/blurred.jpg"
fixed_width = 400
image = cv2.imread(path)


def find_and_drow_contours(image):
    # Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Find Canny edges
    edged = cv2.Canny(gray, 30, 200)
    contours, _ = cv2.findContours(
        edged, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image=image, contours=contours,
                     contourIdx=-1, color=(0, 255, 0), thickness=1)


class PlateFinder:
    def __init__(self) -> None:
        self.min_area = 4000  # min plate area
        self.max_area = 30000  # max plate area
        self.element_structure = cv2.getStructuringElement(
            shape=cv2.MORPH_RECT, ksize=(22, 3))  # we define plate like a rectangle

    def preprocess_image(self, image_input):
        """
            1. To reduce the noise we need to blur the input Image with Gaussian Blur and then convert it to grayscale.
            2. Find vertical edges in the image.
            3. To reveal the plate we have to binarize the image. For this apply Otsu’s Thresholding on the vertical edge image. In other thresholding methods, we have to choose a threshold value to binarize the image but Otsu’s Thresholding determines the value automatically.
            4.Apply Closing Morphological Transformation on the thresholded image. Closing is useful to fill small black regions between white regions in a thresholded image. It reveals the rectangular white box of license plates.
        """
        # blur image with gaussian blur
        gussian_blur = cv2.GaussianBlur(
            src=image_input, ksize=(7, 7), sigmaX=0)
        # convert image to gray
        image_gray = cv2.cvtColor(src=gussian_blur, code=cv2.COLOR_BGR2GRAY)
        # get vertical edges
        vertical_edges = cv2.Sobel(
            src=image_gray, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=3)
        # binarize the image
        _, threash = cv2.threshold(
            src=vertical_edges, thresh=0, maxval=255, type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        image_copy = threash.copy()
        # applay closing morphology
        cv2.morphologyEx(
            src=threash, kernel=self.element_structure, op=cv2.MORPH_CLOSE, dst=image_copy)
        # cv2.imshow('Image PreProcessing', cv2.resize(image_copy, (960, 540)))
        return image_copy

    def getContours(self, preproccessed_image):
        contours, _ = cv2.findContours(
            image=preproccessed_image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
        return contours

    def find_possible_plates(self, image_input):
        """ 
        1. Now find the minimum area rectangle enclosed by each of the contours and validate their side ratios and area. We have defined the minimum and maximum area of the plate as 4500 and 30000 respectively.
        2.Now find the contours in the validated region and validate the side ratios and area of the bounding rectangle of the largest contour in that region. After validating you will get a perfect contour of a license plate. Now extract that contour from the original image
        """
        self.preprocessed_image = self.preprocess_image(image_input)
        find_and_drow_contours(image=image_input)  # for testing


plateFinder = PlateFinder()
# plateFinder.find_possible_plates(image_input=cv2.resize(image, (960, 540)))
find_and_drow_contours(image=image)  # for testing
cv2.imshow("Car license plate finder", cv2.resize(image, (960, 540)))

cv2.waitKey(0)
cv2.destroyAllWindows()
