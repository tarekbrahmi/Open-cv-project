import cv2

# path
path = r'icons.jpg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Bordred image'
"""
 camon border type
  
 cv2.BORDER_CONSTANT: 
    It adds a constant colored border. The value should be given as a keyword argument
 cv2.BORDER_REFLECT: 
    The border will be mirror reflection of the border elements. Suppose, if image contains letters “abcdefg” then output will be “gfedcba|abcdefg|gfedcba“. 
 cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT: 
    It does the same works as cv2.BORDER_REFLECT but with slight change. Suppose, if image contains letters “abcdefgh” then output will be “gfedcb|abcdefgh|gfedcba“. 
 cv2.BORDER_REPLICATE: 
    It replicates the last element. Suppose, if image contains letters “abcdefgh” then output will be “aaaaa|abcdefgh|hhhhh“. 
"""
# Using cv2.copyMakeBorder() method
image = cv2.copyMakeBorder(src=image,
                           top=10,
                           bottom=10,
                           left=10,
                           right=10,
                           borderType=cv2.BORDER_CONSTANT,
                           dst=None,
                           value=0
                           )

# Displaying the image

cv2.imshow("BORDER_CONSTANT", image)
cv2.waitKey(0)
image = cv2.copyMakeBorder(src=image,
                           top=image.shape[0],
                           bottom=image.shape[0],
                           left=image.shape[1],
                           right=image.shape[1],
                           borderType=cv2.BORDER_REFLECT,
                           dst=None,
                           value=0
                           )

# Displaying the image

cv2.imshow("BORDER_REFLECT", image)
cv2.waitKey(0)

image = cv2.copyMakeBorder(src=image,
                           top=10,
                           bottom=10,
                           left=10,
                           right=10,
                           borderType=cv2.BORDER_REPLICATE,
                           dst=None,
                           value=0
                           )

# Displaying the image

cv2.imshow("BORDER_REPLICATE", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
