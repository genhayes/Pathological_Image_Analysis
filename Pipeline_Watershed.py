#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:24:32 2021

@author: genevieve.hayes

Watershed Pipeline Functions

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
import matplotlib

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
    
    hsv_color_min = np.array([-1,50,20]) #identifies brown cells well
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

def watershedSegmentation_whiteRegion(BGR_cropimg, markers, thresh, dist, gray, markersimg, min_radius, max_radius):
    colour_threshold = 160#120 #COLOUR THRESHOLD

    HSV_cropimg = cv2.cvtColor(BGR_cropimg, cv2.COLOR_BGR2HSV)
    image = 255-image_nored # Invert input image
    #Identify each rsegmented region
    labels = watershed(-dist, markers, mask=thresh)
    print("{} unique segments found".format(len(np.unique(labels)) - 1))

    # loop over the unique labels returned by the Watershed algorithm
    maskim = np.zeros(np.shape(image), dtype="uint8")
    val = 0
    radius = 6

    r = np.zeros(len(np.unique(labels))+1, dtype="uint8")
    mean_coloursBRG = np.zeros((len(np.unique(labels))+1,4), dtype="uint8")
    
    total = 0;
    brown = 0;
    blue = 0;
    
    for label in np.unique(labels):
        #if the label is zero, we are examining the 'background' so simply ignore it
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
        #draw a circle enclosing the object
        ((x, y), r[val]) = cv2.minEnclosingCircle(c)
    
        #Get mean colour inside each contour
        mean_colour_in_contourBRG = cv2.mean(BGR_cropimg,mask)
        mean_colour_in_contourHSV = cv2.mean(HSV_cropimg,mask)
        mean_coloursBRG[val, :] = mean_colour_in_contourBRG
    
        intensity = np.around(mean_colour_in_contourBRG[0],0)
    
        inBrownRange = BGRinBrownRange_whiteRegion(mean_colour_in_contourHSV)
        inBlueRange = BGRinBlueRange_whiteRegion(mean_colour_in_contourHSV)
    
        if r[val] > min_radius and r[val] < max_radius:
            total = total+1;
            #Draw Contours
            #Green
            if inBrownRange > 0.5:
                cv2.drawContours(BGR_cropimg, cnts, -1, (0,255,0), 1)
                #cv2.putText(cropped_image, "#{}".format(mean_colour_in_contourBRG), (int(x) - 10, int(y)),
                #ONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
                brown = brown+1;
                #Blue
            elif inBlueRange > 0.5:
                cv2.drawContours(BGR_cropimg, cnts, -1, (255,0,0), 1)
                #cv2.putText(cropped_image, "#{}".format(mean_colour_in_contourBRG), (int(x) - 10, int(y)),
                #ONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
                blue = blue+1;
 
        markersimg = cv2.circle(markersimg,(int(x), int(y)), int(radius), 255, -1)

    return BGR_cropimg, total, brown, blue

def watershedSegmentation_redRegion(img, markers, thresh, dist, gray, markersimg, min_radius, max_radius):
    colour_threshold = 160#120 #COLOUR THRESHOLD

    HSV_cropimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    image = 255-image_nored # Invert input image
    #Identify each rsegmented region
    labels = watershed(-dist, markers, mask=thresh)
    print("{} unique segments found".format(len(np.unique(labels)) - 1))

    # loop over the unique labels returned by the Watershed algorithm
    maskim = np.zeros(np.shape(image), dtype="uint8")
    val = 0
    radius = 6

    r = np.zeros(len(np.unique(labels))+1, dtype="uint8")
    mean_coloursBRG = np.zeros((len(np.unique(labels))+1,4), dtype="uint8")
    
    total = 0;
    brown = 0;
    blue = 0;
    
    for label in np.unique(labels):
        #if the label is zero, we are examining the 'background' so simply ignore it
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
        #draw a circle enclosing the object
        ((x, y), r[val]) = cv2.minEnclosingCircle(c)
    
        #Get mean colour inside each contour
        mean_colour_in_contourBRG = cv2.mean(img,mask)
        mean_colour_in_contourHSV = cv2.mean(HSV_cropimg,mask)
        mean_coloursBRG[val, :] = mean_colour_in_contourBRG
    
        intensity = np.around(mean_colour_in_contourBRG[0],0)
    
        inBrownRange = BGRinBrownRange_redRegion(mean_colour_in_contourHSV)
        inBlueRange = BGRinBlueRange_redRegion(mean_colour_in_contourHSV)
    
        if r[val] > min_radius and r[val] < max_radius:
            total = total+1;
            #Draw Contours
            #Green
            if inBrownRange > 0.5:
                cv2.drawContours(img, cnts, -1, (0,255,0), 1)
                #cv2.putText(cropped_image, "#{}".format(mean_colour_in_contourBRG), (int(x) - 10, int(y)),
                #ONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
                brown = brown+1;
                #Blue
            elif inBlueRange > 0.5:
                cv2.drawContours(img, cnts, -1, (255,0,0), 1)
                ##cv2.putText(cropped_image, "#{}".format(mean_colour_in_contourBRG), (int(x) - 10, int(y)),
                ##ONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
                blue = blue+1;
 
        markersimg = cv2.circle(markersimg,(int(x), int(y)), int(radius), 255, -1)

    return img, total, brown, blue
# In[1]: LOAD IMAGE

# Set SAVEIMG to 1 to save images
SAVEIMG = 0

