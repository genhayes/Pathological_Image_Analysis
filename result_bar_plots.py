#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:38:42 2021

@author: genevieve.hayes
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib



# In[]: WATERSHED
width = 0.7
matplotlib.rc('font', serif='Helvetica Neue')
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6.5, 5.5)

#Sample 6B
B_kngp =  2149.0
B_kpgp =  3968.0
B_kpgn = 101.0
B_kngn = 478.0
xB = np.array(["Sample 6B"])
yB = np.array([B_kngp,B_kngn,B_kpgp,B_kpgn])
p1B = plt.bar(xB, yB[0], width, color='g')
p2B = plt.bar(xB, yB[1], width, bottom=yB[0], color='c')
p3B = plt.bar(xB, yB[2], width, bottom=yB[0]+yB[1], color='r')
p4B = plt.bar(xB, yB[3], width, bottom=yB[0]+yB[1]+yB[2], color='b')

#Sample 6D
D_kngp =  2152.0
D_kpgp =  1402.0
D_kpgn = 28.0
D_kngn = 2373.0
xD = np.array(["Sample 6D"])
yD = np.array([D_kngp,D_kngn,D_kpgp,D_kpgn])
p1D = plt.bar(xD, yD[0], width, color='g')
p2D = plt.bar(xD, yD[1], width, bottom=yD[0], color='c')
p3D = plt.bar(xD, yD[2], width, bottom=yD[0]+yD[1], color='r')
p4D = plt.bar(xD, yD[3], width, bottom=yD[0]+yD[1]+yD[2], color='b')

#Sample 6G
G_kngp =  424.0
G_kpgp =  5892.0
G_kpgn = 5.0
G_kngn = 185.0
xG = np.array(["Sample 6G"])
yG = np.array([G_kngp,G_kngn,G_kpgp,G_kpgn])
p1G = plt.bar(xG, yG[0], width, color='g')
p2G = plt.bar(xG, yG[1], width, bottom=yG[0], color='c')
p3G = plt.bar(xG, yG[2], width, bottom=yG[0]+yG[1], color='r')
p4G = plt.bar(xG, yG[3], width, bottom=yG[0]+yG[1]+yG[2], color='b')


plt.ylabel("Number of Cells Identified")
#plt.legend((p1B[0], p2B[0], p3B[0], p4B[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1.04))
plt.title("Watershed Method")
plt.ylim([0,8000])
plt.show()

# In[]: TEMPLATE MATCHING
width = 0.7
matplotlib.rc('font', serif='Helvetica Neue')
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6.5, 5.5)

#Sample 6B
B_kngp =  1225.0
B_kpgp =  1882.0
B_kpgn = 0.0
B_kngn = 234.0
xB = np.array(["Sample 6B"])
yB = np.array([B_kngp,B_kngn,B_kpgp,B_kpgn])
p1B = plt.bar(xB, yB[0], width, color='g')
p2B = plt.bar(xB, yB[1], width, bottom=yB[0], color='c')
p3B = plt.bar(xB, yB[2], width, bottom=yB[0]+yB[1], color='r')
p4B = plt.bar(xB, yB[3], width, bottom=yB[0]+yB[1]+yB[2], color='b')

#Sample 6D
D_kngp =  1352.0
D_kpgp =  545.0
D_kpgn = 1.0
D_kngn = 884.0
xD = np.array(["Sample 6D"])
yD = np.array([D_kngp,D_kngn,D_kpgp,D_kpgn])
p1D = plt.bar(xD, yD[0], width, color='g')
p2D = plt.bar(xD, yD[1], width, bottom=yD[0], color='c')
p3D = plt.bar(xD, yD[2], width, bottom=yD[0]+yD[1], color='r')
p4D = plt.bar(xD, yD[3], width, bottom=yD[0]+yD[1]+yD[2], color='b')

#Sample 6G
G_kngp =  647.0
G_kpgp =  3139.0
G_kpgn = 0.0
G_kngn = 128.0
xG = np.array(["Sample 6G"])
yG = np.array([G_kngp,G_kngn,G_kpgp,G_kpgn])
p1G = plt.bar(xG, yG[0], width, color='g')
p2G = plt.bar(xG, yG[1], width, bottom=yG[0], color='c')
p3G = plt.bar(xG, yG[2], width, bottom=yG[0]+yG[1], color='r')
p4G = plt.bar(xG, yG[3], width, bottom=yG[0]+yG[1]+yG[2], color='b')


plt.ylabel("Number of Cells Identified")
#plt.legend((p1B[0], p2B[0], p3B[0], p4B[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
plt.title("Template Matching Method")
plt.ylim([0,8000])
plt.show()

# In[]: COMBINED
width = 0.7
matplotlib.rc('font', serif='Helvetica Neue')
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6.5, 5.5)

