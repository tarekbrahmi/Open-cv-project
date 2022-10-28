import cv2
# Color RGB Codes & Font
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (255, 255, 104)
FONT = cv2.QT_FONT_NORMAL
HAARCASCADE_PATH = "haarcascade_frontalface_default.xml"


class DistanceCalculator:
    FACE_WIDTH = 0

    def __init__(self) -> None:
        self.face_detector = cv2.CascadeClassifier(HAARCASCADE_PATH)

    def face_ref_width(self, original):
        """ detect and draw green rectangle in face"""
        gray_scaled = cv2.cvtColor(src=original, code=cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray_scaled, 1.3, 5)
        for (x, y, h, w) in faces:
            cv2.rectangle(img=original, pt1=(x, y), pt2=(
                x+w, y+h), color=GREEN_COLOR, thickness=2)
            self.FACE_WIDTH = w

    def calc_distance(self, original):
        self.face_ref_width(original=original)

    def preproccess(self):

        pass
