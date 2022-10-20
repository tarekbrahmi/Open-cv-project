# Frame Differencing and Summing Technique

Frame Differencing and Summing Technique (DST for short) is a very simple yet effective computer vision technique. We can use it to know whether there are any moving objects in a video or not.

We know that a video consists of multiple consecutive frames. And these frames are made up of pixels which consist of colors ( ***red, green, and blue*** ). And these pixels are just values in the range of 0 to 255. 0 is completely black and 255 is white.

So, suppose that we take any two consecutive frames from a video. Now, let’s subtract the current frame from the previous frame. If they contain the same information (RGB color values), then the resulting frame will be completely black. But if the current frame consists of some newer information or pixel values, then we will see some sort of white patches after the subtraction. This tells us that something in the video has moved or changed position. This is a very simple concept. Yet we will use this as the basis for moving object detection in videos.

# **CLAHE (Contrast Limiting Adaptive Histogram Equalization)**

Adaptive Histogram Equalization

* Histogram equalization is one of the tools we have for image pre-processing and it makes image thresholding or segmentation tasks easier.
* The reason we need histogram equalization is that when we collect images that are washed out or images with low contrast, we can stretch the histogram to span the entire range.

>  Contrast Limited AHE ( **CLAHE** ) is a variant of adaptive histogram equalization in which the contrast amplification is limited, so as to reduce this problem of noise amplification. In simple words, CLAHE does histogram equalization in small patches or in small tiles with high accuracy and contrast limiting.
