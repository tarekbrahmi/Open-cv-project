import cv2
import numpy as np
import argparse

# Frame Width & Height
FRAME_WIDTH = 640
FRAME_HEIGHT = 490


class DST:
    CLAHE = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    vidCapture = None

    def __init__(self, video_path, consecutive_frame):
        self.__init_video_capture(
            video_path, frame_w=FRAME_WIDTH, frame_h=FRAME_HEIGHT)
        self.background = self.get_background()
        self.consecutive_frame = consecutive_frame

    def __init_video_capture(self, video_path: str, frame_w: int, frame_h: int):
        self.vidCapture = cv2.VideoCapture(video_path)
        self.vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH, frame_w)
        self.vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_h)

    def read_frame(self) -> np.ndarray:
        ret, frame = self.vidCapture.read()
        # frame = cv2.resize(src=frame, dsize=(960, 540))
        return ret, frame

    def get_background(self,  size=20):
        """
        After calculation, this function will return the background model of the video
        """
        cap = self.vidCapture
        frame_indices = cap.get(cv2.CAP_PROP_FRAME_COUNT) * \
            np.random.uniform(size=size)
        frames = []
        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            _, frame = cap.read()
            frames.append(frame)
        # calculate the median
        median_frame = np.median(frames, axis=0).astype(np.uint8)
        # cv2.imshow("median background", median_frame)
        background = cv2.cvtColor(median_frame, cv2.COLOR_BGR2GRAY)
        # background = cv2.resize(src=background, dsize=(960, 540))
        return background

    def execute(self, wait_key_delay=33, quit_key='q'):
        frame_cnt = 0
        while cv2.waitKey(delay=wait_key_delay) != ord(quit_key) and self.vidCapture.isOpened():
            ret, frame = self.read_frame()
            if ret == True:
                frame_cnt += 1
                orig_frame = frame.copy()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                if frame_cnt % self.consecutive_frame == 0 or frame_cnt == 1:
                    frame_diff_list = []

                frame_diff = cv2.absdiff(gray, self.background)
                _, thres = cv2.threshold(
                    frame_diff, 50, 255, cv2.THRESH_BINARY)
                dilate_frame = cv2.dilate(thres, None, iterations=2)
                frame_diff_list.append(dilate_frame)

                if len(frame_diff_list) == self.consecutive_frame:
                    sum_frames = sum(frame_diff_list)
                    contours, _ = cv2.findContours(
                        sum_frames, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    for contour in contours:
                        if cv2.contourArea(contour) < 500:
                            continue
                        (x, y, w, h) = cv2.boundingRect(contour)
                        # draw the bounding boxes
                        cv2.rectangle(orig_frame, (x, y),
                                      (x+w, y+h), (0, 255, 0), 2)

                    cv2.imshow('Detected Objects', orig_frame)
        cv2.destroyAllWindows()
        self.vidCapture.release()


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='path to the input video',
                    required=True)
parser.add_argument('-c', '--consecutive-frames', default=4, type=int,
                    dest='consecutive_frames', help='number of consecutive frames')
if __name__ == "__main__":
    args = vars(parser.parse_args())
    video_path = args["input"]
    consecutive_frame = args['consecutive_frames']
    DST(video_path=video_path, consecutive_frame=consecutive_frame).execute()
