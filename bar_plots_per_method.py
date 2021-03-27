#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:38:42 2021

@author: genevieve.hayes

Bar plots per method
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# In[]: WATERSHED
width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6.5, 5.5)

#Sample 6B
B_kngp_w =  2340.0
B_kpgp_w =  3509.0
B_kpgn_w = 80.0
B_kngn_w = 1048
xB_w = np.array(["Sample 6B"])
yB_w = np.array([B_kngp_w,B_kngn_w,B_kpgp_w,B_kpgn_w])
p1B_w = plt.bar(xB_w, yB_w[0], width, color='g')
p2B_w = plt.bar(xB_w, yB_w[1], width, bottom=yB_w[0], color='c')
p3B_w = plt.bar(xB_w, yB_w[2], width, bottom=yB_w[0]+yB_w[1], color='r')
p4B_w = plt.bar(xB_w, yB_w[3], width, bottom=yB_w[0]+yB_w[1]+yB_w[2], color='b')

#Sample 6D
D_kngp_w = 2082.0
D_kpgp_w = 1137.0
D_kpgn_w = 9.0
D_kngn_w = 2485.0
xD_w = np.array(["Sample 6D"])
yD_w = np.array([D_kngp_w,D_kngn_w,D_kpgp_w,D_kpgn_w])
p1D_w = plt.bar(xD_w, yD_w[0], width, color='g')
p2D_w = plt.bar(xD_w, yD_w[1], width, bottom=yD_w[0], color='c')
p3D_w = plt.bar(xD_w, yD_w[2], width, bottom=yD_w[0]+yD_w[1], color='r')
p4D_w = plt.bar(xD_w, yD_w[3], width, bottom=yD_w[0]+yD_w[1]+yD_w[2], color='b')

#Sample 6G
G_kngp_w = 442.0
G_kpgp_w = 5507.0
G_kpgn_w = 1.0
G_kngn_w = 441.0
xG_w = np.array(["Sample 6G"])
yG_w = np.array([G_kngp_w,G_kngn_w,G_kpgp_w,G_kpgn_w])
p1G_w = plt.bar(xG_w, yG_w[0], width, color='g')
p2G_w = plt.bar(xG_w, yG_w[1], width, bottom=yG_w[0], color='c')
p3G_w = plt.bar(xG_w, yG_w[2], width, bottom=yG_w[0]+yG_w[1], color='r')
p4G_w = plt.bar(xG_w, yG_w[3], width, bottom=yG_w[0]+yG_w[1]+yG_w[2], color='b')

plt.ylabel("Number of Cells Identified")
#plt.legend((p1B_w[0], p2B_w[0], p3B_w[0], p4B_w[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1.04))
plt.title("Watershed Method")
plt.ylim([0,9000])
plt.show()

print('\n----  WATERSHED METHOD ----')  
print('-----------------------------')   
print('\n----  Sample 6B  ----')               
print('\nKRT5-/GATA3+:', B_kngp_w)
print('KRT5+/GATA3+:', B_kpgp_w)    
print('KRT5+/GATA3-:', B_kpgn_w)
print('KRT5-/GATA3-:', B_kngn_w)

print('\n----  Sample 6D  ----')               
print('\nKRT5-/GATA3+:', D_kngp_w)
print('KRT5+/GATA3+:', D_kpgp_w)    
print('KRT5+/GATA3-:', D_kpgn_w)
print('KRT5-/GATA3-:', D_kngn_w)

print('\n----  Sample 6G  ----')               
print('\nKRT5-/GATA3+:', G_kngp_w)
print('KRT5+/GATA3+:', G_kpgp_w)    
print('KRT5+/GATA3-:', G_kpgn_w)
print('KRT5-/GATA3-:', G_kngn_w)

# In[]: TEMPLATE MATCHING
width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6.5, 5.5)

#Sample 6B
B_kngp_tm = 1276.0
B_kpgp_tm =  1529.0
B_kpgn_tm = 0.0
B_kngn_tm = 246.0
xB_tm = np.array(["Sample 6B"])
yB_tm = np.array([B_kngp_tm,B_kngn_tm,B_kpgp_tm,B_kpgn_tm])
p1B_tm = plt.bar(xB_tm, yB_tm[0], width, color='g')
p2B_tm = plt.bar(xB_tm, yB_tm[1], width, bottom=yB_tm[0], color='c')
p3B_tm = plt.bar(xB_tm, yB_tm[2], width, bottom=yB_tm[0]+yB_tm[1], color='r')
p4B_tm = plt.bar(xB_tm, yB_tm[3], width, bottom=yB_tm[0]+yB_tm[1]+yB_tm[2], color='b')

#Sample 6D
D_kngp_tm = 1382.0
D_kpgp_tm = 445.0
D_kpgn_tm = 1.0
D_kngn_tm = 897.0
xD_tm = np.array(["Sample 6D"])
yD_tm = np.array([D_kngp_tm,D_kngn_tm,D_kpgp_tm,D_kpgn_tm])
p1D_tm = plt.bar(xD_tm, yD_tm[0], width, color='g')
p2D_tm = plt.bar(xD_tm, yD_tm[1], width, bottom=yD_tm[0], color='c')
p3D_tm = plt.bar(xD_tm, yD_tm[2], width, bottom=yD_tm[0]+yD_tm[1], color='r')
p4D_tm = plt.bar(xD_tm, yD_tm[3], width, bottom=yD_tm[0]+yD_tm[1]+yD_tm[2], color='b')

