#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:29:31 2021

@author: genevieve.hayes

Density plot added after pipeline

Helpful resource: https://stackoverflow.com/questions/20105364/how-can-i-make-a-scatter-plot-colored-by-density-in-matplotlib/53865762#53865762

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
from scipy.stats import gaussian_kde
from scipy.interpolate import Rbf
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

def watershedSegmentation_whiteRegion(BGR_cropimg, markers, thresh, dist, gray, markersimg, min_radius):
    max_radius = 11
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
    x = np.zeros(len(np.unique(labels))+1, dtype="uint8")
    y = np.zeros(len(np.unique(labels))+1, dtype="uint8")
    x_cells = np.array([500,0,0, 500])
    y_cells = np.array([0,500,0,500])
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
        ((x[val], y[val]), r[val]) = cv2.minEnclosingCircle(c)
    
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
                x_cells = np.append(x_cells, x[val])
                y_cells = np.append(y_cells, y[val])
                #cv2.putText(cropped_image, "#{}".format(mean_colour_in_contourBRG), (int(x) - 10, int(y)),
                #ONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
                brown = brown+1;
                #Blue
            elif inBlueRange > 0.5:
                cv2.drawContours(BGR_cropimg, cnts, -1, (255,0,0), 1)
                x_cells = np.append(x_cells, x[val])
                y_cells = np.append(y_cells, y[val])
                #cv2.putText(cropped_image, "#{}".format(mean_colour_in_contourBRG), (int(x) - 10, int(y)),
                #ONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
                blue = blue+1;
 
        markersimg = cv2.circle(markersimg,(int(x[val]), int(y[val])), int(radius), 255, -1)

    return BGR_cropimg, total, brown, blue, x_cells, y_cells

def watershedSegmentation_redRegion(img, markers, thresh, dist, gray, markersimg, min_radius):
    max_radius = 11
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
    x = np.zeros(len(np.unique(labels))+1, dtype="uint8")
    x_cells = np.array([500,0,0, 500])
    y_cells = np.array([0,500,0,500])
    y = np.zeros(len(np.unique(labels))+1, dtype="uint8")
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
        ((x[val], y[val]), r[val]) = cv2.minEnclosingCircle(c)
    
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
                cv2.drawContours(img, cnts, -1, (1,200,200), 1)
                #cv2.putText(cropped_image, "#{}".format(mean_colour_in_contourBRG), (int(x) - 10, int(y)),
                #ONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
                brown = brown+1;
                x_cells = np.append(x_cells, x[val])
                y_cells = np.append(y_cells, y[val])
                #Blue
            #elif inBlueRange > 0.5:
                #cv2.drawContours(img, cnts, -1, (255,0,0), 1)
                ##cv2.putText(cropped_image, "#{}".format(mean_colour_in_contourBRG), (int(x) - 10, int(y)),
                ##ONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
                #blue = blue+1;
 
        markersimg = cv2.circle(markersimg,(int(x[val]), int(y[val])), int(radius), 255, -1)

    return img, total, brown, blue, x_cells, y_cells


# In[1]: LOAD IMAGE

#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample 6B/Bladder 1 TMA - QATA3_sample6B.tiff"

filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Bladder 1 TMA - QATA3_FULL2 copy.tiff"
BGR_fullimg = load_BGR_img(filepath)

# In[2]: CROP IMAGE

#BGR_cropimg = BGR_fullimg[2500:3000,2500:3000]
BGR_cropimg = BGR_fullimg[3200:3700,15300:15800]

#BGR_cropimg = BGR_fullimg[1800:2300,8500:9000]
#BGR_cropimg = BGR_fullimg[1000:1500,1000:1500]
BGR_cropimg_duplicate = BGR_cropimg

cv2.imshow('Original Image', BGR_cropimg)
cv2.waitKey(1) 

# In[3]: IDENTIFY RED REGION AND FILL IN HOLES

mask_red, mask_nored = create_red_mask(BGR_cropimg)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,25))
mask_closedred = fill_mask_holes(mask_red, kernel)

# In[4]: REMOVE FILLED RED REGION FROM IMAGE

image_nored = removeRedRegionFromImage(BGR_cropimg, mask_closedred)

