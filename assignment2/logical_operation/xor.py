import cv2
import numpy as np

img1 = cv2.imread("circle.jpg")
img2 = cv2.imread("rectangle.jpg")

print(img1.shape)
print(img2.shape)

dim = (500,400)

res_img1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
res_img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)

print(res_img1.shape)
print(res_img2.shape)

img3 = cv2.bitwise_xor(res_img1,res_img2)

cv2.imshow('new',img3)
cv2.waitKey()
cv2.destroyAllWindows()
