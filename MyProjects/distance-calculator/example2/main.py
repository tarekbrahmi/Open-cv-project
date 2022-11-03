"""
    Find distance from camera to object using Python and OpenCV
    Triangle Similarity for Object/Marker to Camera Distance
    camera caractr
        Webcam Name:	HP Webcam-101
        Quality Rating:	71
        Built-in Microphone:	None
        Built-in Speaker:	None
        Frame rate:	8 FPS
        Stream Type:	video
        Image Mode:	rgb
        Webcam MegaPixels:	0.31 MP
        Webcam Resolution:	640×480
        Video Standard:	VGA
        Aspect Ratio:	1.33
        PNG File Size:	456.73 kB
        JPEG File Size:	260.46 kB
        Bitrate:	2.11 MB/s
        Number of Colors:	80563
        Lightness:	72.16%
        Luminosity:	71.98%
        Brightness:	72.03%
        Hue:	15°
        Saturation:	2.82%        
"""
from DistanceCalculator import DistanceCalculator
from VideoStreamer import RealTimeVideoStreamer


if __name__ == "__main__":
    distance_ref, width_ref, pixels = 12, 3, 20 # en cm
    distance_calculator = DistanceCalculator(distance_ref, width_ref, pixels)
    RealTimeVideoStreamer(distance_calculator=distance_calculator).execute(
        applay_delay=False)
