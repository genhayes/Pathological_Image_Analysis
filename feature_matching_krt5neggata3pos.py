#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:33:18 2021

@author: genevieve.hayes

Feature Matching  of KRT5- GATA3+
"""

# In[0]: IMPORT

# import the necessary packages
from __future__ import print_function
from PIL import Image
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import argparse
import imutils
import cv2
import numpy as np
import random as rng
import matplotlib.pyplot as plt

# In[00]: FUNCTIONS

def load_BGR_img(filepath):
    #Loads BGR image at filepath (str type).
    rng.seed(12345)
    parser = argparse.ArgumentParser(description='Code for Image Segmentation with Distance Transform and Watershed Algorithm.\
                                     Sample code showing how to segment overlapping objects using Laplacian filtering, \
                                    in addition to Watershed and Distance Transformation')
    parser.add_argument('--input', help='Path to input image.', default=filepath)
    args = parser.parse_args()
    BGR_img = cv2.imread(cv2.samples.findFile(args.input))
    if BGR_img is None:
        print('Could not open or find the image:', args.input)
        exit(0)
        
    return BGR_img

# In[1]: LOAD IMAGE

filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample 6B/Bladder 1 TMA - QATA3_sample6B.tiff"
filepath_featurekngp = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos.tiff"
BGR_fullimg = load_BGR_img(filepath)
BGR_fullimg = BGR_fullimg[2500:3000,2500:3000]
BGR_featureimg_kngp = load_BGR_img(filepath_featurekngp)

# In[]: Feature Matching

#img1 = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)          # queryImage
#img2 = cv2.imread(filepath_featurekngp,cv2.IMREAD_GRAYSCALE) # trainImage
img1 = BGR_fullimg
img2 = BGR_featureimg_kngp
# Initiate SIFT detector
sift = cv2.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3)
plt.show()

# In[]: Object Matching

originalPicRead = BGR_fullimg
#img_bgr = cv2.resize(originalPicRead, (0,0), fx=0.33, fy=0.33)
img_bgr = BGR_fullimg
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

templateR = cv2.imread(filepath_featurekngp,0)

w,h = templateR.shape[::-1]

for magn in range(1,11):
    mult = magn*0.35
    w,h = int(mult*w),int(mult*h)
    template = cv2.resize(templateR, (0,0), fx=mult, fy = mult)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.35
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow('Detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()