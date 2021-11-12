import cv2
from random import *
from copy import deepcopy

img = cv2.imread('picture.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    // Umwandlung des Bilder in Graustufen

key = deepcopy(gray_img)
AND = deepcopy(gray_img)
OR = deepcopy(gray_img)
XOR = deepcopy(gray_img)

height, width = gray_img.shape[:2]

for i in range(height):
    for j in range(width):
        key[i, j] = randint(0,255)

        AND[i,j] = gray_img[i,j] & key[i, j]
        OR[i,j] = gray_img[i,j] | key[i, j]
        XOR[i,j] = gray_img[i,j] ^ key[i, j]

//cv2.imshow('AND', AND)
//cv2.imshow('OR', OR)
cv2.imshow('XOR', XOR)      // Anzeige des versuesselten Bildes
