# -*- coding: utf-8 -*-
"""
@author: Xarly
"""

import dlib
from skimage import io
import PIL.ImageGrab
from numpy import array, uint8

img = io.imread(r'C:\Users\Xarly\Desktop\images\faces2.JPEG')


im = PIL.ImageGrab.grab(bbox=(1420, 215, 1770, 538))
im = im.convert('RGB')
im = array(im)
image = im.astype(uint8)
print(type(img), type(im), type(image))
detector = dlib.get_frontal_face_detector()
# Run the face detector, up-sampling the image 1 time to find smaller faces.
dets = detector(image, 1)

print("number of faces detected: ", len(dets))
win = dlib.image_window()
win.set_image(image)
win.add_overlay(dets)
input("Hit enter to continue")
