import cv2
import numpy as np
from DistanceCalculator import DistanceCalculator


# Frame Width & Height
FRAME_WIDTH = 640
FRAME_HEIGHT = 490
VIDEO_PATH = 0


class RealTimeVideoStreamer:
    """
    RealTimeVideoStreamer : stream video 
    """
    CLAHE = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    vidCapture = None

    def __init__(self, distance_calculator: DistanceCalculator):
        self.__init_video_capture(
            video_path=VIDEO_PATH, frame_w=FRAME_WIDTH, frame_h=FRAME_HEIGHT)
        self.distance_calculator = distance_calculator

    def __init_video_capture(self, video_path: int, frame_w: int, frame_h: int):
        self.vidCapture = cv2.VideoCapture(video_path)
        self.vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH, frame_w)
        self.vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_h)

    def read_frame(self) -> np.ndarray:
        ret, frame = self.vidCapture.read()
        return ret, frame

    def execute(self, wait_key_delay=33, quit_key='q', frame_period_s=0.2, applay_delay=True):
        frame_cnt = 0
        while cv2.waitKey(delay=wait_key_delay) != ord(quit_key) and self.vidCapture.isOpened():
            ret, frame = self.read_frame()
            if ret == True:
                original_image = frame.copy()
                frame = cv2.resize(src=frame, dsize=(960, 540))
                original_image = cv2.resize(
                    src=original_image, dsize=(960, 540))
                if applay_delay:
                    frame_cnt += 1
                    if frame_cnt % (frame_period_s * 10) == 0:
                        frame_cnt = 0
                        print('we can execute distance calculator with delay')

                else:
                    print('we can execute distance calculator')
                cv2.imshow('Original', original_image)
        cv2.destroyAllWindows()
        self.vidCapture.release()
