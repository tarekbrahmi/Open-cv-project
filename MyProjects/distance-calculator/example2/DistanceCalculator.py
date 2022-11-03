import numpy as np
import imutils
import cv2
# helpers


def inch2cm(inch_val):
    """ 1 inch = 2.54 cm"""
    return inch_val*2.54


def cm2inch(cm_val):
    """ 1 cm = 0.393700787 inch """
    return cm_val*0.393700787


def ft2cm(ft_val):
    """ 1 ft = 30.48 cm """
    return ft_val*30.48


def cm2ft(cm_val):
    """ 1 cm = 0.032808399 ft """
    return cm_val*0.032808399


class DistanceCalculator:
    def __init__(self, distance_ref, width_ref, pixels):
        self.distance_ref = distance_ref
        self.width_ref = width_ref
        self.focal_ref = (pixels*distance_ref)/width_ref

    def find_object(self, original):
        """ 

        find object that went to calculate camera-object distance 

        we can applay a mask to take only region of intrest
        but here we applay only max contour detection
        """

        # convert the image to grayscale, blur it, and detect edges
        gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 35, 125)

        # find the contours in the edged image and keep the largest one
        cnts = cv2.findContours(
            edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cv2.drawContours(original, cnts, -1, (0, 0, 255))
        if len(cnts):
            c = max(cnts, key=cv2.contourArea)
            return cv2.minAreaRect(c)
        else:
            return (0, 0), (self.width_ref, 0), 0

    def _calc_distance(self, pixels):
        """ real distance"""
        return (self.width_ref*self.focal_ref)/pixels

    def calc_distance(self, original):
        """ calculate camera-object distance """
        # applay rectangle max area filter and draw contours
        (x, y), (width, height), angle = self.find_object(original=original)
        print("distance %d" % self._calc_distance(width))
