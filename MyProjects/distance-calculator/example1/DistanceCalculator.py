import cv2
# Color RGB Codes & Font
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (255, 255, 104)
FONT = cv2.QT_FONT_NORMAL
HAARCASCADE_PATH = "haarcascade_frontalface_default.xml"


class DistanceCalculator:
    FACE_WIDTH = 0
    REF_FACE_WIDTH = 14  # face width
    REF_FACE_DISTANCE = 20  # face-webcam distance
    (width, height) = (130, 100)

    def focal_ref(self, width_image_ref):
        return (width_image_ref * self.REF_FACE_DISTANCE) / self.REF_FACE_WIDTH

    def focal_real(self, width_image_real):

        return (width_image_real * self.REF_FACE_DISTANCE) / self.REF_FACE_WIDTH

    def __init__(self, face_rec, names) -> None:
        self.face_detector = cv2.CascadeClassifier(HAARCASCADE_PATH)
        self.model = face_rec.model
        self.names = names

    def face_real_width(self, original):
        """ detect and draw green rectangle in face"""
        gray_scaled = cv2.cvtColor(src=original, code=cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray_scaled, 1.3, 5)

        for (x, y, h, w) in faces:
            cv2.rectangle(original, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray_scaled[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (self.width, self.height))
            # Try to recognize the face
            prediction = self.model.predict(face_resize)
            cv2.rectangle(original, (x, y), (x + w, y + h), (0, 255, 0), 3)

            if prediction[1] < 500:
                cv2.putText(original, '% s - %.0f' %
                            (self.names[prediction[0]],
                             prediction[1]), (x-10, y-10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                self.FACE_WIDTH = w
            else:
                cv2.putText(original, 'not recognized',
                            (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

    def calc_distance(self, original):
        self.face_real_width(original=original)

    def preproccess(self):

        pass
