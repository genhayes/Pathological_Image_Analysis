#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:24:32 2021

@author: genevieve.hayes


BULK ANALYSIS
Main Watershed Pipeline

"""
# In[0]: IMPORT

# Import the necessary packages
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
import pandas as pd

# Import functions
from MAIN_Functions import *

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
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Bladder 1 TMA - Sample 6G.tiff"

#Low res
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6G.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6D.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Sample6B.tiff"
#filepath = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Bladder 1 TMA - QATA3_FULL2 copy.tiff"

import os

directory = os.path.join(os.path.expanduser("~"), "Desktop/ENPH 455 Thesis/Samples")

for filename in os.listdir(directory):
    if filename.endswith(".tiff") or filename.endswith(".tiff"):

        print(os.path.join(directory, filename))
        
        filepath = directory + '/' + filename
    
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
                
                mask_closedred = fill_mask_holes(mask_red, 0) #if kernel = 0, use default
                
                #In[4]: REMOVE FILLED RED REGION FROM IMAGE
                 
                image_nored = removeRedRegionFromImage(BGR_cropimg, mask_closedred)
                
                #cv2.imshow('No red white region',image_nored)
                #cv2.waitKey(1) 
                
                #In[5]: APPLY WATERSHED SEGMENTATION TO IMAGE WIHOUT RED REGION + IDENTIFY THE BROWN RANGE AND BLUE RANGE CELLS (KRTN5-) + REMOVE NOISE
                
                markers, thresh, dist, gray, markersimg = preprocessing_for_watershed(image_nored)
                
                BGR_cropimg_watershed, total, brown, blue = watershedSegmentation_whiteRegion(BGR_cropimg, markers, thresh, dist, gray, markersimg, min_radius_kn, max_radius_kn)
                
                # show the output watershed image
                #cv2.imshow("White Region Watershed Segmented Image", BGR_cropimg_watershed)
                #cv2.waitKey(1)
                
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
                    filename_output = "Outputs_WHR6G/"+str(ind_x)+str(ind_y)+ "processed_img_section.tiff"
                    cv2.imwrite(filename_output, BGR_cropimg_watershed_inred)
                    print('- Image Saved -')
                    
        print('\nIMAGE PROCESSING COMPLETE') 
        print('----     ----    ----    ----')         
        
        # In[]: FINAL CLASSIFICATIONS
             
        print('\nTOTAL KRT5-/GATA3+:', np.sum(TOTAL_kngp))
        print('TOTAL KRT5+/GATA3+:', np.sum(TOTAL_kpgp))    
        print('TOTAL KRT5+/GATA3-:', np.sum(TOTAL_kpgn))
        print('TOTAL KRT5-/GATA3-:', np.sum(TOTAL_kngn))
        
        #filename_save = filename[0:8]+'_Analysis_Outputs.txt'
        filename_save = 'Watershed/Watershed_Analysis_Outputs.txt'
        
        file = open(filename_save,'a') 
     
        file.write('File:')
        file.write(filename+'\n')
        
        file.write('w'+filename[6:8]+'kpgp = ')
        file.write(str(np.sum(TOTAL_kpgp))+'\n')
        
        file.write('w'+filename[6:8]+'kngn = ')
        file.write(str(np.sum(TOTAL_kngn))+'\n')
        
        file.write('w'+filename[6:8]+'kpgn = ')
        file.write(str(np.sum(TOTAL_kpgn))+'\n')

        file.write('w'+filename[6:8]+'kngp = ')
        file.write(str(np.sum(TOTAL_kngp))+'\n')
         
        file.close() 
        
        results = {'Phenotype': ['K+G+','K-G-','K+G-','K-G+'],
        'Num Cells': [np.sum(TOTAL_kpgp),np.sum(TOTAL_kngn),np.sum(TOTAL_kpgn),np.sum(TOTAL_kngp)]
        }
        
        df = pd.DataFrame(results, columns = ['Phenotype', 'Num Cells'])
        df.to_csv('Watershed/Watershed_Batch_Results.csv', mode='a', index = False, header=None)
                
        # In[]: BAR PLOTS
        
        x = np.array(["Sample6G"])
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
