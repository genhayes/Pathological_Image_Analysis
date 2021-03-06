#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:24:32 2021

@author: genevieve.hayes

BULK ANALYSIS
Main Combined Pipeline

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
from MTM import matchTemplates, drawBoxesOnRGB

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

filepath_featurekngp = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos.tiff"
filepath_featurekngp_2 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos_2.tiff"
filepath_featurekngp_3 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos_7.tiff"
filepath_featurekngp_4 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3pos_4.tiff"

filepath_featurekpgp = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos.tiff"
filepath_featurekpgp_2 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos_2.tiff"
filepath_featurekpgp_3 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos_3.tiff"
filepath_featurekpgp_4 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos_4.tiff"
filepath_featurekpgp_5 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3pos_5.tiff"

filepath_featurekngn = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3neg.tiff"
filepath_featurekngn_2 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3neg_2.tiff"
filepath_featurekngn_3 = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5neg_gata3neg_3.tiff"

filepath_featurekpgn = "/Users/genevieve.hayes/Desktop/ENPH 455 Thesis/Features/krt5pos_gata3neg.tiff"


BGR_featureimg_kngp = load_BGR_img(filepath_featurekngp)
BGR_featureimg_kngp_2 = load_BGR_img(filepath_featurekngp_2)
BGR_featureimg_kngp_3 = load_BGR_img(filepath_featurekngp_3)
BGR_featureimg_kngp_4 = load_BGR_img(filepath_featurekngp_4)

BGR_featureimg_kpgp = load_BGR_img(filepath_featurekpgp)
BGR_featureimg_kpgp_2 = load_BGR_img(filepath_featurekpgp_2)
BGR_featureimg_kpgp_3 = load_BGR_img(filepath_featurekpgp_3)
BGR_featureimg_kpgp_4 = load_BGR_img(filepath_featurekpgp_4)
BGR_featureimg_kpgp_5 = load_BGR_img(filepath_featurekpgp_5)

BGR_featureimg_kngn = load_BGR_img(filepath_featurekngn)
BGR_featureimg_kngn_2 = load_BGR_img(filepath_featurekngn_2)
BGR_featureimg_kngn_3 = load_BGR_img(filepath_featurekngn_3)

