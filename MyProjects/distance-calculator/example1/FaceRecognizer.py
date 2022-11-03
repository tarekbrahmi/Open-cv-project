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
        self.path = os.path.join(self.datasets_folder_path, self.sub_data)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def train(self, images, labels):
        """ train model from dataset"""
        self.model = cv2.face.LBPHFaceRecognizer_create()
        print('labels,images', len(labels), len(images))
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
        return (images, labels, names)

    def preproccess(self):
        """prepare images like dataset"""
        counter = 0
        webcam = cv2.VideoCapture(0)
        while counter < 30:
            (_, im) = webcam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (self.width, self.height))
                cv2.imwrite('% s/% s.png' %
                            (self.path, counter), face_resize)
            counter += 1
            cv2.imshow('OpenCV', im)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
