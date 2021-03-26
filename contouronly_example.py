#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:11:14 2020

@author: genevieve.hayes
"""

# import the necessary packages
from __future__ import print_function
#import skimage
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
#import argparse
import imutils
import cv2
import numpy as np

#filepath
filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Coins.png"

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", filepath, required=True,
#	help="path to input image")
#args = vars(ap.parse_args())

# load the image and perform pyramid mean shift filtering
# to aid the thresholding step
image = cv2.imread(filepath)
#image = image[0:500, 0:500]
shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)
cv2.imshow("Input", image)
cv2.waitKey()

# convert the mean shift image to grayscale, then apply
# Otsu's thresholding
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey()

# In[1]: 
# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("[INFO] {} unique contours found".format(len(cnts)))
# loop over the contours
for (i, c) in enumerate(cnts):
    # draw the contour
    ((x, y), _) = cv2.minEnclosingCircle(c)
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, "#{}".format(i + 1), (int(x) - 10, int(y)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
# show the output image
cv2.imshow("Contour-Only Segmented Image", image)
cv2.waitKey()
