#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:37:52 2020

Watershed segmentation and color identification within ROIs

@author: genevieve.hayes
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

def loadImageYCbCr( path ):
    global currentImage
    currentImage = Image.open( path ).convert( 'YCbCr' ).transpose( Image.FLIP_TOP_BOTTOM )
    return currentImage

def loadImageRGB( path ):
    global currentImage
    currentImage = Image.open( path ).convert( 'RGB' ).transpose( Image.FLIP_TOP_BOTTOM )
    return currentImage

currentImage = loadImageRGB( filepath )
width = currentImage.size[0]
height = currentImage.size[1]
currentPixels = currentImage.load()
np_currentImage = np.asarray(currentImage)
print(np.shape(np_currentImage))

rng.seed(12345)
parser = argparse.ArgumentParser(description='Code for Image Segmentation with Distance Transform and Watershed Algorithm.\
    Sample code showing how to segment overlapping objects using Laplacian filtering, \
    in addition to Watershed and Distance Transformation')
parser.add_argument('--input', help='Path to input image.', default=filepath)
args = parser.parse_args()
src = cv2.imread(cv2.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
# Show source image
print(np.shape(src[1:1000,1:1000]))
cv2.imshow('Source Image', src)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped_image = src[2500:3000,2500:3000]

cv2.imshow("Original Image", cropped_image)
cv2.waitKey()

image = 255-cropped_image

cv2.imshow("Inverted Image", image)
cv2.waitKey()


spatial_window_radius = 19
color_window_radius = 20

shifted = cv2.pyrMeanShiftFiltering(image, sp = spatial_window_radius, sr = color_window_radius)# 21, 51)

cv2.imshow("Pyramid Mean Shifted Image", shifted)
cv2.waitKey()

# In[]: 

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

minimum_distance_map_distance = 10 #28

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

cropped_image_hsv_colourID = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
mean_colours = np.zeros((len(np.unique(labels))+1,3), dtype="uint8") #initialize RGB mean colour array for each segmentation

# show hsv image
cv2.imshow("HSV Colour Image", cropped_image_hsv_colourID)
cv2.waitKey()

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
	## draw a circle enclosing the object
    ((x, y), r) = cv2.minEnclosingCircle(c)
    #cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
    
    #Draw Contours
    cv2.drawContours(cropped_image, cnts, -1, (0,255,0), 1)
    
    #Get mean colour inside each contour
    mean_colour_in_contour = cv2.mean(cropped_image_hsv_colourID,mask)
    mean_colours[val, :] = mean_colour_in_contour[0:3]
    
    colour_threshold = 50
    
    if mean_colour_in_contour[0] >= colour_threshold:
        #binary_colourID = [0, 100, 100] #red
        binary_colourID = [230, 100, 100] #blue
        #binary_colourID = mean_colour_in_contour[0:3]
    else:
        #binary_colourID = [230, 100, 100] #blue
        binary_colourID = mean_colour_in_contour[0:3]
    
    cv2.drawContours(cropped_image_hsv_colourID, cnts, -1,binary_colourID,-1)        
    #cv2.drawContours(cropped_image_hsv_colourID, cnts, -1,mean_colour_in_contour,-1)
    #cv2.putText(image, "#{}".format(label), (int(x) - 10, int(y)),
		#cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    markersim = cv2.circle(markersim,(int(x), int(y)), int(radius), 255, -1)

cv2.imshow('Visible Markers', markersim)
cv2.waitKey()

cv2.imshow("Mask", maskim)
cv2.waitKey()

# show the output image with identified cell contours
cv2.imshow("Watershed Segmented Image", cropped_image)
cv2.waitKey()

segment_hue = mean_colours[:,0]
# using list comprehension to get numbers > colour_threshold 
count = len([i for i in segment_hue if i > colour_threshold]) 

# printing the intersection  
print ("The number of cell with hue less than"+ str(colour_threshold) + " : " + str(count))

# In[]:

# show the output image with blocks of identified mean colours
cv2.imshow("Colour ID of Segmented Image, Greater than 50 Hue Coloured Blue", cropped_image_hsv_colourID)
cv2.waitKey()



