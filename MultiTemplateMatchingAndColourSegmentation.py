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

# Import functions
from MAIN_Functions import *

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

mask_closedred = fill_mask_holes(mask_red, 0)

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


