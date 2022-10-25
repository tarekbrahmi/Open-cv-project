import cv2
import numpy as np


class LaneDetector:
    """
     Lane detector from video
    """

    def __init__(self) -> None:
        pass

    def laneFinder(self, frame):
        # applay grayscale image
        gray_image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # applay Gaussian Noise kernel
        kernel_size = 5
        blur_image = cv2.GaussianBlur(
            gray_image, (kernel_size, kernel_size), 0)

        # applay Canny transformation
        low_threshold, high_threshold = 70, 140
        # get vertical edges
        vertical_edges = cv2.Sobel(
            src=blur_image, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=3)
        return cv2.Canny(vertical_edges, low_threshold, high_threshold, apertureSize=3)

    def prePreoccess(self, frame,original):
        """ 
        find and drow lines in frame
        """
        lines = cv2.HoughLinesP(
            frame,  # Input edge image
            1,  # Distance resolution in pixels
            np.pi/180,  # Angle resolution in radians
            threshold=100,  # Min number of votes for valid line
            minLineLength=5,  # Min allowed length of line
            maxLineGap=10  # Max allowed gap between line for joining them
        )
        if len(lines):
            for points in lines:
                # Extracted points nested in the list
                x1, y1, x2, y2 = points[0]
                # Draw the lines joing the points
                # On the original image
                cv2.line(original, (x1, y1), (x2, y2), (0, 255, 0), 2)
