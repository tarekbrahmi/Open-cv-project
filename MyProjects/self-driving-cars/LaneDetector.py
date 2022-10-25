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
        return cv2.Canny(blur_image, low_threshold, high_threshold)
