import cv2
import numpy as np


def get_background(file_path):
    """
        After calculation, this function will return the background model of the video
    """
    cap = cv2.VideoCapture(file_path)
    # we will randomly select 20 frames for the calculating the median
    frame_indices = cap.get(cv2.CAP_PROP_FRAME_COUNT) * \
        np.random.uniform(size=20)
    # we will store the frames in array
    frames = []
    for idx in frame_indices:
        # set the frame id to read that particular frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        _, frame = cap.read()
        frames.append(frame)
    # calculate the median
    median_frame = np.median(frames, axis=0).astype(np.uint8)
    # cv2.imshow("median background", median_frame)
    return median_frame
