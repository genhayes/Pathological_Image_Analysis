#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:22:46 2021

@author: genevieve.hayes

Template Matching Pipeline

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
import pandas as pd
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

SAVEIMG = 0

#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample 6B/Bladder 1 TMA - QATA3_sample6B.tiff"
filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6B.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6G.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6D.tiff"
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

BGR_fullimg = load_BGR_img(filepath)
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

cv2.imshow('Full image', BGR_fullimg)
cv2.waitKey(1) 

Nx, Ny, w = np.shape(BGR_fullimg)

x_iterations = np.floor(Nx/500)
y_iterations = np.floor(Ny/500)

TOTAL_kngn = np.array([])
TOTAL_kngp = np.array([])
TOTAL_kpgn = np.array([])
TOTAL_kpgp = np.array([])


#In[2]: CROP IMAGE
for ind_x in range(0, int(x_iterations)):
    for ind_y in range(0, int(y_iterations)):
        BGR_cropimg = BGR_fullimg[ind_x*500:(ind_x*500+500),ind_y*500:(ind_y*500+500)]
        BGR_cropimg_duplicate = BGR_cropimg
        
        cv2.imshow('Original Image', BGR_cropimg)
        cv2.waitKey(1) 
        
        print("------------------------------------------------- ")
        print("\nImage Coordinates: ",ind_x*500,ind_y*500)
        
        #In[3]: IDENTIFY RED REGION AND FILL IN HOLES
        
        mask_red, mask_nored = create_red_mask(BGR_cropimg)
        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,25))
        mask_closedred = fill_mask_holes(mask_red, kernel)
        
        #In[4]: REMOVE FILLED RED REGION FROM IMAGE
        
        image_nored = removeRedRegionFromImage(BGR_cropimg, mask_closedred)
        
        cv2.imshow('No red white region',image_nored)
        cv2.waitKey(1) 
        
        #In[4]: APPLY TEMPLATE MATCHING WITHOUT RED REGION
        
        listTemplate_inwhite = [('A', BGR_featureimg_kngp),('B', BGR_featureimg_kngp_2),('G', BGR_featureimg_kngp_3),('D', BGR_featureimg_kngp_4)]#,('E', BGR_featureimg_kngp_5)]
        Hits = matchTemplates(listTemplate_inwhite, image_nored, score_threshold=0.55, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
        Overlay_inwhite = drawBoxesOnRGB(image_nored, Hits, showLabel=True)
        
        total_inwhite = len(Hits)
        
        print('\n KRT5 -\n')
        print('Number of segments identified:', total_inwhite)
        
        cv2.imshow('KRT5- Region', Overlay_inwhite)
        cv2.waitKey(1)
        
        #In[6]: INVERT MASK TO GET ONLY RED REGION
        
        mask_closed_nored = cv2.bitwise_not(mask_closedred)
        image_justred = removeRedRegionFromImage(BGR_cropimg, mask_closed_nored)
        
        cv2.imshow('Red region', image_justred)
        cv2.waitKey(1) 
        
        #In[6]: APPLY TEMPLATE MATCHING IN RED REGION
        
        listTemplate_inred = [('A+', BGR_featureimg_kpgp),('B+', BGR_featureimg_kpgp_2),('C+', BGR_featureimg_kpgp_3),('D+', BGR_featureimg_kpgp_4),('F+', BGR_featureimg_kpgp_5)]
        Hits_inred = matchTemplates(listTemplate_inred, image_justred, score_threshold=0.4, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
        Overlay_inred = drawBoxesOnRGB(image_justred, Hits_inred, showLabel=True)
        
        total_inred = len(Hits_inred)
        
        print('\n KRT5 +\n')
        print('Number of segments identified:', total_inred)
        
        cv2.imshow('KRT5+ Region', Overlay_inred)
        cv2.waitKey(1)
        
        Total_overlay = drawBoxesOnRGB(BGR_cropimg, pd.concat([Hits,Hits_inred]), showLabel=True)
        cv2.imshow('KRT5+ Region', Total_overlay)
        cv2.waitKey(1)
        
        #TOTAL_kngn = np.append(TOTAL_kngn, blue)
        TOTAL_kngp = np.append(TOTAL_kngp, total_inwhite)
        TOTAL_kpgn = np.append(TOTAL_kpgn, total_inred)
        #TOTAL_kpgp = np.append(TOTAL_kpgp, blue_inred)
        
        if SAVEIMG == 1:
            filename_output = "Outputs/"+str(ind_x)+str(ind_y)+ "processed_img_section.tiff"
            cv2.imwrite(filename_output, Total_overlay)
            print('- Image Saved -')
            
print('\nIMAGE PROCESSING COMPLETE') 
print('----     ----    ----    ----')         
        
print('\nTOTAL KRT5-/GATA3+:', np.sum(TOTAL_kngp))
print('TOTAL KRT5+/GATA3+:', np.sum(TOTAL_kpgp))    
print('TOTAL KRT5+/GATA3-:', np.sum(TOTAL_kpgn))
print('TOTAL KRT5-/GATA3-:', np.sum(TOTAL_kngn))
        
        
