#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:16:36 2021

@author: genevieve.hayes

Different variations of red removed watershed segmentation
"""

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

filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample 6B/Bladder 1 TMA - QATA3_sample6B.tiff"

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

src = load_BGR_img(filepath)
    
# Show source image
print(np.shape(src[1:1000,1:1000]))
#cv2.imshow('Source Image', src)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#crop image
cropped_image = src[2500:3000,2500:3000]
#cropped_image = src[2800:3000,2500:2700]

cv2.imshow("Original Image", cropped_image)
cv2.waitKey()

# In[]: Remove red from the image

def removeRedFromImage(img):
    global img_redremoved
    
    #Convert image to HSV 
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hsv_color_min = np.array([160, 100, 100],np.uint8) #identifies red dye well
    hsv_color_max = np.array([179, 255, 255],np.uint8)
    
    #Define threshold color range to filter
    mask = cv2.inRange(hsv_img, hsv_color_min, hsv_color_max)

    #Bitwise-AND mask and original image
    channel1hsv_img = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
    ratio = cv2.countNonZero(mask)/(hsv_img.size/3)
    percentage_redstain = np.round(ratio*100, 2)

    #Get second masked value (background) mask must be inverted
    mask_inv = cv2.bitwise_not(mask)
    channel2hsv_img = cv2.bitwise_and(hsv_img, hsv_img, mask=mask_inv)
    channel2_img = cv2.cvtColor(channel2hsv_img, cv2.COLOR_HSV2BGR)
    
    #Set masked region to white
    whiteimg = np.full(channel2_img.shape, 255, dtype=np.uint8)  #make white image  
    img_redremoved = np.where(channel2_img[:,:] == [0,0,0], whiteimg, channel2_img) #here we replace black pixels.    
    
    return img_redremoved

image_nored = removeRedFromImage(cropped_image)
cv2.imshow("Original Image with red Channel Removed", image_nored)
cv2.waitKey()

# In[]: Invert input image

image = 255-image_nored
    
# In[]: Apply pyramid mean shift filtering
    
spatial_window_radius = 19
color_window_radius = 20

shifted = cv2.pyrMeanShiftFiltering(image, sp = spatial_window_radius, sr = color_window_radius)# 21, 51)

#cv2.imshow("Pyramid Mean Shifted Image", shifted)
#cv2.waitKey()

# In[]: Convert the mean shift image to grayscale, then apply Otsu thresholding
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayscale Image", gray)
#cv2.waitKey()

thresh_nored = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#thresh = 255 - thresh
#cv2.imshow("Thresholded Image", thresh_nored)
#cv2.waitKey()

# In[]: Compute the exact Euclidean distance from every binary pixel to the nearest zero pixel, then find peaks in this distance map

minimum_distance_map_distance = 11 #3 #10 

# Perform the distance transform algorithm
dist = cv2.distanceTransform(thresh_nored, distanceType=cv2.DIST_L2, maskSize=3)
# Normalize the distance image for range = {0.0, 1.0}
# so we can visualize and threshold it
cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
#cv2.imshow('Distance Transform Image', dist)
#cv2.waitKey()

# Identifiy markers in distance map

localMax = peak_local_max(dist, indices=False, min_distance=minimum_distance_map_distance,
	labels=thresh_nored)

# perform a connected component analysis on the local peaks,
# using 8-connectivity, then apply the Watershed algorithm
markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
markersim = np.array(markers*1000000, dtype="uint8")

cv2.imshow('Markers', markersim)
cv2.waitKey()

# In[]: 
    
# In[]:
# WITHOUT RED COLOR REMOVED

# In[]: Invert input image

a_image = 255-cropped_image
    
# In[]: Apply pyramid mean shift filtering
    
spatial_window_radius = 19
color_window_radius = 20

shifted = cv2.pyrMeanShiftFiltering(a_image, sp = spatial_window_radius, sr = color_window_radius)# 21, 51)

cv2.imshow("Pyramid Mean Shifted Image", shifted)
cv2.waitKey()

# In[]: Convert the mean shift image to grayscale, then apply Otsu thresholding
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey()

thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

cv2.imshow("Thresholded Image", thresh)
cv2.waitKey()

# In[]: Compute the exact Euclidean distance from every binary pixel to the nearest zero pixel, then find peaks in this distance map

minimum_distance_map_distance = 11 #3 #10 

# Perform the distance transform algorithm
distance_withred = cv2.distanceTransform(thresh, distanceType=cv2.DIST_L2, maskSize=3)
# Normalize the distance image for range = {0.0, 1.0}
# so we can visualize and threshold it
cv2.normalize(distance_withred, distance_withred, 0, 1.0, cv2.NORM_MINMAX)
cv2.imshow('Distance Transform Image', distance_withred)
cv2.waitKey()

# Identifiy markers in distance map

localMax = peak_local_max(distance_withred, indices=False, min_distance=minimum_distance_map_distance,
	labels=thresh)

# perform a connected component analysis on the local peaks,
# using 8-connectivity, then apply the Watershed algorithm
markers_withred = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
markersim = np.array(markers*1000000, dtype="uint8")






# In[]: Identify each rsegmented region
    
labels = watershed(-distance_withred, markers_withred, mask=thresh)
print("{} unique segments found".format(len(np.unique(labels)) - 1))

# loop over the unique labels returned by the Watershed algorithm

maskim = np.zeros(np.shape(image), dtype="uint8")
val = 0
radius = 6

r = np.zeros(len(np.unique(labels))+1, dtype="uint8")
mean_coloursBRG = np.zeros((len(np.unique(labels))+1,4), dtype="uint8")
colour_threshold = 160#120 #COLOUR THRESHOLD

for label in np.unique(labels):
	# if the label is zero, we are examining the 'background' so simply ignore it
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
	## draw a circle enclosing the object
    ((x, y), r[val]) = cv2.minEnclosingCircle(c)
    
    
    #Get mean colour inside each contour
    mean_colour_in_contourBRG = cv2.mean(cropped_image,mask)
    mean_coloursBRG[val, :] = mean_colour_in_contourBRG
    
    intensity = np.around(mean_colour_in_contourBRG[0],0)
    
    #Draw Contours
    cv2.drawContours(cropped_image, cnts, -1, (255,0,0), 1)
 
    markersim = cv2.circle(markersim,(int(x), int(y)), int(radius), 255, -1)

#cv2.imshow('Visible Markers', markersim)
#cv2.waitKey()

#cv2.imshow("Mask", maskim)
#cv2.waitKey()

# show the output image
cv2.imshow("Watershed Segmented Image", cropped_image)
cv2.waitKey()

print('Number of segments larger than radius 6:', len(r[r > 6]))