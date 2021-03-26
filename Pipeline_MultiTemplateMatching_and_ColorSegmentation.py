#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:13:28 2021

@author: genevieve.hayes

Pipeline (using colour segmentation and template matching).

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
import MTM
from MTM import matchTemplates, drawBoxesOnRGB

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

def create_red_mask(img):
    
    #Convert image to HSV 
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hsv_color_min = np.array([160, 100, 100],np.uint8) #identifies red dye well
    hsv_color_max = np.array([179, 255, 255],np.uint8)
    
    #Define threshold color range to filter
    mask_red = cv2.inRange(hsv_img, hsv_color_min, hsv_color_max)
    
    #Get inverted mask (background) 
    mask_nored = cv2.bitwise_not(mask_red)
    
    return mask_red, mask_nored

def create_light_red_mask(img):
    
    #Convert image to HSV 
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
        #hsv_color_min = np.array([-1,70,20]) #identifies brown cells well in red region
        #hsv_color_max = np.array([30,255,255])
    
    hsv_color_min = np.array([100, 50, 100],np.uint8) #identifies red dye well
    hsv_color_max = np.array([179, 255, 255],np.uint8)
    
    #Define threshold color range to filter
    mask_red = cv2.inRange(hsv_img, hsv_color_min, hsv_color_max)
    
    #Get inverted mask (background) 
    mask_nored = cv2.bitwise_not(mask_red)
    
    return mask_red, mask_nored

def removeRedRegionFromImage(img, mask_red):
    
    #Convert image to HSV 
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Bitwise-AND mask and original image
    channel_red_hsv_img = cv2.bitwise_and(hsv_img, hsv_img, mask=mask_red)
    ratio = cv2.countNonZero(mask_red)/(hsv_img.size/3)
    percentage_redstain = np.round(ratio*100, 2)

    #Get second masked value (background) mask must be inverted
    mask_nored = cv2.bitwise_not(mask_red)
    channel_nored_hsv_img = cv2.bitwise_and(hsv_img, hsv_img, mask=mask_nored)
    channel_nored_img = cv2.cvtColor(channel_nored_hsv_img, cv2.COLOR_HSV2BGR)
    
    #Set masked region to white
    whiteimg = np.full(channel_nored_img.shape, 255, dtype=np.uint8)  #make white image  
    img_redremoved = np.where(channel_nored_img[:,:] == [0,0,0], whiteimg, channel_nored_img) #here we replace black pixels.    
    
    return img_redremoved


def fill_mask_holes(mask, kernel):
    ''' Fill holes in the mask with a defined kernel.
    Kernel can be rectangular (kernel = np.ones((10,10),np.uint8)), 
    cross (kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(20,25))),
    or elliptical (kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,25))).
    '''
    closed_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    return closed_mask


#WATERSHED PREPROCESSING FUNCTION
def preprocessing_for_watershed(image_nored):
    
    # Invert input image
    image = 255-image_nored
    
    #Apply pyramid mean shift filtering
    spatial_window_radius = 19
    color_window_radius = 20
    shifted = cv2.pyrMeanShiftFiltering(image, sp = spatial_window_radius, sr = color_window_radius)

    # Convert the mean shift image to grayscale, then apply Otsu thresholding
    gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Compute the exact Euclidean distance from every binary pixel to the nearest zero pixel, then find peaks in this distance map
    minimum_distance_map_distance = 11 #3 #10 

    # Perform the distance transform algorithm
    dist = cv2.distanceTransform(thresh, distanceType=cv2.DIST_L2, maskSize=3)
    # Normalize the distance image for range = {0.0, 1.0} so we can visualize and threshold it
    cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)

    localMax = peak_local_max(dist, indices=False, min_distance=minimum_distance_map_distance, labels=thresh)

    # perform a connected component analysis on the local peaks, using 8-connectivity, then apply the Watershed algorithm
    markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
    markersimg = np.array(markers*1000000, dtype="uint8")
    
    return markers, thresh, dist, gray, markersimg

def BGRinBrownRange_whiteRegion(mean_colour_in_contourHSV):
    
    hsv_color_min = np.array([-1,70,20]) #identifies brown cells well
    hsv_color_max = np.array([30,255,255])
    
    inHRange = (mean_colour_in_contourHSV[0]>hsv_color_min[0])*(mean_colour_in_contourHSV[0]<hsv_color_max[0])
    inSRange = (mean_colour_in_contourHSV[1]>hsv_color_min[1])*(mean_colour_in_contourHSV[1]<hsv_color_max[1])
    inVRange = (mean_colour_in_contourHSV[2]>hsv_color_min[2])*(mean_colour_in_contourHSV[2]<hsv_color_max[2])
    
    inBrownRange = inHRange*inSRange*inVRange
    
    return inBrownRange