BGR_featureimg_kpgn = load_BGR_img(filepath_featurekpgn)


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
                
                mask_closedred = fill_mask_holes(mask_red, np.array([0,0]))
                
                
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
                
                BGR_cropimg_watershed_inred, total_inred, brown_inred, total_blueinred = watershedSegmentation_redRegion(BGR_cropimg_duplicate, markers_red, thresh_red, dist_red, gray_red, markersimg_red, min_radius_kp, max_radius_kp)
                
                # show the output watershed image
                cv2.imshow("Total Watershed Segmented Image", BGR_cropimg_watershed_inred)
                cv2.waitKey(1)
                
                #plt.subplot(1, 2, 1)
                #plt.imshow(BGR_cropimg_watershed_inred)
                #plt.subplot(1, 2, 2)
                #plt.imshow(Overlay_inwhite)
                #plt.show()
                
                #In[4]: REMOVE FILLED RED REGION FROM IMAGE
                
                image_nored = removeRedRegionFromImage(BGR_cropimg, mask_closedred)
                
                cv2.imshow('No red white region',image_nored)
                cv2.waitKey(1) 
                
                #In[4]: APPLY TEMPLATE MATCHING WITHOUT RED REGION
                
                listTemplate_inwhite = [('A', BGR_featureimg_kngp),('B', BGR_featureimg_kngp_2),('G', BGR_featureimg_kngp_3),('D', BGR_featureimg_kngp_4)]#,('E', BGR_featureimg_kngp_5)]
                Hits = matchTemplates(listTemplate_inwhite, image_nored, score_threshold=0.55, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
                Overlay_inwhite = drawBoxesOnRGB(BGR_cropimg_watershed_inred, Hits, showLabel=True)
                
                total_inwhite = len(Hits)
                
                listTemplate_blueinwhite = [('*A', BGR_featureimg_kngn),('*B', BGR_featureimg_kngn_2),('*C', BGR_featureimg_kngn_3)]
                Hits_blueinwhite = matchTemplates(listTemplate_blueinwhite, image_nored, score_threshold=0.75, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
                Overlay_blueinwhite = drawBoxesOnRGB(BGR_cropimg_watershed_inred, Hits_blueinwhite, showLabel=True)
                
                total_blueinwhite = len(Hits_blueinwhite)
                
                print('\n KRT5 -\n')
                print('Number of GATA3+ segments identified:', total_inwhite)
                print('Number of GATA3- segments identified:', total_blueinwhite)
                
                cv2.imshow('KRT5- Region', Overlay_inwhite)
                cv2.waitKey(1)
                
                #combined_img = cv2.hconcat((BGR_cropimg_watershed_inred, Overlay_inwhite))
                #cv2.imshow("Combined Segmentation Images", combined_img)
                #cv2.waitKey(1) 
        
                
                print('\n KRT5 +\n')
                print('Number of GATA3+ segments identified:', total_inred)
                print('Number of GATA3- segments identified:', total_blueinred)
                
        
                TOTAL_kngn = np.append(TOTAL_kngn, total_blueinwhite)
                TOTAL_kngp = np.append(TOTAL_kngp, total_inwhite)
                TOTAL_kpgp = np.append(TOTAL_kpgp, total_inred)
                TOTAL_kpgn = np.append(TOTAL_kpgn, total_blueinred)
                
                if SAVEIMG == 1:
                    filename_output = "Outputs_CHR6G/"+str(ind_x)+str(ind_y)+ "processed_img_section.tiff"
                    cv2.imwrite(filename_output, Overlay_inwhite)
                    print('\n- Image Saved -')
                                    
                    print('\nIMAGE PROCESSING COMPLETE') 
                    print('----     ----    ----    ----')         
        
        # In[]: FINAL CLASSIFICATIONS
             
        print('\nTOTAL KRT5-/GATA3+:', np.sum(TOTAL_kngp))
        print('TOTAL KRT5+/GATA3+:', np.sum(TOTAL_kpgp))    
        print('TOTAL KRT5+/GATA3-:', np.sum(TOTAL_kpgn))
        print('TOTAL KRT5-/GATA3-:', np.sum(TOTAL_kngn))
        
        #filename_save = filename[0:8]+'_Analysis_Outputs.txt'
        filename_save = 'Combined/Combined_Analysis_Outputs.txt'
        
        file = open(filename_save,'a') 
     
        file.write('#File:')
        file.write(filename+'\n')
        
        file.write('tm'+filename[6:8]+'kpgp = ')
        file.write(str(np.sum(TOTAL_kpgp))+'\n')
        
        file.write('tm'+filename[6:8]+'kngn = ')
        file.write(str(np.sum(TOTAL_kngn))+'\n')
        
        file.write('tm'+filename[6:8]+'kpgn = ')
        file.write(str(np.sum(TOTAL_kpgn))+'\n')

        file.write('tm'+filename[6:8]+'kngp = ')
        file.write(str(np.sum(TOTAL_kngp))+'\n')
         
        file.close() 
        
        results = {'Phenotype': ['K+G+','K-G-','K+G-','K-G+'],
        'Num Cells': [np.sum(TOTAL_kpgp),np.sum(TOTAL_kngn),np.sum(TOTAL_kpgn),np.sum(TOTAL_kngp)]
        }
        
        df = pd.DataFrame(results, columns = ['Phenotype', 'Num Cells'])
        df.to_csv('Combined/Combined_Batch_Results.csv', mode='a', index = False, header=None)
                
        # In[]: BAR PLOTS
        
        # x = np.array(["Sample6G"])
        # y = np.array([np.sum(TOTAL_kngp),np.sum(TOTAL_kngn),np.sum(TOTAL_kpgp),np.sum(TOTAL_kpgn)])
        # width = 0.2
        
        # matplotlib.rc('font', serif='Helvetica Neue')
        # matplotlib.rc('text', usetex='false')
        # matplotlib.rcParams.update({'font.size': 16})
        
        # fig = matplotlib.pyplot.gcf()
        # fig.set_size_inches(4.5, 5.5)
        
        # #plt.bar(x,y)
        # p1 = plt.bar(x, y[0], width, color='g')
        # p2 = plt.bar(x, y[1], width, bottom=y[0], color='c')
        # p3 = plt.bar(x, y[2], width, bottom=y[0]+y[1], color='r')
        # p4 = plt.bar(x, y[3], width, bottom=y[0]+y[1]+y[2], color='b')
        # plt.ylabel("Number of Cells Identified")
        # plt.legend((p1[0], p2[0], p3[0], p4[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
        # plt.show()
