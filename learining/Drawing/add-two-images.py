import cv2
image1 = cv2.imread("./image1.jpg")
image2 = cv2.imread("./image2.jpg")

# cv2.addWeighted is applied over the
# image inputs with applied parameters

# dst = src1*alpha + src2*beta + gamma;

result = cv2.addWeighted(src1=image1, alpha=1,
                         src2=image2, beta=0.1, gamma=0)

cv2.imshow("Concatination", result)
cv2.waitKey(0)