def BGRinBlueRange_whiteRegion(mean_colour_in_contourHSV):
    
    hsv_color_min = np.array([38, 0, 18],np.uint8) #identifies blue cells well
    hsv_color_max = np.array([160, 255, 255],np.uint8)
    
    inHRange = (mean_colour_in_contourHSV[0]>hsv_color_min[0])*(mean_colour_in_contourHSV[0]<hsv_color_max[0])
    inSRange = (mean_colour_in_contourHSV[1]>hsv_color_min[1])*(mean_colour_in_contourHSV[1]<hsv_color_max[1])
    inVRange = (mean_colour_in_contourHSV[2]>hsv_color_min[2])*(mean_colour_in_contourHSV[2]<hsv_color_max[2])
    
    inBlueRange = inHRange*inSRange*inVRange
    
    return inBlueRange

def BGRinBrownRange_redRegion(mean_colour_in_contourHSV):
    
    hsv_color_min = np.array([-1,70,20]) #identifies brown cells well in red region
    hsv_color_max = np.array([30,255,255])
    
    inHRange = (mean_colour_in_contourHSV[0]>hsv_color_min[0])*(mean_colour_in_contourHSV[0]<hsv_color_max[0])
    inSRange = (mean_colour_in_contourHSV[1]>hsv_color_min[1])*(mean_colour_in_contourHSV[1]<hsv_color_max[1])
    inVRange = (mean_colour_in_contourHSV[2]>hsv_color_min[2])*(mean_colour_in_contourHSV[2]<hsv_color_max[2])
    
    inBrownRange = inHRange*inSRange*inVRange
    
    return inBrownRange

def BGRinBlueRange_redRegion(mean_colour_in_contourHSV):
    
    hsv_color_min = np.array([38, 0, 18],np.uint8) #identifies blue cells well
    hsv_color_max = np.array([160, 255, 255],np.uint8)
    
    inHRange = (mean_colour_in_contourHSV[0]>hsv_color_min[0])*(mean_colour_in_contourHSV[0]<hsv_color_max[0])
    inSRange = (mean_colour_in_contourHSV[1]>hsv_color_min[1])*(mean_colour_in_contourHSV[1]<hsv_color_max[1])
    inVRange = (mean_colour_in_contourHSV[2]>hsv_color_min[2])*(mean_colour_in_contourHSV[2]<hsv_color_max[2])
    
    inBlueRange = inHRange*inSRange*inVRange
    
    return inBlueRange

# In[1]: LOAD AND CROP IMAGE AND FEATURES

filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample 6B/Bladder 1 TMA - QATA3_sample6B.tiff"
filepath_featurekngp = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos.tiff"
filepath_featurekngp_2 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos_2.tiff"
filepath_featurekngp_3 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos_7.tiff"
filepath_featurekngp_4 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos_4.tiff"
filepath_featurekngp_5 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos_5.tiff"

filepath_featurekpgp = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos.tiff"
filepath_featurekpgp_2 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos_2.tiff"
filepath_featurekpgp_3 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos_3.tiff"
filepath_featurekpgp_4 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos_4.tiff"
filepath_featurekpgp_5 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos_5.tiff"

filepath_featurekngn = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3neg.tiff"
filepath_featurekngn_2 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3neg_2.tiff"
filepath_featurekngn_3 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3neg_3.tiff"

filepath_featurekpgn = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3neg.tiff"

BGR_fullimg = load_BGR_img(filepath)
BGR_cropimg = BGR_fullimg[2500:3000,2500:3000]

BGR_featureimg_kngp = load_BGR_img(filepath_featurekngp)
BGR_featureimg_kngp_2 = load_BGR_img(filepath_featurekngp_2)
BGR_featureimg_kngp_3 = load_BGR_img(filepath_featurekngp_3)
BGR_featureimg_kngp_4 = load_BGR_img(filepath_featurekngp_4)
BGR_featureimg_kngp_5 = load_BGR_img(filepath_featurekngp_5)

