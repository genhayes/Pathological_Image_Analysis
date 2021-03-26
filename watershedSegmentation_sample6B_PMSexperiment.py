#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:51:20 2020

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

increment_swr = 5
increment_cwr = 20

for i in range(0,4):
    spatial_window_radius = 4 + (increment_swr*i)
    for j in range(0,4):
        color_window_radius = 10 + (increment_cwr*j)
        
        figure_title = "Pyramid Mean Shifted Image SWR: " + str(spatial_window_radius) + " ,CWR: "+ str(color_window_radius)
        
        shifted = cv2.pyrMeanShiftFiltering(image, sp = spatial_window_radius, sr = color_window_radius)# 21, 51)
        
        cv2.imshow(figure_title, shifted)
        cv2.waitKey()

