#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 10:56:53 2020

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
#cv2.imshow('Source Image', src)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#crop image
cropped_image = src[2500:3000,2500:3000]

cv2.imshow("Original Image", cropped_image)
cv2.waitKey()

# In[]: Color filter image

#Convert image to HSV 
hsv_img = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)

#hsv_color1 = np.asarray([0, 0, 255])   # white!
#hsv_color2 = np.asarray([18, 255, 255])   # red
#print(hsv_color1)
#print(hsv_color2)

#RED_MIN = np.array([5, 50, 50],np.uint8)
#RED_MAX = np.array([15, 255, 255],np.uint8)
#hsv_color_min = np.array([0, 100, 100],np.uint8) #identifies cells well
#hsv_color_max = np.array([10, 255, 255],np.uint8)
hsv_color_min = np.array([160, 100, 100],np.uint8) #identifies red dye well
hsv_color_max = np.array([179, 255, 255],np.uint8)

#Define threshold color range to filter
mask = cv2.inRange(hsv_img, hsv_color_min, hsv_color_max)

# Bitwise-AND mask and original image
channel1hsv_img = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
ratio = cv2.countNonZero(mask)/(hsv_img.size/3)
print('pixel percentage in channel 1:', np.round(ratio*100, 2))

# get second masked value (background) mask must be inverted
mask_inv = cv2.bitwise_not(mask)
channel2hsv_img = cv2.bitwise_and(hsv_img, hsv_img, mask=mask_inv)
#background = np.full(hsv_img.shape, 255, dtype=np.uint8)
#channel2_img = cv2.bitwise_or(background, background, mask=mask)

cv2.imshow('Mask',mask)
cv2.waitKey(1) 

channel1_img = cv2.cvtColor(channel1hsv_img, cv2.COLOR_HSV2BGR)
cv2.imshow('Masked image channel 1',channel1_img)
cv2.waitKey(1) 

channel2_img = cv2.cvtColor(channel2hsv_img, cv2.COLOR_HSV2BGR)
cv2.imshow('Masked image channel 2',channel2_img)
cv2.waitKey(1) 

whiteimg = np.full(channel2_img.shape, 255, dtype=np.uint8)  # White image  
channel2_imgwhite = np.where(channel2_img[:,:] == [0,0,0], whiteimg, channel2_img)   # This is where we replace black pixels.    
    
cv2.imshow('Masked image channel 2 No Red',channel2_imgwhite)
cv2.waitKey(1) 

# In[]: Filter out red from image function

def removeRedFromImage(img):
    #remove the red range from the image
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

# In[]:

# Fload fill red mask
    
kernel = np.ones((10,10),np.uint8) #can make circular/triangular using ones and zeros #can change shape

# Elliptical Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,25))

def fill_mask_holes(mask, kernel):
    ''' Fill holes in the mask with a defined kernel.
    Kernel can be rectangular (kernel = np.ones((10,10),np.uint8)), 
    cross (kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(20,25))),
    or elliptical (kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,25))).
    '''
    closed_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    return closed_mask

closed = fill_mask_holes(mask, kernel)

cv2.imshow('Filled mask',closed)
cv2.waitKey(1) 
