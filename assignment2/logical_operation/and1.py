from PIL import Image
import numpy as np
import cv2

img1 = np.array(Image.open('Image1.jpg'))
img2 = np.array(Image.open('Image2.jpg'))

R = img1[:,:,0] + img2[:,:,0]
G = img1[:,:,1] + img2[:,:,1]
B = img1[:,:,2] + img2[:,:,2]

img3 = 0.2989 * R + 0.5870 * G + 0.1140 * B

cv2.imwrite('gray_image.jpg',img3)

'''
for i in range(311):
    for j in range(553):
        if img3[i,j]>50:
            img3[i,j]=1
        else:
            img3[i,j]=0


cv2.imwrite('binary_image.jpg',img3)
'''
