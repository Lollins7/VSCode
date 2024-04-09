from PIL import Image
import os
image = Image.open("img.jpg")
# print(os.getcwd())
image.save("img.eps")
