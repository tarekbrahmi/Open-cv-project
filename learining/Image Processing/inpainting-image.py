import cv2

# Open the image.
img = cv2.imread('cat_damaged.png')


# # Load the mask.
mask = cv2.imread('cat_mask.png',0)
# mask=cv2.bitwise_not(src=mask)
# new_mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
# cv2.imshow('New mask', new_mask)
# cv2.waitKey(0)
# Inpaint.
result = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

cv2.imshow('Noise removed with mask', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