cv2.imshow('No red white region',image_nored)
cv2.waitKey(1) 

# In[5]: APPLY WATERSHED SEGMENTATION TO IMAGE WIHOUT RED REGION + IDENTIFY THE BROWN RANGE AND BLUE RANGE CELLS (KRTN5-) + REMOVE NOISE

markers, thresh, dist, gray, markersimg = preprocessing_for_watershed(image_nored)

BGR_cropimg_watershed, total, brown, blue, x_inwhite, y_inwhite = watershedSegmentation_whiteRegion(BGR_cropimg, markers, thresh, dist, gray, markersimg, 6)

# show the output watershed image
cv2.imshow("White Region Watershed Segmented Image", BGR_cropimg_watershed)
cv2.waitKey(1)

print('Number of segments larger than radius 6:', total)
print('Number of brown segments larger than radius 6:', brown)
print('Number of blue segments larger than radius 6:', blue)

# In[6]: INVERT MASK TO GET ONLY RED REGION

mask_closed_nored = cv2.bitwise_not(mask_closedred)
image_justred = removeRedRegionFromImage(BGR_cropimg, mask_closed_nored)

cv2.imshow('Red region', image_justred)
cv2.waitKey(1) 

# In[7]: REMOVE RED STAIN FROM RED REGION IMAGE

mask_red_noredstain, mask_red_redstain = create_light_red_mask(image_justred)

image_redregion_noredstain = removeRedRegionFromImage(image_justred, mask_red_noredstain)

cv2.imshow('No red red region', image_redregion_noredstain)
cv2.waitKey(1) 

# In[8]: APPLY WATERSHED SEGMENTATION TO RED REGION WITHOUT STAIN + IDENTIFY THE BROWN RANGE AND BLUE RANGE CELLS (KRT5+) + REMOVE NOISE

markers_red, thresh_red, dist_red, gray_red, markersimg_red = preprocessing_for_watershed(image_redregion_noredstain)

BGR_cropimg_watershed_inred, total_inred, brown_inred, blue_inred, x_inred, y_inred = watershedSegmentation_redRegion(BGR_cropimg_duplicate, markers_red, thresh_red, dist_red, gray_red, markersimg_red, 3)

cv2.imshow('Duplicate of original image', BGR_cropimg_duplicate)
cv2.waitKey(1) 

# show the output watershed image
cv2.imshow("Red Region Watershed Segmented Image", BGR_cropimg_watershed_inred)
cv2.waitKey(1)

print('Number of segments larger than radius 6:', total_inred)
print('Number of brown segments larger than radius 6:', brown_inred)
print('Number of blue segments larger than radius 6:', blue_inred)

# In[9]: PLOT DENSITY PLOTS (in white and red)

# Calculate the point density
#y_inwhite = np.max(y_inwhite) - y_inwhite #reverse y
#x_inwhite = np.max(x_inwhite) - x_inwhite #reverse x
xy_inwhite = np.vstack([x_inwhite,y_inwhite])
z_inwhite = gaussian_kde(xy_inwhite)(xy_inwhite)

# Remove 3 initial buffer points
#x_inwhite = x_inwhite[2:]
#y_inwhite = y_inwhite[2:]
#z_inwhite = z_inwhite[2:]

# Sort the points by density, so that the densest points are plotted last
idx = z_inwhite.argsort()
x_inwhite, y_inwhite, z_inwhite = x_inwhite[idx], y_inwhite[idx], z_inwhite[idx]

fig, ax = plt.subplots()
plt.scatter(x_inwhite[4:], y_inwhite[4:], c=z_inwhite[4:], s=50, edgecolor='')
plt.colorbar()
plt.title("Density Plot KRT5-")
plt.show()

# In[9]: PLOT DENSITY PLOTS (in red)

# Calculate the point density
#y_inred = np.max(y_inred) - y_inred #reverse y
#x_inred = np.max(x_inred) - x_inred #reverse y
xy_inred = np.vstack([x_inred,y_inred])
z_inred = gaussian_kde(xy_inred)(xy_inred)

# Remove 3 initial buffer points
#x_inred = x_inred[2:]
#y_inred = y_inred[2:]
#z_inred = z_inred[2:]

