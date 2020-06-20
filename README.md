# OCR-
A basic OCR script based on tesseract for python which extracts text from images and uses OpenCV 2.
Library requirements For python on Windows :

1. Pytesseract 
2. Image
3. Os
4. OpenCV
5. Numpy
6. Argparse

Note - Pytesseract requires the tesseract binary to be installed on the system for interfacing.

The image may need some preprocessing before running it through tesseract therefore I have added some options for preprocessing like -
Thresholding, Blur, Dilation, Erosion, Opening, Closing and Deskewing(may or may not work properly depending on the image). 
You need to choose the preprocessing option based on your needs.

Usage :

```
$ python ocr.py -p "preprocess-option"
Example(thresholding) : $ python ocr.py -p thresh
```

Sample Image :
![Input](https://raw.githubusercontent.com/Akhilesh64/OCR-/master/Image.png)

Below is the Output after running the Image.png file through the script with close preprocessing parameter :

![Output](https://raw.githubusercontent.com/Akhilesh64/OCR-/master/Text_Output.png)

Deskewing sample image :

![Input](https://raw.githubusercontent.com/Akhilesh64/OCR-/master/Image1.jpg)

Image after after running the script with deskew preprocessing parameter :

![Output](https://raw.githubusercontent.com/Akhilesh64/OCR-/master/Output_Img1.jpg)

Recognized Text:

![Output](https://raw.githubusercontent.com/Akhilesh64/OCR-/master/Output_Image1.png)

