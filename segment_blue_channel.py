#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:20:45 2021

@author: genevieve.hayes

SEGMENT CHANNEL BLUE
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
from matplotlib import pyplot as plt


filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample 6B/Bladder 1 TMA - QATA3_sample6B.tiff"


rng.seed(12345)
parser = argparse.ArgumentParser(description='Code for Image Segmentation with Distance Transform and Watershed Algorithm.\
    Sample code showing how to segment overlapping objects using Laplacian filtering, \
    in addition to Watershed and Distance Transformation')
parser.add_argument('--input', help='Path to input image.', default=filepath)
args = parser.parse_args()
src_bgr = cv2.imread(cv2.samples.findFile(args.input))
if src_bgr is None:
    print('Could not open or find the image:', args.input)
    exit(0)
    
# Show source image
print(np.shape(src_bgr[1:1000,1:1000]))
#cv2.imshow('Source Image', src)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#crop image
#cropped_image = src_bgr[3000:3500,3000:3500]
#cropped_image = src_bgr[2500:3000,2500:3000]
cropped_image = src_bgr[800:1600,800:1600]

cv2.imshow("Original Image", cropped_image)
cv2.waitKey()

# In[]:
    
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

# In[]:
    
def removeBlueFromImage(img):
    global img_blueremoved
    
    #Convert image to HSV 
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #hsv_color_min = np.array([90,10,130])
    #hsv_color_max = np.array([255,255,170])
    
    hsv_color_min = np.array([38, 0, 18],np.uint8)
    hsv_color_max = np.array([160, 255, 255],np.uint8)
    
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
    img_blueremoved = np.where(channel2_img[:,:] == [0,0,0], whiteimg, channel2_img) #here we replace black pixels.    
    
    return img_blueremoved

# In[]:
def BGRinBrownRange(img):
    
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hsv_color_min = np.array([-1,70,20]) #identifies brown cells well
    hsv_color_max = np.array([30,255,255])
    
    inRange = hsv_img[(hsv_img[:,1,1]>hsv_color_min[1])*(hsv_img[:,1,1]<hsv_color_max[1])]
    
    return inRange
    

def removeBrownFromImage(img):
    global img_brownremoved
    
    #Convert image to HSV 
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    hsv_color_min = np.array([-1,70,20]) #identifies brown cells well
    hsv_color_max = np.array([30,255,255])

    
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
    img_brownremoved = np.where(channel2_img[:,:] == [0,0,0], whiteimg, channel2_img) #here we replace black pixels.    
    
    return img_brownremoved

# In[]:
    
image_nored = removeRedFromImage(cropped_image)
cv2.imshow("Original Image with Red Colors Removed", image_nored)
cv2.waitKey()

image_noblue = removeBlueFromImage(cropped_image)
cv2.imshow("Original Image with Blue Colors Removed", image_noblue)
cv2.waitKey()

image_nobrown = removeBrownFromImage(cropped_image)
cv2.imshow("Original Image with Brown Colors Removed", image_nobrown)
cv2.waitKey()


# In[]: BGR histogram
    
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([cropped_image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.ylim([0,30000])
plt.xlabel('B,G,R values')
plt.title('BGR Histogram')
plt.show()

# In[]: HSV histogram
    
color = ('g','m','c')
hsv_img = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
for i,col in enumerate(color):
    histr = cv2.calcHist([hsv_img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.ylim([0,30000])
plt.xlabel('H, S, V values')
plt.title('HSV Histogram')
plt.legend(['H', 'S', 'V'])
plt.show()
