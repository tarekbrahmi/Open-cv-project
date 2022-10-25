import cv2
import numpy as np
from LaneDetector import LaneDetector

# Color RGB Codes & Font
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (255, 255, 104)
FONT = cv2.QT_FONT_NORMAL

# Frame Width & Height
FRAME_WIDTH = 640
FRAME_HEIGHT = 490
VIDEO_PATH = "./test_videos/test_video.mp4"


class RealTimeVideoStreamer:
    """
    RealTimeVideoStreamer : stream video 
    """
    CLAHE = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    vidCapture = None

    def __init__(self, lane_detector: LaneDetector):
        self.__init_video_capture(
            video_path=VIDEO_PATH, frame_w=FRAME_WIDTH, frame_h=FRAME_HEIGHT)
        self.lane_detector = lane_detector

    def __init_video_capture(self, video_path: str, frame_w: int, frame_h: int):
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
                frame = cv2.resize(src=frame, dsize=(960, 540))
                if applay_delay:
                    frame_cnt += 1
                    if frame_cnt % (frame_period_s * 10) == 0:
                        # here we can applay plate finder
                        frame_cnt = 0
                        frame = self.lane_detector.laneFinder(frame=frame)
                        print('we can execute lane detector with delay')
                else:
                    frame = self.lane_detector.laneFinder(frame=frame)
                    print('we can execute lane detector')
                cv2.imshow('Lane Detection', frame)
        cv2.destroyAllWindows()
        self.vidCapture.release()
