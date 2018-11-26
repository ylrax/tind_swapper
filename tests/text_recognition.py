# -*- coding: utf-8 -*-
"""

@author: Xarly
"""
from PIL import Image #, ImageGrab
import pytesseract
from numpy import array
from scipy.misc import imsave
config = '-l spa -oem 3'


def binarize_array(numpy_array, threshold=50):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


def binarize_image(img_path, target_path, threshold):
    """Binarize an image"""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = array(image)
    image = binarize_array(image, threshold)
    imsave(target_path, image)


for i in [200, 210, 220, 225, 230, 235, 236, 237, 238, 239, 240, 241]:
    print(i)
    binarize_image(r'C:\Users\Xarly\Desktop\images\tes3.PNG', r'C:\Users\Xarly\Desktop\images\tes3_bi.PNG', i)
    print(pytesseract.image_to_string(Image.open(r'C:\Users\Xarly\Desktop\images\tes3_bi.PNG'), config=config))
    print(" ")

binarize_image(r'C:\Users\Xarly\Desktop\images\tes3.PNG',r'C:\Users\Xarly\Desktop\images\tes3_bi.PNG', 360)
print(pytesseract.image_to_string(Image.open(r'C:\Users\Xarly\Desktop\images\tes3_bi.PNG'), config=config))

# part of the screen
#im=ImageGrab.grab(bbox=(1420,215,1770,538))
#im.show()
#image_file = im.convert('1')
#image_file.show()
print("saving")
# to file
#im.save(r'C:\Users\Xarly\Desktop\im.jpeg', "JPEG")
