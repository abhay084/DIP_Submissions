import numpy as np
from PIL import Image
import cv2

pic1 = np.array(Image.open('sasuke.jpg'))

B = pic1[:,:,0]
G = pic1[:,:,1]
R = pic1[:,:,2]

gray = (B+G+R)/3

print(np.shape(gray))


for i in range(1080):
    for j in range(1920):
        if gray[i,j]>100:
            gray[i,j]=1
        else:
            gray[i,j]=0


cv2.imwrite('binary_image.jpg',gray)

