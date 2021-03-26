# -*- coding: utf-8 -*-
"""
Genevieve Hayes
Sept 30, 2020
Initial loading functions for tiff image of core 6B of cancerous urotherlial cells stained for GATA3 and KRT5.
"""

from __future__ import print_function
from PIL import Image
import numpy as np
import cv2 as cv
import numpy as np
import argparse
import random as rng
#import matplotlib.pyplot as plt

#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample 6B/Bladder 1 TMA - QATA3_6B.tiff"
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

# WATERSHED SEGMENTATION
rng.seed(12345)
parser = argparse.ArgumentParser(description='Code for Image Segmentation with Distance Transform and Watershed Algorithm.\
    Sample code showing how to segment overlapping objects using Laplacian filtering, \
    in addition to Watershed and Distance Transformation')
parser.add_argument('--input', help='Path to input image.', default=filepath)
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
# Show source image
print(np.shape(src[1:1000,1:1000]))
src = src[2500:3000,2500:3000]
cv.imshow('Source Image', src)
cv.waitKey(0)
cv.destroyAllWindows()
#src[np.all(src == 255, axis=2)] = 0
# Show output image
#cv.imshow('Black Background Image', src)
# In[]:
kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=np.float32)
# do the laplacian filtering as it is
# well, we need to convert everything in something more deeper then CV_8U
# because the kernel has some negative values,
# and we can expect in general to have a Laplacian image with negative values
# BUT a 8bits unsigned int (the one we are working with) can contain values from 0 to 255
# so the possible negative number will be truncated
imgLaplacian = cv.filter2D(src, cv.CV_32F, kernel)
sharp = np.float32(src)
imgResult = sharp - imgLaplacian
# convert back to 8bits gray scale
imgResult = np.clip(imgResult, 0, 255)
imgResult = imgResult.astype('uint8')
imgLaplacian = np.clip(imgLaplacian, 0, 255)
imgLaplacian = np.uint8(imgLaplacian)
#cv.imshow('Laplace Filtered Image', imgLaplacian)
cv.imshow('New Sharped Image', imgResult)
cv.waitKey(0)
cv.destroyAllWindows()
# In[]:
bw = cv.cvtColor(imgResult, cv.COLOR_BGR2GRAY)
_, bw = cv.threshold(bw, 40, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow('Binary Image', bw)
dist = cv.distanceTransform(bw, cv.DIST_L2, 3)
# Normalize the distance image for range = {0.0, 1.0}
# so we can visualize and threshold it
cv.normalize(dist, dist, 0, 1.0, cv.NORM_MINMAX)
cv.imshow('Distance Transform Image', dist)
cv.waitKey(0)
cv.destroyAllWindows()
# In[]:
_, dist = cv.threshold(dist, 0.4, 1.0, cv.THRESH_BINARY)
# Dilate a bit the dist image
kernel1 = np.ones((3,3), dtype=np.uint8)
dist = cv.dilate(dist, kernel1)
cv.imshow('Peaks', dist)
cv.waitKey(0)
cv.destroyAllWindows()
# In[]:
# Create the CV_8U version of the distance image
# It is needed for findContours()
dist_8u = dist.astype('uint8')
# Find total markers
contours, _ = cv.findContours(dist_8u, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# Create the marker image for the watershed algorithm
markers = np.zeros(dist.shape, dtype=np.int32)
# Draw the foreground markers
for i in range(len(contours)):
    cv.drawContours(markers, contours, i, (i+1), -1)
# Draw the background marker
cv.circle(markers, (5,5), 3, (255,255,255), -1)
cv.imshow('Markers', markers*10000)
# In[]:
# Perform the watershed algorithm
cv.watershed(imgResult, markers)
#mark = np.zeros(markers.shape, dtype=np.uint8)
mark = markers.astype('uint8')
mark = cv.bitwise_not(mark)
# uncomment this if you want to see how the mark
# image looks like at that point
#cv.imshow('Markers_v2', mark)
# Generate random colors
colors = []
for contour in contours:
    colors.append((rng.randint(0,256), rng.randint(0,256), rng.randint(0,256)))
# Create the result image
dst = np.zeros((markers.shape[0], markers.shape[1], 3), dtype=np.uint8)
# Fill labeled objects with random colors
for i in range(markers.shape[0]):
    for j in range(markers.shape[1]):
        index = markers[i,j]
        if index > 0 and index <= len(contours):
            dst[i,j,:] = colors[index-1]
# Visualize the final image
cv.imshow('Final Result', dst)
cv.waitKey()
