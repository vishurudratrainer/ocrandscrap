# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:07:11 2023

@author: ASUS
"""

import pytesseract
from PIL import Image,ImageOps,ImageFilter

image_path = "C:/ocr/img.png"
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)
print(extracted_text)

with open("C:/ocr/output.txt", "w") as output_file:
    output_file.write(extracted_text)
    
    
config = '--psm 6 -l eng'
text = pytesseract.image_to_string(image, config=config)
print(text)

#pytesseract.pytesseract.tesseract_cmd = '/path/to/tesseract'

config = '-l eng+fra'
text = pytesseract.image_to_string(image, config=config)
from PIL import ImageOps, ImageFilter

# Convert image to grayscale.
gray_image = ImageOps.grayscale(image)

# Resize the image.
scale_factor = 2
resized_image = gray_image.resize(
    (gray_image.width * scale_factor, gray_image.height * scale_factor),
    resample=Image.LANCZOS
)

# Apply adaptive thresholding.
thresholded_image = resized_image.filter(ImageFilter.FIND_EDGES)

# Extract text from the preprocessed image.
improved_text = pytesseract.image_to_string(thresholded_image)
print(improved_text)


import re

config = '--psm 6'
text = pytesseract.image_to_string(image, config=config)
digits = re.findall(r'\d+', text)
print(digits)