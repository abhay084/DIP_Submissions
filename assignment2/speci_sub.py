import cv2
import numpy as np


img1 = cv2.imread("img.png")

gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray.png',gray)

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if(i>300 and i<600 and j>500 and j<650):
            gray[i,j]=255
        else:
            continue

cv2.imwrite('new.png',gray)

