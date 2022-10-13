import numpy as np
import cv2

field_threshold = {"Hello": 0.3}

# Function to Generate bounding
# boxes around detected fields


def getBoxed(img, img_gray, template, field_name="Hello"):

    w, h = template.shape[::-1]

    # Apply template matching
    res = cv2.matchTemplate(img_gray, template,
                            cv2.TM_CCOEFF_NORMED)
    hits = np.where(res >= field_threshold[field_name])
    # Draw a rectangle around the matched region.
    for pt in zip(*hits[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),
                      (0, 255, 255), 2)

        y = pt[1] - 10 if pt[1] - 10 > 10 else pt[1] + h + 20

        cv2.putText(img, field_name, (pt[0], y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1)

    return img


# Driver Function
if __name__ == '__main__':

    # Read the original document image
    img = cv2.imread('./doc.jpg')

    # 3-d to 2-d conversion
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Field templates
    template_greeting = cv2.imread('./greeting.jpg', 0)

    img = getBoxed(img.copy(), img_gray.copy(),
                   template_greeting, 'Hello')

    cv2.imshow('Detected', img)
    cv2.waitKey(0)