BGR_featureimg_kpgp = load_BGR_img(filepath_featurekpgp)
BGR_featureimg_kpgp_2 = load_BGR_img(filepath_featurekpgp_2)
BGR_featureimg_kpgp_3 = load_BGR_img(filepath_featurekpgp_3)
BGR_featureimg_kpgp_4 = load_BGR_img(filepath_featurekpgp_4)
BGR_featureimg_kpgp_5 = load_BGR_img(filepath_featurekpgp_5)

BGR_featureimg_kngn = load_BGR_img(filepath_featurekngn)
BGR_featureimg_kngn_2 = load_BGR_img(filepath_featurekngn_2)
BGR_featureimg_kngn_3 = load_BGR_img(filepath_featurekngn_3)

BGR_featureimg_kpgn = load_BGR_img(filepath_featurekpgn)

cv2.imshow('Original Image', BGR_cropimg)
cv2.waitKey(1) 

# In[2]: IDENTIFY RED REGION AND FILL IN HOLES

mask_red, mask_nored = create_red_mask(BGR_cropimg)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,25))
mask_closedred = fill_mask_holes(mask_red, kernel)

# In[3]: REMOVE FILLED RED REGION FROM IMAGE

image_nored = removeRedRegionFromImage(BGR_cropimg, mask_closedred)

cv2.imshow('Red Removed Region',image_nored)
cv2.waitKey(1)

# In[4]: APPLY TEMPLATE MATCHING WITHOUT RED REGION

listTemplate_inwhite = [('A', BGR_featureimg_kngp),('B', BGR_featureimg_kngp_2),('G', BGR_featureimg_kngp_3),('D', BGR_featureimg_kngp_4)]#,('E', BGR_featureimg_kngp_5)]
Hits = matchTemplates(listTemplate_inwhite, image_nored, score_threshold=0.55, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
Overlay_inwhite = drawBoxesOnRGB(image_nored, Hits, showLabel=True)

total_inwhite = len(Hits)

listTemplate_blueinwhite = [('*A', BGR_featureimg_kngn),('*B', BGR_featureimg_kngn_2),('*C', BGR_featureimg_kngn_3)]
Hits_blueinwhite = matchTemplates(listTemplate_blueinwhite, image_nored, score_threshold=0.75, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
Overlay_blueinwhite = drawBoxesOnRGB(image_nored, Hits_blueinwhite, showLabel=True)

total_blueinwhite = len(Hits_blueinwhite)

print('\n KRT5 -\n')
print('Number of GATA3+ segments identified:', total_inwhite)
print('Number of GATA3- segments identified:', total_blueinwhite)


cv2.imshow('KRT5- Region', Overlay_inwhite)
cv2.waitKey(1)

cv2.imshow('KRT5- Region GATA3-', Overlay_blueinwhite)
cv2.waitKey(1)

# In[5]: INVERT MASK TO GET ONLY RED REGION

mask_closed_nored = cv2.bitwise_not(mask_closedred)
image_justred = removeRedRegionFromImage(BGR_cropimg, mask_closed_nored)

cv2.imshow('Only Red Region', image_justred)
cv2.waitKey(1) 

# In[6]: APPLY TEMPLATE MATCHING IN RED REGION

listTemplate_inred = [('A+', BGR_featureimg_kpgp),('B+', BGR_featureimg_kpgp_2),('C+', BGR_featureimg_kpgp_3),('D+', BGR_featureimg_kpgp_4),('F+', BGR_featureimg_kpgp_5)]
Hits = matchTemplates(listTemplate_inred, image_justred, score_threshold=0.4, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
Overlay_inred = drawBoxesOnRGB(image_justred, Hits, showLabel=True)

total_inred = len(Hits)

listTemplate_blueinred = [('***', BGR_featureimg_kpgn)]
Hits_blueinred = matchTemplates(listTemplate_blueinred, image_justred, score_threshold=0.55, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
Overlay_blueinred = drawBoxesOnRGB(image_justred, Hits_blueinred, showLabel=True)

total_blueinred = len(Hits_blueinred)

print('\n KRT5 +\n')
print('Number of GATA3+ segments identified:', total_inred)
print('Number of GATA3- segments identified:', total_blueinred)


cv2.imshow('KRT5+ Region', Overlay_inred)
cv2.waitKey(1)

cv2.imshow('KRT5+ Region GATA3-', Overlay_blueinred)
cv2.waitKey(1)


