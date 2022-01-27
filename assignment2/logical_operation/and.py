from PIL import Image
import numpy as np
import cv2

img1 = np.array(Image.open('image1.jpg'))

img2 = np.array(Image.open('image2.jpg'))

for i in range(3):
    for x in img1[:,:i]:
        for m in x:
            for n in m:
                if img1[m,n,i]>100:
                    img1[m,n,i]=1
                else:
                    img1[m,n,i]=0

                if img2[m,n,i]>100:
                    img2[m,n,i]=1
                else:
                    img2[m,n,i]=0

                x  = img1[m,n,i] and img2[m,n,i]


print(x)

                
                