#Sample 6G
G_kngp_tm =  756.0
G_kpgp_tm =  2816.0
G_kpgn_tm = 0.0
G_kngn_tm = 138.0
xG_tm = np.array(["Sample 6G"])
yG_tm = np.array([G_kngp_tm,G_kngn_tm,G_kpgp_tm,G_kpgn_tm])
p1G_tm = plt.bar(xG_tm, yG_tm[0], width, color='g')
p2G_tm = plt.bar(xG_tm, yG_tm[1], width, bottom=yG_tm[0], color='c')
p3G_tm = plt.bar(xG_tm, yG_tm[2], width, bottom=yG_tm[0]+yG_tm[1], color='r')
p4G_tm = plt.bar(xG_tm, yG_tm[3], width, bottom=yG_tm[0]+yG_tm[1]+yG_tm[2], color='b')


plt.ylabel("Number of Cells Identified")
#plt.legend((p1B_tm[0], p2B_tm[0], p3B_tm[0], p4B_tm[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
plt.title("Template Matching Method")
plt.ylim([0,9000])
plt.show()

print('\n----  TEMPLATE MATCHING METHOD ----')  
print('-------------------------------------')   
print('\n----  Sample 6B  ----')               
print('\nKRT5-/GATA3+:', B_kngp_tm)
print('KRT5+/GATA3+:', B_kpgp_tm)    
print('KRT5+/GATA3-:', B_kpgn_tm)
print('KRT5-/GATA3-:', B_kngn_tm)

print('\n----  Sample 6D  ----')               
print('\nKRT5-/GATA3+:', D_kngp_tm)
print('KRT5+/GATA3+:', D_kpgp_tm)    
print('KRT5+/GATA3-:', D_kpgn_tm)
print('KRT5-/GATA3-:', D_kngn_tm)

print('\n----  Sample 6G  ----')               
print('\nKRT5-/GATA3+:', G_kngp_tm)
print('KRT5+/GATA3+:', G_kpgp_tm)    
print('KRT5+/GATA3-:', G_kpgn_tm)
print('KRT5-/GATA3-:', G_kngn_tm)

# In[]: COMBINED
width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6.5, 5.5)

#Sample 6B
B_kngp_c = 1276.0
B_kpgp_c =  3627.0
B_kpgn_c = 80.0
B_kngn_c = 246.0
xB_c = np.array(["Sample 6B"])
yB_c = np.array([B_kngp_c,B_kngn_c,B_kpgp_c,B_kpgn_c])
p1B_c = plt.bar(xB_c, yB_c[0], width, color='g')
p2B_c = plt.bar(xB_c, yB_c[1], width, bottom=yB_c[0], color='c')
p3B_c = plt.bar(xB_c, yB_c[2], width, bottom=yB_c[0]+yB_c[1], color='r')
p4B_c = plt.bar(xB_c, yB_c[3], width, bottom=yB_c[0]+yB_c[1]+yB_c[2], color='b')

#Sample 6D
D_kngp_c = 1382.0
D_kpgp_c = 1153.0
D_kpgn_c = 9.0
D_kngn_c = 897.0
xD_c = np.array(["Sample 6D"])
yD_c = np.array([D_kngp_c,D_kngn_c,D_kpgp_c,D_kpgn_c])
p1D_c = plt.bar(xD_c, yD_c[0], width, color='g')
p2D_c = plt.bar(xD_c, yD_c[1], width, bottom=yD_c[0], color='c')
p3D_c = plt.bar(xD_c, yD_c[2], width, bottom=yD_c[0]+yD_c[1], color='r')
p4D_c = plt.bar(xD_c, yD_c[3], width, bottom=yD_c[0]+yD_c[1]+yD_c[2], color='b')

#Sample 6G
G_kngp_c =  756.0
G_kpgp_c =  5508.0
G_kpgn_c = 1.0
G_kngn_c = 138.0
xG_c = np.array(["Sample 6G"])
yG_c = np.array([G_kngp_c,G_kngn_c,G_kpgp_c,G_kpgn_c])
p1G_c = plt.bar(xG_c, yG_c[0], width, color='g')
p2G_c = plt.bar(xG_c, yG_c[1], width, bottom=yG_c[0], color='c')
p3G_c = plt.bar(xG_c, yG_c[2], width, bottom=yG_c[0]+yG_c[1], color='r')
p4G_c = plt.bar(xG_c, yG_c[3], width, bottom=yG_c[0]+yG_c[1]+yG_c[2], color='b')


plt.ylabel("Number of Cells Identified")
#plt.legend((p1G_c[0], p2G_c[0], p3G_c[0], p4G_c[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
plt.ylim([0,9000])
plt.title("Combined Method")
plt.show()

