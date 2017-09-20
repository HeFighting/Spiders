#coding=utf-8

import pytesseract

from PIL import Image

# 加载图片文件
img = Image.open('test.jpg')

# 提取数据
text = pytesseract.image_to_string(img)

print(text)
