# -*- coding: utf-8 -*-
"""
@author: Xarly
"""

import time
import pyautogui#, win32gui
import PIL.ImageGrab
import cv2
from PIL import ImageGrab # , Image
import pytesseract
import dlib
import imutils
from numpy import array, uint8
# from scipy.misc import imsave
from imageai.Detection import ObjectDetection
import os
config = '-l spa -oem 3'

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
# rgb = PIL.ImageGrab.grab().load()[x,y]


def need_scroll():
    if PIL.ImageGrab.grab().load()[1782, 455] == (205, 205, 205):
        return True
    else:
        return False


def get_images_number():

    positions = [PIL.ImageGrab.grab().load()[1582, 555],
                 PIL.ImageGrab.grab().load()[1570, 555],
                 PIL.ImageGrab.grab().load()[1557, 555],
                 PIL.ImageGrab.grab().load()[1546, 555],
                 PIL.ImageGrab.grab().load()[1534, 555],
                 PIL.ImageGrab.grab().load()[1522, 555],
                 PIL.ImageGrab.grab().load()[1510, 555],
                 PIL.ImageGrab.grab().load()[1500, 555]]
    try:
        return positions.index((253, 80, 104)) + 2
    except ValueError:
        return 0


def has_faces(img):

    im = img.convert('RGB')
    im = array(im)
    image = im.astype(uint8)
    detector = dlib.get_frontal_face_detector()
    # Run the face detector, up-sampling the image 1 time to find smaller faces.
    faces = detector(image, 1)

    print("number of faces detected: ", len(faces))
    return faces


def has_people(img):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    im = img.convert('RGB')
    im = array(im)
    image = im.astype(uint8)
    # image = cv2.resize(image, (min(800, image.shape[1]), min(600, image.shape[0])), interpolation = cv2.INTER_LINEAR)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
    return rects, weights


def skip(m):
    def swapper():
        time.sleep(1)
        pyautogui.keyDown('space')
        time.sleep(0.1)
        pyautogui.keyUp('space')
        time.sleep(0.3)
        # part of the screen
        im = PIL.ImageGrab.grab(bbox=(1420, 215, 1770, 538))
        print("Faces: ", has_faces(im))
        print("Ppl: ", has_people(im))
        print("things :")
        image_things_detector(im)
    # im.show()
    swapper()
    im = PIL.ImageGrab.grab(bbox=(1420, 215, 1770, 538))
    print("Faces: ", has_faces(im))
    print("Ppl: ", has_people(im))
    print("things :")
    image_things_detector(im)
    for i in range(m-2):
        swapper()


def image_things_detector(image):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=image,
                                                 input_type="array")

    for eachObject in detections:
        print(eachObject["name"], " : ", eachObject["percentage_probability"])


def get_instagram():
    photos = ImageGrab.grab(bbox=(1420, 407, 1500, 444))
    try:
        print('Photos: ', int(pytesseract.image_to_string(photos, config='-l spa -oem 3')[0:4]))
        print('Photos: ', int(pytesseract.image_to_string(photos.convert('L'), config='-l spa -oem 3')[0:4]))
    except ValueError:
        print("No valid Instagram")


def get_description():
    image = ImageGrab.grab(bbox=(1420, 580, 1750, 790))
    image = image.convert('RGB')
    image = array(image)
    image = image.astype(uint8)
    template = cv2.imread(r'line.jpg')

    # Convert to grayscale
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Find template
    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = templateGray.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 4)

    image2 = ImageGrab.grab(bbox=(1420, 580 + max_loc[1] + h, 1750, 790))
    image2 = image2.convert('RGB')
    image2 = array(image2)
    image2 = image2.astype(uint8)
    print('Summary: ', pytesseract.image_to_string(image2, config='-l spa -oem 3'))
    return pytesseract.image_to_string(image2, config='-l spa -oem 3')


for i in range(1):
    description = []
    photos = []

    time.sleep(4)
    pyautogui.keyDown('up')
    time.sleep(0.1)
    pyautogui.keyUp('up')
    time.sleep(0.1)
    n = get_images_number()
    print(n)
    description = get_description()
    print("Description: ", description)
    scroll = need_scroll()
    print("Need scroll: ", scroll, "\n")

    skip(n)
    if scroll:
        print("Scrolling")
        pyautogui.click(x=1784, y=725)
        time.sleep(0.1)
        pyautogui.dragRel(0, 100, 1, button='left')
        get_instagram()







# Scuba:

# person  :  67.8743302822113
# motorcycle  :  53.09184193611145

# o
# kite  :  59.69024896621704
# bird  :  78.75009179115295
