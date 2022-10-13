import cv2
image_bit1 = cv2.imread('./bit1.png')
image_bit2 = cv2.imread('./bit2.png')


# AND operation
cv2.imshow("AND operation", cv2.bitwise_and(src1=image_bit1, src2=image_bit2))

# OR operation
cv2.imshow("OR operation", cv2.bitwise_or(src1=image_bit1, src2=image_bit2))
# XOR operation
cv2.imshow("XOR operation", cv2.bitwise_xor(src1=image_bit1, src2=image_bit2))
# NOT operation
cv2.imshow("NOT operation", cv2.bitwise_not(src=image_bit1))
cv2.waitKey(0)
cv2.destroyAllWindows()
