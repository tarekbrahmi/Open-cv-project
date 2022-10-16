import cv2
import random
import numpy as np
imgResult = cv2.imread("image-test.png")
clone = imgResult.copy()
save = False
colors = [[51, 153, 255],
          [255, 0, 255],
          [0, 255, 0],
          [255, 0, 0],
          [0, 0, 255]]

color = random.choice(colors)

def draw_event(event, x, y):
    global save, imgResult, color
    if event == cv2.EVENT_LBUTTONDOWN and ~save:
        save = True
    if event == cv2.EVENT_LBUTTONUP:
        save = False
        color = random.choice(colors)
    if (save):
        cv2.circle(imgResult, (x, y), 4, color, cv2.FILLED)
        imgHSV = cv2.cvtColor(imgResult, cv2.COLOR_BGR2HSV)
        # lower boundary RED color range values; Hue (0 - 10)
        lower1 = np.array([0, 100, 20])
        upper1 = np.array([10, 255, 255])

        # upper boundary RED color range values; Hue (160 - 180)
        lower2 = np.array([160, 100, 20])
        upper2 = np.array([179, 255, 255])

        lower_mask = cv2.inRange(imgHSV, lower1, upper1)
        upper_mask = cv2.inRange(imgHSV, lower2, upper2)

        full_mask = lower_mask + upper_mask
        contours, _ = cv2.findContours(full_mask, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.2 * cv2.arcLength(cnt, True), True)
            cv2.drawContours(imgResult, [approx], 0, (0, 255, 5), 1)
        cv2.imshow('Drawing', imgResult)


while True:
    cv2.imshow("Drawing", imgResult)
    cv2.setMouseCallback('Drawing', draw_event)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):
        imgResult = clone.copy()
    elif key == ord("x"):
        break
cv2.destroyAllWindows()
