**Approach :**

* Find all the contours in the image.
* Find the bounding rectangle of every contour.
* Compare and validate the sides ratio and area of every bounding rectangle with an average license plate.
* Apply image segmentation in the image inside the validated contour to find characters in it.
* Recognize characters using an OCR.

**Methodology:**

1. To reduce the noise we need to blur the input Image with [Gaussian Blur](https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html) and then convert it to grayscale.
2. Find vertical edges in the image.
3. To reveal the plate we have to binarize the image. For this apply Otsu’s Thresholding on the vertical edge image. In other thresholding methods, we have to choose a threshold value to binarize the image but Otsu’s Thresholding determines the value automatically.
4. Apply Closing Morphological Transformation on the thresholded image. Closing is useful to fill small black regions between white regions in a thresholded image. It reveals the rectangular white box of license plates.
5. To detect the plate we need to find contours in the image. It is important to binarize and morph the image before finding contours so that it can find a more relevant and less number of contours in the image. If you draw all the extracted contours on the original image.
6. Now find the [minimum area rectangle](https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=minarearect#minarearect) enclosed by each of the contours and validate their side ratios and area. We have defined the minimum and maximum area of the plate as 4500 and 30000 respectively.
7. Now find the contours in the validated region and validate the side ratios and area of the bounding rectangle of the largest contour in that region. After validating you will get a perfect contour of a license plate. Now extract that contour from the original image.
8. To recognize the characters on the license plate precisely, we have to apply image segmentation. That first step is to extract the value channel from the HSV format of the plate’s image. It would look like.
9. Now apply adaptive thresholding on the plate’s value channel image to binarize it and reveal the characters. The image of the plate can have different lighting conditions in different areas, in that case, adaptive thresholding can be more suitable to binarize because it uses different threshold values for different regions based on the brightness of the pixels in the region around it.
10. After binarizing apply bitwise not operation on the image to find the connected components in the image so that we can extract character candidates.
11. Construct a mask to display all the character components and then find contours in the mask. After extracting the contours take the largest one, find its bounding rectangle and validate side ratios.
12. After validating the side ratios find the convex hull of the contour ad draws it on the character candidate mask. The mask would look like-
13. Now find all the contours in the character candidate mask and extract those contour areas from the plate’s value thresholded image, you will get all the characters separately.

OCR Comparison
