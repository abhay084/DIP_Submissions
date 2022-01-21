
from PIL import Image
import  numpy as np
import cv2

img = np.array(Image.open('office.jpg'))

print("converting colour to gray scale image.")

print(np.shape(img))

print("extract three channels of color image.")

B,G,R = img[:,:,0], img[:,:,1], img[:,:,2]

print(B)
print("\n")
print(G)
print("\n")
print(R)

Y = (R+B+G)/3

print(type(Y))



img2 = cv2.imwrite('gray_office.jpg',Y)



print("Adding images")

img3 = np.array(Image.open('naruto.jpg'))
img4 = np.array(Image.open('sasuke.jpg'))

img5 = img3 + img4

cv2.imwrite('mixed_img.jpg',img5)