print('\n---- COMBINED METHOD ----')  
print('---------------------------')   
print('\n----  Sample 6B  ----')               
print('\nKRT5-/GATA3+:', B_kngp_c)
print('KRT5+/GATA3+:', B_kpgp_c)    
print('KRT5+/GATA3-:', B_kpgn_c)
print('KRT5-/GATA3-:', B_kngn_c)

print('\n----  Sample 6D  ----')               
print('\nKRT5-/GATA3+:', D_kngp_c)
print('KRT5+/GATA3+:', D_kpgp_c)    
print('KRT5+/GATA3-:', D_kpgn_c)
print('KRT5-/GATA3-:', D_kngn_c)

print('\n----  Sample 6G  ----')               
print('\nKRT5-/GATA3+:', G_kngp_c)
print('KRT5+/GATA3+:', G_kpgp_c)    
print('KRT5+/GATA3-:', G_kpgn_c)
print('KRT5-/GATA3-:', G_kngn_c)

# In[]: HALO
# Stain 1 is green
# Stain 2 is red

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6.5, 5.5)

#Sample 6B
Btot_stain1_h = 7087
Btot_stain2_h = 3918

B_kpgp_h = 3439 #Dual positive cells
B_kngn_h = 747 #Dual negative cells
B_kngp_h = Btot_stain1_h - B_kpgp_h
B_kpgn_h = Btot_stain2_h - B_kpgp_h


xB_h = np.array(["Sample 6B"])
yB_h = np.array([B_kngp_h,B_kngn_h,B_kpgp_h,B_kpgn_h])
p1B_h = plt.bar(xB_h, yB_h[0], width, color='g')
p2B_h = plt.bar(xB_h, yB_h[1], width, bottom=yB_h[0], color='c')
p3B_h = plt.bar(xB_h, yB_h[2], width, bottom=yB_h[0]+yB_h[1], color='r')
p4B_h = plt.bar(xB_h, yB_h[3], width, bottom=yB_h[0]+yB_h[1]+yB_h[2], color='b')

#Sample 6D
Dtot_stain1_h = 4570
Dtot_stain2_h = 387

D_kpgp_h = 284
D_kngn_h = 1894
D_kngp_h = Dtot_stain1_h - D_kpgp_h
D_kpgn_h = Dtot_stain2_h - D_kpgp_h

xD_h = np.array(["Sample 6D"])
yD_h = np.array([D_kngp_h,D_kngn_h,D_kpgp_h,D_kpgn_h])
p1D_h = plt.bar(xD_h, yD_h[0], width, color='g')
p2D_h = plt.bar(xD_h, yD_h[1], width, bottom=yD_h[0], color='c')
p3D_h = plt.bar(xD_h, yD_h[2], width, bottom=yD_h[0]+yD_h[1], color='r')
p4D_h = plt.bar(xD_h, yD_h[3], width, bottom=yD_h[0]+yD_h[1]+yD_h[2], color='b')

#Sample 6G
Gtot_stain1_h = 6819
Gtot_stain2_h = 5800

G_kpgp_h = 5400
G_kngn_h = 340
G_kngp_h = Gtot_stain1_h - G_kpgp_h
G_kpgn_h = Gtot_stain2_h - G_kpgp_h

xG_h = np.array(["Sample 6G"])
yG_h = np.array([G_kngp_h,G_kngn_h,G_kpgp_h,G_kpgn_h])
p1G_h = plt.bar(xG_h, yG_h[0], width, color='g')
p2G_h = plt.bar(xG_h, yG_h[1], width, bottom=yG_h[0], color='c')
p3G_h = plt.bar(xG_h, yG_h[2], width, bottom=yG_h[0]+yG_h[1], color='r')
p4G_h = plt.bar(xG_h, yG_h[3], width, bottom=yG_h[0]+yG_h[1]+yG_h[2], color='b')

plt.ylabel("Number of Cells Identified")
plt.legend((p1G_h[0], p2G_h[0], p3G_h[0], p4G_h[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
plt.ylim([0,9000])
plt.title("HALO Analysis")
plt.show()

print('\n---- HALO METHOD ----')  
print('-----------------------')   
print('\n----  Sample 6B  ----')               
print('\nKRT5-/GATA3+:', B_kngp_h)
print('KRT5+/GATA3+:', B_kpgp_h)    
print('KRT5+/GATA3-:', B_kpgn_h)
print('KRT5-/GATA3-:', B_kngn_h)

print('\n----  Sample 6D  ----')               
print('\nKRT5-/GATA3+:', D_kngp_h)
print('KRT5+/GATA3+:', D_kpgp_h)    
print('KRT5+/GATA3-:', D_kpgn_h)
print('KRT5-/GATA3-:', D_kngn_h)

print('\n----  Sample 6G  ----')               
print('\nKRT5-/GATA3+:', G_kngp_h)
print('KRT5+/GATA3+:', G_kpgp_h)    
print('KRT5+/GATA3-:', G_kpgn_h)
print('KRT5-/GATA3-:', G_kngn_h)
