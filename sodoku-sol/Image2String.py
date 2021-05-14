import json

import cv2
import numpy as np
from cv2 import *
import RemoveHV as rm
import pytesseract
from collections import  Counter

def generate_text(img):
    gray = np.array(img)
    gray = 255 * (gray < 128).astype(np.uint8)  # To invert the text to white
    coords = cv2.findNonZero(gray)  # Find all non-zero points (text)
    x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box
    image = img[y - 15:y + h + 15, x - 15:x + w + 15]
    concateImg = np.concatenate((image, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    concateImg = np.concatenate((concateImg, image), axis=1)
    try :
        text = pytesseract.image_to_string(concateImg)
        if len(text)>3:
            arrr = []
            arrr[:0]=text
            ctn = Counter(arrr)
            for aa in ctn:
                # if int(aa)>=1 and int(aa)<=9:
                return int(aa)
        else :
            return  "."
    except Exception as e:
        return "."
    # return pytesseract.image_to_string(concateImg)


def to81(path):
    img = cv2.imread(path, 0)
    result = img.copy()
    img = rm.renmove_lines(img, x)
    img = cv2.resize(img, (900, 900))
    # cut the image to sigle number
    cell = [np.hsplit(row, 9) for row in np.vsplit(img, 9)]
    arr = ""
    for i in cell:
    # print(len(i))
        for j in i :
            arr+=str(generate_text(j))
    print(arr)

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = "D:\\SteamGame\\New folder\\tesseract.exe"
    x = 100
    path = '1.png'
    to81(path)