# high res parameters
min_radius_kn = 3
max_radius_kn = 18
min_radius_kp = 3
max_radius_kp = 18

## low res parameters
#min_radius_kn = 3
#max_radius_kn = 16
#min_radius_kp = 3
#max_radius_kp = 18

# SET INPUT FILEPATH
#High res
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample 6B/Bladder 1 TMA - QATA3_sample6B.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Bladder 1 TMA - Sample 6D.tiff"
filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Bladder 1 TMA - Sample 6G.tiff"

#Low res
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6G.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6D.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6B.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Bladder 1 TMA - QATA3_FULL2 copy.tiff"
BGR_fullimg = load_BGR_img(filepath)

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
        
        #In[5]: APPLY WATERSHED SEGMENTATION TO IMAGE WIHOUT RED REGION + IDENTIFY THE BROWN RANGE AND BLUE RANGE CELLS (KRTN5-) + REMOVE NOISE
        
        markers, thresh, dist, gray, markersimg = preprocessing_for_watershed(image_nored)
        
        BGR_cropimg_watershed, total, brown, blue = watershedSegmentation_whiteRegion(BGR_cropimg, markers, thresh, dist, gray, markersimg, min_radius_kn, max_radius_kn)
        
        # show the output watershed image
        cv2.imshow("White Region Watershed Segmented Image", BGR_cropimg_watershed)
        cv2.waitKey(1)
        
        print('\n KRT5 -')
        print('Number of segments larger than radius 6:', total)
        print('Number of brown segments larger than radius 6:', brown)
        print('Number of blue segments larger than radius 6:', blue)
        
        #In[6]: INVERT MASK TO GET ONLY RED REGION
        
        mask_closed_nored = cv2.bitwise_not(mask_closedred)
        image_justred = removeRedRegionFromImage(BGR_cropimg, mask_closed_nored)
        
        cv2.imshow('Red region', image_justred)
        cv2.waitKey(1) 
        
        #In[7]: REMOVE RED STAIN FROM RED REGION IMAGE
        
        mask_red_noredstain, mask_red_redstain = create_light_red_mask(image_justred)
        
        image_redregion_noredstain = removeRedRegionFromImage(image_justred, mask_red_noredstain)
        
        cv2.imshow('No red red region', image_redregion_noredstain)
        cv2.waitKey(1) 
        
        #In[8]: APPLY WATERSHED SEGMENTATION TO RED REGION WITHOUT STAIN + IDENTIFY THE BROWN RANGE AND BLUE RANGE CELLS (KRT5+) + REMOVE NOISE
        
        markers_red, thresh_red, dist_red, gray_red, markersimg_red = preprocessing_for_watershed(image_redregion_noredstain)
        
        BGR_cropimg_watershed_inred, total_inred, brown_inred, blue_inred = watershedSegmentation_redRegion(BGR_cropimg_duplicate, markers_red, thresh_red, dist_red, gray_red, markersimg_red, min_radius_kp, max_radius_kp)
        
        cv2.imshow('Duplicate of original image', BGR_cropimg_duplicate)
        cv2.waitKey(1) 
        
        # show the output watershed image
        cv2.imshow("Total Watershed Segmented Image", BGR_cropimg_watershed_inred)
        cv2.waitKey(1)
    

        print('\n KRT5 +')
        print('Number of segments larger than radius 6:', total_inred)
        print('Number of brown segments larger than radius 6:', brown_inred)
        print('Number of blue segments larger than radius 6:', blue_inred)
        
        TOTAL_kngn = np.append(TOTAL_kngn, blue)
        TOTAL_kngp = np.append(TOTAL_kngp, brown)
        TOTAL_kpgp = np.append(TOTAL_kpgp, brown_inred)
        TOTAL_kpgn = np.append(TOTAL_kpgn, blue_inred)
        
        if SAVEIMG == 1:
            filename_output = "Outputs/"+str(ind_x)+str(ind_y)+ "processed_img_section.tiff"
            cv2.imwrite(filename_output, BGR_cropimg_watershed_inred)
            print('- Image Saved -')
            
print('\nIMAGE PROCESSING COMPLETE') 
print('----     ----    ----    ----')         

# In[]: FINAL CLASSIFICATIONS
     
print('\nTOTAL KRT5-/GATA3+:', np.sum(TOTAL_kngp))
print('TOTAL KRT5+/GATA3+:', np.sum(TOTAL_kpgp))    
print('TOTAL KRT5+/GATA3-:', np.sum(TOTAL_kpgn))
print('TOTAL KRT5-/GATA3-:', np.sum(TOTAL_kngn))
        
# In[]: BAR PLOTS

x = np.array(["Sample6B"])
y = np.array([np.sum(TOTAL_kngp),np.sum(TOTAL_kngn),np.sum(TOTAL_kpgp),np.sum(TOTAL_kpgn)])
width = 0.2

matplotlib.rc('font', serif='Helvetica Neue')
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4.5, 5.5)

#plt.bar(x,y)
p1 = plt.bar(x, y[0], width, color='g')
p2 = plt.bar(x, y[1], width, bottom=y[0], color='c')
p3 = plt.bar(x, y[2], width, bottom=y[0]+y[1], color='r')
p4 = plt.bar(x, y[3], width, bottom=y[0]+y[1]+y[2], color='b')
plt.ylabel("Number of Cells Identified")
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
plt.show()
