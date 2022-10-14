"""
    Histogram Calculation
        images : 
            it is the source image of type uint8 or float32 represented as “[img]”.
        channels : 
            it is the index of channel for which we calculate histogram. 
            For grayscale image, its value is [0] and 
            color image, you can pass [0], [1] or [2] to calculate histogram of 
            blue, green or red channel respectively.
        mask : 
            mask image. To find histogram of full image, it is given as “None”.
        histSize : 
            this represents our BIN count. For full scale, we pass [256].
        ranges : 
            this is our RANGE. Normally, it is [0,256].
"""
import cv2
import matplotlib.pyplot as plt
# gray scale image
image = cv2.imread('./icons.jpg', 0)
# calculate frequency of pixels in range 0-255
histogram = cv2.calcHist(
    images=[image],
    channels=[0],
    mask=None,
    histSize=[256],
    ranges=[0, 256]
)

# show the plotting graph of an image
plt.plot(histogram)
plt.show()