#Sample 6B
B_kngp =  1291.0
B_kpgp =  3641.0
B_kpgn = 74.0
B_kngn = 237.0
xB = np.array(["Sample 6B"])
yB = np.array([B_kngp,B_kngn,B_kpgp,B_kpgn])
p1B = plt.bar(xB, yB[0], width, color='g')
p2B = plt.bar(xB, yB[1], width, bottom=yB[0], color='c')
p3B = plt.bar(xB, yB[2], width, bottom=yB[0]+yB[1], color='r')
p4B = plt.bar(xB, yB[3], width, bottom=yB[0]+yB[1]+yB[2], color='b')

#Sample 6D
D_kngp =  1364.0
D_kpgp =  1204.0
D_kpgn = 18.0
D_kngn = 894.0
xD = np.array(["Sample 6D"])
yD = np.array([D_kngp,D_kngn,D_kpgp,D_kpgn])
p1D = plt.bar(xD, yD[0], width, color='g')
p2D = plt.bar(xD, yD[1], width, bottom=yD[0], color='c')
p3D = plt.bar(xD, yD[2], width, bottom=yD[0]+yD[1], color='r')
p4D = plt.bar(xD, yD[3], width, bottom=yD[0]+yD[1]+yD[2], color='b')

#Sample 6G
G_kngp =  766.0
G_kpgp =  5526.0
G_kpgn = 1.0
G_kngn = 136.0
xG = np.array(["Sample 6G"])
yG = np.array([G_kngp,G_kngn,G_kpgp,G_kpgn])
p1G = plt.bar(xG, yG[0], width, color='g')
p2G = plt.bar(xG, yG[1], width, bottom=yG[0], color='c')
p3G = plt.bar(xG, yG[2], width, bottom=yG[0]+yG[1], color='r')
p4G = plt.bar(xG, yG[3], width, bottom=yG[0]+yG[1]+yG[2], color='b')


plt.ylabel("Number of Cells Identified")
plt.legend((p1G[0], p2G[0], p3G[0], p4G[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
plt.ylim([0,8000])
plt.title("Combined Method")
plt.show()

# In[]: ALL

# width = 0.7
# matplotlib.rc('font', serif='Helvetica Neue')
# matplotlib.rc('text', usetex='false')
# matplotlib.rcParams.update({'font.size': 16})
# fig = matplotlib.pyplot.gcf()
# fig.set_size_inches(6.5, 5.5)

# #Sample 6B
# B_kngp =  1225.0
# B_kpgp =  4129.0
# B_kpgn = 101.0
# B_kngn = 234.0
# xBC = np.array(["Sample 6B"])
# yB = np.array([B_kngp,B_kngn,B_kpgp,B_kpgn])
# p1B = plt.bar(xB, yB[0], width, color='g')
# p2B = plt.bar(xB, yB[1], width, bottom=yB[0], color='c')
# p3B = plt.bar(xB, yB[2], width, bottom=yB[0]+yB[1], color='r')
# p4B = plt.bar(xB, yB[3], width, bottom=yB[0]+yB[1]+yB[2], color='b')

# #Sample 6D
# D_kngp =  1352.0
# D_kpgp =  1443.0
# D_kpgn = 28.0
# D_kngn = 884.0
# xD = np.array(["Sample 6D"])
# yD = np.array([D_kngp,D_kngn,D_kpgp,D_kpgn])
# p1D = plt.bar(xD, yD[0], width, color='g')
# p2D = plt.bar(xD, yD[1], width, bottom=yD[0], color='c')
# p3D = plt.bar(xD, yD[2], width, bottom=yD[0]+yD[1], color='r')
# p4D = plt.bar(xD, yD[3], width, bottom=yD[0]+yD[1]+yD[2], color='b')

# #Sample 6G
# G_kngp =  647.0
# G_kpgp =  5900.0
# G_kpgn = 5.0
# G_kngn = 128.0
# xG = np.array(["Sample 6G"])
# yG = np.array([G_kngp,G_kngn,G_kpgp,G_kpgn])
# p1G = plt.bar(xG, yG[0], width, color='g')
# p2G = plt.bar(xG, yG[1], width, bottom=yG[0], color='c')
# p3G = plt.bar(xG, yG[2], width, bottom=yG[0]+yG[1], color='r')
# p4G = plt.bar(xG, yG[3], width, bottom=yG[0]+yG[1]+yG[2], color='b')


# plt.ylabel("Number of Cells Identified")
# plt.legend((p1G[0], p2G[0], p3G[0], p4G[0]), ('KRT5-/GATA3+', 'KRT5-/GATA3-', 'KRT5+/GATA3+', 'KRT5+/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
# plt.ylim([0,8000])
