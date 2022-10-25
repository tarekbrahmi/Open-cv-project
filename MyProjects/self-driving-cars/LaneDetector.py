import cv2
import numpy as np


class LaneDetector:
    """
     Lane detector from video
    """

    def __init__(self) -> None:
        pass

    def prePreoccess(self, frame):
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

    def laneFinder(self, frame, original):
        """ 
        find and drow lines in frame
        Probabilistic Hough Line Transform
        """
        frame = self.prePreoccess(frame=frame)
        # black mask
        mask = np.zeros_like(frame)
        # polygone point (region of intrest)
        vertices = np.array(
            [[(0, 539), (350, 270), (461, 231), (627, 256), (959, 539)]], dtype=np.int32)
        cv2.circle(img=original, center=(0, 539), radius=1,
                   color=(0, 0, 255), thickness=2)
        cv2.circle(img=original, center=(350, 270),
                   radius=1, color=(0, 0, 255), thickness=2)
        cv2.circle(img=original, center=(461, 231),
                   radius=1, color=(0, 0, 255), thickness=2)

        cv2.circle(img=original, center=(627, 256),
                   radius=1, color=(0, 0, 255), thickness=2)
        cv2.circle(img=original, center=(959, 539),
                   radius=1, color=(0, 0, 255), thickness=2)

        cv2.fillPoly(mask, vertices, 255)
        # applay the mask to prevent other line (not in regionof intrest) of detection
        new_frame = cv2.bitwise_and(mask, frame)
        
        # draw lines of lane
        lines = cv2.HoughLinesP(
            new_frame,  # Input edge image
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
