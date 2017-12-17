import cv2
import numpy as np

img_rgb = cv2.imread('img-for-matching.jpeg')
if img_rgb == None: 
    raise Exception("could not load image 1!")

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('/home/george/Documents/opencv-template-matching/template.jpeg',0)
if template == None: 
    raise Exception("could not load image 2!")

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)


for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)


cv2.waitKey(0)