# Sort the points by density, so that the densest points are plotted last
idx = z_inred.argsort()
x_inred, y_inred, z_inred = x_inred[idx], y_inred[idx], z_inred[idx]

fig, ax = plt.subplots()
plt.scatter(x_inred[4:], y_inred[4:], c=z_inred[4:], s=50, edgecolor='')
plt.colorbar()
plt.title("Density Plot KRT5+")
plt.xlabel("x pixel")
plt.ylabel("y pixel")
#plt.xlim([0,250])
#plt.ylim([0,250])
plt.show()

# In[9]: PLOT DENSITY PLOTS (in red)

# Make a grid with spacing 0.002.
#grid_x_white, grid_y_white = np.mgrid[np.min(x_inwhite):np.max(x_inwhite):1,np.min(y_inwhite):np.max(y_inwhite):1]
#grid_x_white, grid_y_white = np.mgrid[np.min(BGR_cropimg[:,0,0]):np.max(BGR_cropimg[:,0,0]):1,np.min(BGR_cropimg[0,:,0]):np.max(BGR_cropimg[0,:,0]):1]
grid_x_white, grid_y_white = np.mgrid[0:500:1,0:500:1]

# Make an n-dimensional interpolator.
try:
    rbfi_white = Rbf(x_inwhite, y_inwhite, z_inwhite, smooth=2)# Predict on the regular grid.
    di_white = rbfi_white(grid_x_white, grid_y_white)
    plt.imshow(di_white, cmap='viridis')
    plt.colorbar()
    #plt.clim(0,1)
    plt.xlabel("x pixel")
    plt.ylabel("y pixel")
    #plt.xlim([0,250])
    #plt.ylim([0,250])
    plt.title("Density Plot KRT5-")
    plt.show()
except: 
    print("\n No KRT5- cells identified")


# In[9]: PLOT DENSITY PLOTS (in red)

# Make a grid with spacing 0.002.
#grid_x, grid_y = np.mgrid[np.min(x_inred):np.max(x_inred):0.5,np.min(y_inred):np.max(y_inred):0.5]
grid_x, grid_y = np.mgrid[0:500:1,0:500:1]

try:
    # Make an n-dimensional interpolator.
    rbfi = Rbf(x_inred, y_inred, z_inred, smooth=2)

    # Predict on the regular grid.
    di = rbfi(grid_x, grid_y)
    plt.imshow(di,cmap='viridis')
    plt.colorbar()
    #plt.clim(0,1)
    plt.xlabel("x pixel")
    plt.ylabel("y pixel")
    #plt.xlim([0,250])
    #plt.ylim([0,250])
    plt.title("Density Plot KRT5+")
    plt.show()
except: 
    print("\n No KRT5+ cells identified")
    
# In[]:
    
# def using_hist2d(ax, x, y, bins=(50, 50)):
#     # https://stackoverflow.com/a/20105673/3015186
#     # Answer by askewchan
#     ax.hist2d(x, y, bins, cmap=plt.cm.jet)


# plt.hist2d(x_inred, y_inred, (5, 5), cmap=plt.cm.jet)
# plt.colorbar()
# plt.show()

# plt.hist2d(x_inwhite, y_inwhite, (5, 5), cmap=plt.cm.jet)
# plt.colorbar()
# plt.show()

# In[]:
# import mpl_scatter_density # adds projection='scatter_density'
# from matplotlib.colors import LinearSegmentedColormap

# # "Viridis-like" colormap with white background
# white_viridis = LinearSegmentedColormap.from_list('white_viridis', [
#     (0, '#ffffff'),
#     (1e-20, '#440053'),
#     (0.2, '#404388'),
#     (0.4, '#2a788e'),
#     (0.6, '#21a784'),
#     (0.8, '#78d151'),
#     (1, '#fde624'),
# ], N=256)

# def using_mpl_scatter_density(fig, x, y):
#     ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
#     density = ax.scatter_density(x, y, cmap=plt.cm.jet)
#     fig.colorbar(density, label='Number of points per pixel')

# fig = plt.figure()
# using_mpl_scatter_density(fig, x_inwhite[4:], y_inwhite[4:])
# plt.show()

    
    