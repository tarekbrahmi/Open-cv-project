import cv2
import numpy as np


def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
    left_lines = []  # m=+ve
    right_lines = []  # m=-ve
    postiveSlope = 0  # +veSlopeSUM
    negtiveSlope = 0  # -veSlopeSUM
    for line in lines:
        for x1, y1, x2, y2 in line:
            if (y2-y1)/(x2-x1) < 0.2 and (y2-y1)/(x2-x1) > -0.8:
                left_lines.append(line)
                postiveSlope += ((y2-y1)/(x2-x1))
            elif (y2-y1)/(x2-x1) > 0.2 and (y2-y1)/(x2-x1) < 0.8:
                right_lines.append(line)
                negtiveSlope += abs((y2-y1)/(x2-x1))

        for x1_avg, y1_avg, x2_avg, y2_avg in line:
            x1 = x1_avg
            y1 = y1_avg
            x2 = x2_avg
            y2 = y2_avg
            LL_slope_avg = (y2 - y1)/(x2 - x1)+1
            LL_Intercept_avg = y1 - (LL_slope_avg * x1)
            x1 = x1_avg
            y1 = y1_avg
            x2 = x2_avg
            y2 = y2_avg
            RL_slope_avg = (y2 - y1)/(x2 - x1)-1
            RL_Intercept_avg = y1 - (RL_slope_avg * x1)

    min_left_y = find_minimum_y(left_lines)
     #affecting right line
    min_left_x = calculate_x(min_left_y, LL_Intercept_avg, LL_slope_avg)

    min_right_y = find_minimum_y(right_lines)
    min_right_x = calculate_x(min_right_y, RL_Intercept_avg, RL_slope_avg)


    max_left_y = find_maximum_y(left_lines)
    max_left_x = 502

    max_right_y = find_maximum_y(right_lines)
    # calculate_x(max_right_y,RL_Intercept_avg, RL_slope_avg)
    max_right_x = 465

#   left_lane_lines drawn:  ==================
    cv2.line(img, (min_left_x, min_left_y),
             (max_left_x, max_left_y), [255, 255, 0], thickness=thickness)
#   right_lane_lines drawn  ==================
    cv2.line(img, (min_right_x, min_right_y),
             (max_right_x, max_right_y), [0, 0, 255], thickness=thickness)


def weighted_img(initial_img, img, α=0.1, β=0.9, λ=0.):
    return cv2.addWeighted(img, α, initial_img, β, λ)


def calculate_x(y, intercept, slope):
    x = ((y-intercept)//slope)
    return int(x)


def find_minimum_y(lane_lines):
    temp = 960
    temp1 = 960
    for line in lane_lines:
        for _, y1, _, y2 in line:
            if temp >= y1:
                temp = y1
            if temp1 >= y2:
                temp1 = y2
    if temp < temp1:
        min_y = temp
    else:
        min_y = temp1
    return int(min_y)


def find_maximum_y(lane_lines):
    temp = 0
    temp1 = 0
    for line in lane_lines:
        for _, y1, _, y2 in line:
            if temp <= y1:
                temp = y1
            if temp1 <= y2:
                temp1 = y2
    if temp > temp1:
        max_y = temp
    else:
        max_y = temp1
    return int(max_y)


class LaneDetector:
    """
     Lane detector from video
    """

    def __init__(self) -> None:
        pass

    def hough_lines(self, new_frame, rho, theta, threshold, min_line_len, max_line_gap):
        lines = cv2.HoughLinesP(new_frame, rho, theta, threshold, np.array(
            []), minLineLength=min_line_len, maxLineGap=max_line_gap)
        line_img = np.zeros(
            (new_frame.shape[0], new_frame.shape[1], 3), dtype=np.uint8)
        draw_lines(line_img, lines)
        return line_img

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
            [[(0, mask.shape[1]), (350, 270), (461, 231), (627, 256), (mask.shape[0], mask.shape[1])]], dtype=np.int32)
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
        rho = 1
        theta = np.pi/180
        threshold = 12
        min_line_len = 10
        max_line_gap = 2
        # --> will call draw lines & you get a Blacked-out image with connected Hough returned coordinates.
        line_img = self.hough_lines(new_frame, rho, theta,
                                    threshold, min_line_len, max_line_gap)
        output = weighted_img(line_img, original, α=0.5, β=1.0, λ=0.)
        cv2.imshow('OUTPUT', output)

        # contours, _ = cv2.findContours(image=new_frame,
        #                                mode=cv2.RETR_EXTERNAL,
        #                                method=cv2.CHAIN_APPROX_NONE)

        # def filter_with_area(contour):
        #     (x, y), (width, height), angle = cv2.minAreaRect(contour)
        #     print("angle is", angle)
        #     return width*height > 800
        # contours = list(
        #     filter(lambda contour: filter_with_area(contour=contour), contours))
        # print("Number of Contours found = " + str(len(contours)))
        # self.draw_contours(contours=contours, original=original)
        # lines = cv2.HoughLinesP(
        #     new_frame,  # Input edge image
        #     1,  # Distance resolution in pixels
        #     np.pi/180,  # Angle resolution in radians
        #     threshold=100,  # Min number of votes for valid line
        #     minLineLength=50,  # Min allowed length of line
        #     maxLineGap=10  # Max allowed gap between line for joining them
        # )
        # # draw lines of lane
        # self.draw_lines(lines=lines, original=original)

    def draw_contours(self, contours, original):
        cv2.drawContours(image=original, contours=contours,
                         contourIdx=-1, color=(0, 255, 0), thickness=3)

    def draw_lines(self, lines, original):
        """
        draw left or rigth line based in line slope
        remove othe unused lines from region of intrest
        """
        left_lines = []
        right_lines = []
        if type(lines) != type(None):
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(original, (x1, y1), (x2, y2), (0, 255, 0), 2)
                for x1, y1, x2, y2 in line:
                    slope = (y2-y1)//(x2-x1)
                    if slope >= 0:
                        # right
                        right_lines.append(line)
                    else:
                        left_lines.append(line)

        # print(np.average(left_lines, axis=0), np.average(right_lines, axis=0))
        # avg_left, avg_right = np.average(
        #     left_lines, axis=0), np.average(right_lines, axis=0)
        # if not np.isnan(avg_right).all():
        #     avg_right = avg_right.astype(int)
        #     _x1, _y1, _x2, _y2 = tuple(avg_right[0])
        #     cv2.line(original, (_x1, _y1), (_x2, _y2), (0, 255, 0), 2)

        # if not np.isnan(avg_left).all():
        #     avg_left = avg_left.astype(int)
        #     _x1, _y1, _x2, _y2 = tuple(avg_left[0])
        #     cv2.line(original, (_x1, _y1), (_x2, _y2), (0, 255, 255), 2)
