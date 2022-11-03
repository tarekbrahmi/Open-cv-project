from DistanceCalculator import DistanceCalculator
from VideoStreamer import RealTimeVideoStreamer
from FaceRecognizer import FaceRecognizer


if __name__ == "__main__":
    face_rec = FaceRecognizer()
    # face_rec.preproccess()
    (images, labels, names) = face_rec.proccess()
    face_rec.train(images=images, labels=labels)
    if face_rec.model != None:
        distance_calculator = DistanceCalculator(
            face_rec=face_rec, names=names)
        RealTimeVideoStreamer(distance_calculator=distance_calculator).execute(
            applay_delay=True)
    else:
        print('no model')
