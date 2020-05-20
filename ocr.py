from PIL import Image
import pytesseract
import argparse
import cv2
import os
import numpy as np
kernel = np.ones((5,5),np.uint8)

#Argument Parser

parser = argparse.ArgumentParser(description='For Preprocessing Options.')
parser.add_argument('-p', '--preprocess', type=str, help='type of preprocessing to be done')
args = vars(parser.parse_args())

image = cv2.imread('Image.png',0)

if args['preprocess'] == 'thresh':
    a = cv2.threshold(image, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    image=np.float32(a[1])
        
elif args['preprocess'] == 'blur':
    image = cv2.medianBlur(image,3)

elif args['preprocess'] == 'dilate':
    image = cv2.dilate(image,kernel,iterations = 1)

elif args['preprocess'] == 'erode':
    image = cv2.erode(image,kernel,iterations = 1)

elif args['preprocess'] == 'open':
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

elif args['preprocess'] == 'close':
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

elif args['preprocess'] == 'deskew':
    gray = cv2.bitwise_not(image)
    thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    coords = np.column_stack(np.where(thresh[1] > 0))
    angle = cv2.minAreaRect(coords)
    new_list=list(angle)
    if new_list[2] < -45:
        new_list[2] = -(90 + new_list[2])
    else:
        new_list[2]=-new_list[2]
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, new_list[2], 1.0)
    image = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


cv2.imwrite('Output_Img.jpg', image)

text = pytesseract.image_to_string(Image.open('Output_Img.jpg'))

print(text)
