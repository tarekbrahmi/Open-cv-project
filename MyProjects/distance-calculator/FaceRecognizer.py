import cv2
import os
import numpy


class FaceRecognizer:
    haar_file_path = 'haarcascade_frontalface_default.xml'
    datasets_folder_path = 'datasets'
    sub_data = 'MY_FACE'
    (width, height) = (130, 100)
    model = None

    def __init__(self) -> None:
        self.face_cascade = cv2.CascadeClassifier(self.haar_file_path)
        self.webcam = cv2.VideoCapture(0)
        self.counter = 0
        self.path = os.path.join(self.datasets_folder_path, self.sub_data)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def train(self):
        """ train model from dataset"""
        images, labels = self.proccess()
        self.model = cv2.face.LBPHFaceRecognizer_create()
        self.model.train(images, labels)

    def proccess(self):
        """prepared data and labels to trained """
        (images, labels, names, id) = ([], [], {}, 0)
        for (subdirs, dirs, files) in os.walk(self.datasets_folder_path):
            for subdir in dirs:
                names[id] = subdir
                subjectpath = os.path.join(self.datasets_folder_path, subdir)
                for filename in os.listdir(subjectpath):
                    path = subjectpath + '/' + filename
                    label = id
                    images.append(cv2.imread(path, 0))
                    labels.append(int(label))
                id += 1
        (images, labels) = [numpy.array(lis) for lis in [images, labels]]
        return (images, labels)

    def preproccess(self):
        """prepare images like dataset"""
        while self.counter < 30:
            (_, im) = self.webcam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (self.width, self.height))
                cv2.imwrite('% s/% s.png' %
                            (self.path, self.counter), face_resize)
            self.counter += 1
            cv2.imshow('OpenCV', im)
