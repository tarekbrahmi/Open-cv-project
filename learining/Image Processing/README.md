## **OpenCV Thresholding ( cv2.threshold )**

Thresholding is one of the most common (and basic) segmentation techniques in computer vision and it allows us to separate the *foreground* (i.e., the objects that we are interested in) from the *background* of the image.

**1. Basic thresholding** where you have to manually supply a threshold value, *T.*


> (**T, threshInv**) = cv2.**threshold**(blurred, **200**, **255**,**cv2.THRESH_BINARY_INV**)
>
> **apply basic thresholding --** 
>
> **the first parameter is the image we want to threshold, the second value is is our threshold check; if a pixel value is greater than our threshold (in this case, 200), we set it to be *black, otherwise it is *white****
>
> **Finally, we must provide a thresholding method. We use the** *****cv2.THRESH_BINARY_INV***** **method, which indicates that pixel values *p* less than *T* are set to the output value (the third argument)**


****2.  Otsu’s thresholding,** which *automatically* determines the threshold value.**

**apply Otsu's automatic thresholding which automatically determines the best threshold value**

> **(**T, threshInv**)** = cv2.**threshold**(**blurred, **0**, **255**,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU**)
>
> **cv2.**imshow**(**"Threshold"**, threshInv**)
>
> **print**(**"[INFO] otsu's thresholding value: {}"**.**format**(**T**))
