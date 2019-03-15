import pytesseract
from PIL import Image
import os
import cv2

directory = (r'F:\Memes')


for file in os.listdir(directory):
    if file.endswith('.jpg'):
        image = cv2.imread(file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filename = "{}.jpg".format(os.getpid())
        cv2.imwrite(filename, gray)
        img = Image.open(filename)
        text = pytesseract.image_to_string(img)
        print(text)
        os.remove(filename)
        
