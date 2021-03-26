#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:13:43 2020

@author: genevieve.hayes
"""
# import the necessary packages
from __future__ import print_function
from PIL import Image
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
cv2.imshow("Original Image", image)
cv2.waitKey()

cv2.imshow("Pyramimd Mean Shifted Image", shifted)
cv2.waitKey()

# convert the mean shift image to grayscale, then apply
# Otsu's thresholding
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey()
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#thresh = 255 - thresh
cv2.imshow("Thresholded Image", thresh)
cv2.waitKey()

# In[2]: 
# compute the exact Euclidean distance from every binary
# pixel to the nearest zero pixel, then find peaks in this
# distance map

minimum_distance_map_distance = 28

#D = ndimage.distance_transform_edt(thresh)

# Perform the distance transform algorithm
dist = cv2.distanceTransform(thresh, distanceType=cv2.DIST_L2, maskSize=3)
# Normalize the distance image for range = {0.0, 1.0}
# so we can visualize and threshold it
cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
cv2.imshow('Distance Transform Image', dist)
cv2.waitKey()

localMax = peak_local_max(dist, indices=False, min_distance=minimum_distance_map_distance,
	labels=thresh)

# perform a connected component analysis on the local peaks,
# using 8-connectivity, then appy the Watershed algorithm
markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
markersim = np.array(markers*1000000, dtype="uint8")

cv2.imshow('Markers', markersim)
cv2.waitKey()

#count = 0
#r = 5
#for i in range(np.shape(markers)[0]):
#    for j in range(np.shape(markers)[1]):
#        if markersim[i,j] > 0.5:
#            count = count +1
#            markersim = cv2.circle(markersim,(i,j), r, 255, -1)
            
#cv2.imshow('Visible Markers', markersim)
#cv2.waitKey()

labels = watershed(-dist, markers, mask=thresh)
print("{} unique segments found".format(len(np.unique(labels)) - 1))

# loop over the unique labels returned by the Watershed
# algorithm

maskim = np.zeros(np.shape(image), dtype="uint8")
val = 0
radius = 6

for label in np.unique(labels):
	# if the label is zero, we are examining the 'background'
	# so simply ignore it
    val = val+1
    if label == 0:
        continue
    # otherwise, allocate memory for the label region and draw
    # it on the mask
    mask = np.zeros(gray.shape, dtype="uint8")
    mask[labels == label] = 255
    
    color1 = (list(np.random.choice(range(256), size=3)))  
    color =[int(color1[0]), int(color1[1]), int(color1[2])]
    maskim[labels == label] = color
    
	# detect contours in the mask and grab the largest one
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
	# draw a circle enclosing the object
    ((x, y), r) = cv2.minEnclosingCircle(c)
    cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
    cv2.putText(image, "#{}".format(label), (int(x) - 10, int(y)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    markersim = cv2.circle(markersim,(int(x), int(y)), int(radius), 255, -1)

cv2.imshow('Visible Markers', markersim)
cv2.waitKey()

cv2.imshow("Mask", maskim)
cv2.waitKey()

# show the output image
cv2.imshow("Watershed Segmented Image", image)
cv2.waitKey()

