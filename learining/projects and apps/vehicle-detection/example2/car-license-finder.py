import cv2
import numpy as np
from skimage.filters import threshold_local
import imutils
from skimage import measure
path = "./test_videos/test1.mp4"
cap = cv2.VideoCapture(path)
fixed_width = 400
image = cv2.imread(path)


def sort_cont(character_contours):
    """
    To sort contours from left to right
    """
    i = 0
    boundingBoxes = [cv2.boundingRect(c) for c in character_contours]
    (character_contours, boundingBoxes) = zip(*sorted(zip(character_contours, boundingBoxes),
                                                      key=lambda b: b[1][i], reverse=False))
    return character_contours


def segment_chars(plate_img, fixed_width):
    """
    extract Value channel from the HSV format of image and apply adaptive thresholding
    to reveal the characters on the license plate
    """
    V = cv2.split(cv2.cvtColor(plate_img, cv2.COLOR_BGR2HSV))[2]

    T = threshold_local(V, 29, offset=15, method='gaussian')

    thresh = (V > T).astype('uint8') * 255

    thresh = cv2.bitwise_not(thresh)

    # resize the license plate region to a canoncial size
    plate_img = imutils.resize(plate_img, width=fixed_width)
    thresh = imutils.resize(thresh, width=fixed_width)
    bgr_thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

    # perform a connected components analysis and initialize the mask to store the locations
    # of the character candidates
    labels = measure.label(thresh, 8, 0)

    charCandidates = np.zeros(thresh.shape, dtype='uint8')

    # loop over the unique components
    characters = []
    for label in np.unique(labels):
        # if this is the background label, ignore it
        if label == 0:
            continue
        # otherwise, construct the label mask to display only connected components for the
        # current label, then find contours in the label mask
        labelMask = np.zeros(thresh.shape, dtype='uint8')
        labelMask[labels == label] = 255

        cnts = cv2.findContours(
            labelMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0]

        # ensure at least one contour was found in the mask
        if len(cnts) > 0:

            # grab the largest contour which corresponds to the component in the mask, then
            # grab the bounding box for the contour
            c = max(cnts, key=cv2.contourArea)
            # c = max([area for area in cv2.contourArea(cnts) if cnts !=0 ])
            (boxX, boxY, boxW, boxH) = cv2.boundingRect(c)

            # compute the aspect ratio, solodity, and height ration for the component
            aspectRatio = boxW / float(boxH)
            solidity = cv2.contourArea(c) / float(boxW * boxH)
            heightRatio = boxH / float(plate_img.shape[0])

            # determine if the aspect ratio, solidity, and height of the contour pass
            # the rules tests
            keepAspectRatio = aspectRatio < 1.0
            keepSolidity = solidity > 0.15
            keepHeight = heightRatio > 0.5 and heightRatio < 0.95

            # check to see if the component passes all the tests
            if keepAspectRatio and keepSolidity and keepHeight and boxW > 14:
                # compute the convex hull of the contour and draw it on the character
                # candidates mask
                hull = cv2.convexHull(c)

                cv2.drawContours(charCandidates, [hull], -1, 255, -1)

    contours, hier = cv2.findContours(
        charCandidates, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contours = sort_cont(contours)
        addPixel = 4  # value to be added to each dimension of the character
        for c in contours:
            (x, y, w, h) = cv2.boundingRect(c)
            if y > addPixel:
                y = y - addPixel
            else:
                y = 0
            if x > addPixel:
                x = x - addPixel
            else:
                x = 0
            temp = bgr_thresh[y:y + h +
                              (addPixel * 2), x:x + w + (addPixel * 2)]

            characters.append(temp)
        return characters
    else:
        return None


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

    def preValidateRatio(self, area, width, height):
        """
        validate plate side ratios and area
        """
        min_ratio = 3.5
        max_ratio = 5
        ratio = float(width)/float(height)
        if ratio < 1:
            ratio = 1/ratio
        return (ratio > min_ratio or ratio < max_ratio) or (area > self.min_area or area < self.max_area)

    def validateRatioAndArea(self, rect):
        """
        prepare possible plate to be preproccessed
        """
        (x, y), (width, height), rect_angle = rect
        if (height == 0 or width == 0):
            return False
        if (width > height) or width == height:
            return False
        if rect_angle < 70 or rect_angle > 95:
            return False
        area = width * height
        return self.preValidateRatio(area=area, width=width, height=height)

    def clean_up_plate(self, possible_plate):

        gray = cv2.cvtColor(possible_plate, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        contours, _ = cv2.findContours(
            thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours):
            areas = [cv2.contourArea(c) for c in contours]
            # index of the largest contour in the area array
            max_index = np.argmax(areas)
            max_cnt = contours[max_index]
            max_cntArea = areas[max_index]
            x, y, w, h = cv2.boundingRect(max_cnt)
            if self.preValidateRatio(area=max_cntArea, width=possible_plate.shape[1], height=possible_plate.shape[0]):
                return True, [x, y, w, h]
            else:
                False, None

    def check_plate(self, image_input, contour):
        """
            check if contour can be a plate 
        """
        # extract possible rectangle
        possible_rect = cv2.minAreaRect(contour)
        if self.validateRatioAndArea(rect=possible_rect):
            x, y, w, h = cv2.boundingRect(contour)
            possible_plate = image_input[y:y + h, x:x + w]
            cv2.imwrite('possible_platex%dy%d.png'%(x,y),possible_plate)
            plate_is_founded, coordinates = self.clean_up_plate(
                possible_plate=possible_plate)
            if plate_is_founded:
                chars_in_plate = segment_chars(
                    fixed_width=fixed_width, plate_img=possible_plate)
                if chars_in_plate != None and len(chars_in_plate) == 7:
                    return possible_plate, coordinates, chars_in_plate

        return None, None, None

    def find_possible_plates(self, image_input):
        """ 
        1. Now find the minimum area rectangle enclosed by each of the contours and validate their side ratios and area. We have defined the minimum and maximum area of the plate as 4500 and 30000 respectively.
        2.Now find the contours in the validated region and validate the side ratios and area of the bounding rectangle of the largest contour in that region. After validating you will get a perfect contour of a license plate. Now extract that contour from the original image
        """
        plates=[]
        self.preprocessed_image = self.preprocess_image(image_input)
        all_images_contours = self.getContours(
            preproccessed_image=self.preprocessed_image)
        for contour in all_images_contours:
            possible_plate, coordinates, chars_in_plate = self.check_plate(
                image_input=image_input, contour=contour)
            
            if chars_in_plate:
                plates.append(possible_plate)
            #     cv2.drawContours(image_input, [contour], 0, (0, 255, 0), 3)
        return plates
plateFinder = PlateFinder()
while True:
    # reads frames from a video
    ret, frames = cap.read()
    plateFinder.find_possible_plates(image_input=frames)
    cv2.imshow("Car license plate finder", cv2.resize(frames, (960, 540)))
    key = cv2.waitKey(1) & 0xFF
    if key == ord("x"):
        break
cv2.destroyAllWindows()
