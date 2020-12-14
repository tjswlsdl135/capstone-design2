from PIL import Image
from pytesseract import *

# # 영어 인식
# print(pytesseract.image_to_string(Image.open('testocr.png')))

# 한글 
img = Image.open('sample2.jpg')
text = pytesseract.image_to_string(img, lang='kor+eng')
print(text)
