#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:24:34 2021

@author: genevieve.hayes

Bulk Analysis
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


# In[]:
    
width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 16})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(9.5, 5.5)
    
#Watershed Info

#File:Sample4B.tiff
w4Bkpgp = 400.0
w4Bkngn = 526.0
w4Bkpgn = 1.0
w4Bkngp = 1914.0
#File:Sample3I.tiff
w3Ikpgp = 53.0
w3Ikngn = 1510.0
w3Ikpgn = 14.0
w3Ikngp = 28.0
#File:Sample1I.tiff
w1Ikpgp = 2150.0
w1Ikngn = 327.0
w1Ikpgn = 243.0
w1Ikngp = 345.0
#File:Sample6B.tiff
w6Bkpgp = 3509.0
w6Bkngn = 1048.0
w6Bkpgn = 80.0
w6Bkngp = 2340.0
#File:Sample2C.tiff
w2Ckpgp = 1595.0
w2Ckngn = 741.0
w2Ckpgn = 6.0
w2Ckngp = 4072.0
#File:Sample2B.tiff
w2Bkpgp = 160.0
w2Bkngn = 474.0
w2Bkpgn = 4.0
w2Bkngp = 445.0
#File:Sample6C.tiff
w6Ckpgp = 1570.0
w6Ckngn = 799.0
w6Ckpgn = 10.0
w6Ckngp = 4133.0
#File:Sample1H.tiff
w1Hkpgp = 1262.0
w1Hkngn = 255.0
w1Hkpgn = 19.0
w1Hkngp = 113.0
#File:Sample3H.tiff
w3Hkpgp = 1122.0
w3Hkngn = 1828.0
w3Hkpgn = 29.0
w3Hkngp = 2689.0
#File:Sample4C.tiff
w4Ckpgp = 2091.0
w4Ckngn = 560.0
w4Ckpgn = 17.0
w4Ckngp = 3857.0
#File:Sample6D.tiff
w6Dkpgp = 1137.0
w6Dkngn = 2485.0
w6Dkpgn = 9.0
w6Dkngp = 2082.0
#File:Sample2E.tiff
w2Ekpgp = 386.0
w2Ekngn = 1080.0
w2Ekpgn = 13.0
w2Ekngp = 1297.0
#File:Sample4D.tiff
w4Dkpgp = 2710.0
w4Dkngn = 859.0
w4Dkpgn = 9.0
w4Dkngp = 4129.0
#File:Sample2I.tiff
w2Ikpgp = 320.0
w2Ikngn = 1052.0
w2Ikpgn = 13.0
w2Ikngp = 1402.0
#File:Sample6I.tiff
w6Ikpgp = 64.0
w6Ikngn = 1127.0
w6Ikpgn = 2.0
w6Ikngp = 1153.0
#File:Sample1B.tiff
w1Bkpgp = 143.0
w1Bkngn = 231.0
w1Bkpgn = 9.0
w1Bkngp = 1673.0
#File:Sample4E.tiff
w4Ekpgp = 839.0
w4Ekngn = 2389.0
w4Ekpgn = 97.0
w4Ekngp = 808.0
#File:Sample5C.tiff
w5Ckpgp = 1862.0
w5Ckngn = 938.0
w5Ckpgn = 2.0
w5Ckngp = 4936.0
#File:Sample6E.tiff
w6Ekpgp = 723.0
w6Ekngn = 609.0
w6Ekpgn = 3.0
w6Ekngp = 2531.0
#File:Sample6F.tiff
w6Fkpgp = 97.0
w6Fkngn = 1010.0
w6Fkpgn = 5.0
w6Fkngp = 483.0
#File:Sample6J.tiff
w6Jkpgp = 1215.0
w6Jkngn = 928.0
w6Jkpgn = 15.0
w6Jkngp = 3465.0
#File:Sample1A.tiff
w1Akpgp = 708.0
w1Akngn = 156.0
w1Akpgn = 9.0
w1Akngp = 2572.0
#File:Sample5A.tiff
w5Akpgp = 332.0
w5Akngn = 243.0
w5Akpgn = 3.0
w5Akngp = 1527.0
#File:Sample6G.tiff
w6Gkpgp = 5507.0
w6Gkngn = 441.0
w6Gkpgn = 1.0
w6Gkngp = 442.0
#File:Sample1G.tiff
w1Gkpgp = 1981.0
w1Gkngn = 129.0
w1Gkpgn = 27.0
w1Gkngp = 18.0
#File:Sample2A.tiff
w2Akpgp = 238.0
w2Akngn = 552.0
w2Akpgn = 4.0
w2Akngp = 1359.0
#File:Sample5J.tiff
w5Jkpgp = 776.0
w5Jkngn = 193.0
w5Jkpgn = 8.0
w5Jkngp = 520.0
#File:Sample1J.tiff
w1Jkpgp = 3821.0
w1Jkngn = 203.0
w1Jkpgn = 64.0
w1Jkngp = 20.0
#File:Sample6A.tiff
w6Akpgp = 1853.0
w6Akngn = 1296.0
w6Akpgn = 17.0
w6Akngp = 904.0
#File:Sample3F.tiff
w3Fkpgp = 609.0
w3Fkngn = 480.0
w3Fkpgn = 10.0
w3Fkngp = 159.0

# In[]: HALO Info
stain1_4E_h = 4228
stain2_4E_h = 1558

h_4E_kpgp = 669
h_4E_kngn = 2115
h_4E_kpgn = stain1_4E_h - h_4E_kpgp
h_4E_kngp = stain1_4E_h - h_4E_kpgp

stain1_6I_h = 2010
stain2_6I_h = 31

h_6I_kpgp = 23
h_6I_kngn = 602
h_6I_kpgn = stain1_6I_h - h_6I_kpgp
h_6I_kngp = stain1_6I_h - h_6I_kpgp

stain1_4D_h = 7316
stain2_4D_h = 1879

h_4D_kpgp = 1758
h_4D_kngn = 376
h_4D_kpgn = stain1_4D_h - h_4D_kpgp
h_4D_kngp = stain1_4D_h - h_4D_kpgp

stain1_6D_h = 4570
stain2_6D_h = 387

h_6D_kpgp = 284
h_6D_kngn = 1894
h_6D_kpgn = stain1_6D_h - h_6D_kpgp
h_6D_kngp = stain1_6D_h - h_6D_kpgp

stain1_2E_h = 3784
stain2_2E_h = 672

h_2E_kpgp = 346
h_2E_kngn = 987
h_2E_kpgn = stain1_2E_h - h_2E_kpgp
h_2E_kngp = stain1_2E_h - h_2E_kpgp

stain1_4B_h = 2461
stain2_4B_h = 13

h_4B_kpgp = 9
h_4B_kngn = 425
h_4B_kpgn = stain1_4B_h - h_4B_kpgp
h_4B_kngp = stain1_4B_h - h_4B_kpgp

stain1_4C_h = 2461
stain2_4C_h = 13

h_4C_kpgp = 9
h_4C_kngn = 425
h_4C_kpgn = stain1_4C_h - h_4C_kpgp
h_4C_kngp = stain1_4C_h - h_4C_kpgp

stain1_6B_h = 7087
stain2_6B_h = 3918

h_6B_kpgp = 3439
h_6B_kngn = 747
h_6B_kpgn = stain1_6B_h - h_6B_kpgp
h_6B_kngp = stain1_6B_h - h_6B_kpgp

stain1_3I_h = 372
stain2_3I_h = 140

h_3I_kpgp = 63
h_3I_kngn = 2225
h_3I_kpgn = stain1_3I_h - h_3I_kpgp
h_3I_kngp = stain1_3I_h - h_3I_kpgp

stain1_1I_h = 3191
stain2_1I_h = 3937

h_1I_kpgp = 2034
h_1I_kngn = 677
h_1I_kpgn = stain1_1I_h - h_1I_kpgp
h_1I_kngp = stain1_1I_h - h_1I_kpgp

stain1_2C_h = 5992
stain2_2C_h = 646

h_2C_kpgp = 613
h_2C_kngn = 259
h_2C_kpgn = stain1_2C_h - h_2C_kpgp
h_2C_kngp = stain1_2C_h - h_2C_kpgp

stain1_2B_h = 1289
stain2_2B_h = 122

h_2B_kpgp = 71
h_2B_kngn = 614
h_2B_kpgn = stain1_2B_h - h_2B_kpgp
h_2B_kngp = stain1_2B_h - h_2B_kpgp

stain1_6C_h = 6333
stain2_6C_h = 31

h_6C_kpgp = 26
h_6C_kngn = 258
h_6C_kpgn = stain1_6C_h - h_6C_kpgp
h_6C_kngp = stain1_6C_h - h_6C_kpgp

stain1_1H_h = 1556
stain2_1H_h = 1968

h_1H_kpgp = 1213
h_1H_kngn = 223
h_1H_kpgn = stain1_1H_h - h_1H_kpgp
h_1H_kngp = stain1_1H_h - h_1H_kpgp

stain1_3H_h = 5201
stain2_3H_h = 728

h_3H_kpgp = 612
h_3H_kngn = 952
h_3H_kpgn = stain1_3H_h - h_3H_kpgp
h_3H_kngp = stain1_3H_h - h_3H_kpgp

stain1_2I_h = 2178
stain2_2I_h = 219

h_2I_kpgp = 172
h_2I_kngn = 903
h_2I_kpgn = stain1_2I_h - h_2I_kpgp
h_2I_kngp = stain1_2I_h - h_2I_kpgp

stain1_1B_h = 3529
stain2_1B_h = 3

h_1B_kpgp = 2
h_1B_kngn = 233
h_1B_kpgn = stain1_1B_h - h_1B_kpgp
h_1B_kngp = stain1_1B_h - h_1B_kpgp

stain1_3H_h = 5201
stain2_3H_h = 728

h_3H_kpgp = 612
h_2H_kngn = 952
h_3H_kpgn = stain1_3H_h - h_3H_kpgp
h_3H_kngp = stain1_3H_h - h_3H_kpgp

stain1_5C_h = 5924
stain2_5C_h = 27

h_5C_kpgp = 23
h_5C_kngn = 512
h_5C_kpgn = stain1_5C_h - h_5C_kpgp
h_5C_kngp = stain1_5C_h - h_5C_kpgp


stain1_6E_h = 2913
stain2_6E_h = 206

h_6E_kpgp = 138
h_6E_kngn = 370
h_6E_kpgn = stain1_6E_h - h_6E_kpgp
h_6E_kngp = stain1_6E_h - h_6E_kpgp

stain1_6F_h = 953
stain2_6F_h = 30

h_6F_kpgp = 19
h_6F_kngn = 871
h_6F_kpgn = stain1_6F_h - h_6F_kpgp
h_6F_kngp = stain1_6F_h - h_6F_kpgp

stain1_6J_h = 5119
stain2_6J_h = 781

h_6J_kpgp = 687
h_6J_kngn = 398
h_6J_kpgn = stain1_6J_h - h_6J_kpgp
h_6J_kngp = stain1_6J_h - h_6J_kpgp

stain1_1A_h = 3201
stain2_1A_h = 7

h_1A_kpgp = 6
h_1A_kngn = 42
h_1A_kpgn = stain1_1A_h - h_1A_kpgp
h_1A_kngp = stain1_1A_h - h_1A_kpgp

stain1_5A_h = 2128
stain2_5A_h = 118

h_5A_kpgp = 100
h_5A_kngn = 278
h_5A_kpgn = stain1_5A_h - h_5A_kpgp
h_5A_kngp = stain1_5A_h - h_5A_kpgp

stain1_6G_h = 6819
stain2_6G_h = 5800

h_6G_kpgp = 5400
h_6G_kngn = 340
h_6G_kpgn = stain1_6G_h - h_6G_kpgp
h_6G_kngp = stain1_6G_h - h_6G_kpgp

stain1_1G_h = 2198
stain2_1G_h = 2673

h_1G_kpgp = 1975
h_1G_kngn = 307
h_1G_kpgn = stain1_1G_h - h_1G_kpgp
h_1G_kngp = stain1_1G_h - h_1G_kpgp

stain1_2A_h = 2389
stain2_2A_h = 172

h_2A_kpgp = 133
h_2A_kngn = 777
h_2A_kpgn = stain1_2A_h - h_2A_kpgp
h_2A_kngp = stain1_2A_h - h_2A_kpgp

stain1_5J_h = 1704
stain2_5J_h = 921

h_5J_kpgp = 827
h_5J_kngn = 131
h_5J_kpgn = stain1_5J_h - h_5J_kpgp
h_5J_kngp = stain1_5J_h - h_5J_kpgp


stain1_1J_h = 4162
stain2_1J_h = 5598

h_1J_kpgp = 4015
h_1J_kngn = 626
h_1J_kpgn = stain1_1J_h - h_1J_kpgp
h_1J_kngp = stain1_1J_h - h_1J_kpgp

stain1_6A_h = 3954
stain2_6A_h = 1759

h_6A_kpgp = 1575
h_6A_kngn = 596
h_6A_kpgn = stain1_6A_h - h_6A_kpgp
h_6A_kngp = stain1_6A_h - h_6A_kpgp

stain1_3F_h = 1288
stain2_3F_h = 681

h_3F_kpgp = 559
h_3F_kngn = 603
h_3F_kpgn = stain1_3F_h - h_3F_kpgp
h_3F_kngp = stain1_3F_h - h_3F_kpgp

# In[]: Make the plots
wp1 = np.array([w4Bkngp,
w3Ikngp,
w1Ikngp,
w6Bkngp,
w2Ckngp,
w2Bkngp,
w6Ckngp,
w1Hkngp,
w3Hkngp,
w4Ckngp,
w6Dkngp,
w2Ekngp,
w4Dkngp,
w2Ikngp,
w6Ikngp,
w1Bkngp,
w4Ekngp,
w5Ckngp,
w6Ekngp,
w6Fkngp,
w6Jkngp,
w1Akngp,
w5Akngp,
w6Gkngp,
w1Gkngp,
w2Akngp,
w5Jkngp,
w1Jkngp,
w6Akngp,
w3Fkngp])

hp1 = np.array([h_4B_kpgp,
h_3I_kngp,
h_1I_kngp,
h_6B_kngp,
h_2C_kngp,
h_2B_kngp,
h_6C_kngp,
h_1H_kngp,
h_3H_kngp,
h_4C_kngp,
h_6D_kngp,
h_2E_kngp,
h_4D_kngp,
h_2I_kngp,
h_6I_kngp,
h_1B_kngp,
h_4E_kngp,
h_5C_kngp,
h_6E_kngp,
h_6F_kngp,
h_6J_kngp,
h_1A_kngp,
h_5A_kngp,
h_6G_kngp,
h_1G_kngp,
h_2A_kngp,
h_5J_kngp,
h_1J_kngp,
h_6A_kngp,
h_3F_kngp])

p1 = plt.scatter(wp1, hp1, marker='*', color='red')

wp2 = np.array([w4Bkpgn,
w3Ikpgn,
w1Ikpgn,
w6Bkpgn,
w2Ckpgn,
w2Bkpgn,
w6Ckpgn,
w1Hkpgn,
w3Hkpgn,
w4Ckpgn,
w6Dkpgn,
w2Ekpgn,
w4Dkpgn,
w2Ikpgn,
w6Ikpgn,
w1Bkpgn,
w4Ekpgn,
w5Ckpgn,
w6Ekpgn,
w6Fkpgn,
w6Jkpgn,
w1Akpgn,
w5Akpgn,
w6Gkpgn,
w1Gkpgn,
w2Akpgn,
w5Jkpgn,
w1Jkpgn,
w6Akpgn,
w3Fkpgn])

hp2 = np.array([h_4B_kpgn,
h_3I_kpgn,
h_1I_kpgn,
h_6B_kpgn,
h_2C_kpgn,
h_2B_kpgn,
h_6C_kpgn,
h_1H_kpgn,
h_3H_kpgn,
h_4C_kpgn,
h_6D_kpgn,
h_2E_kpgn,
h_4D_kpgn,
h_2I_kpgn,
h_6I_kpgn,
h_1B_kpgn,
h_4E_kpgn,
h_5C_kpgn,
h_6E_kpgn,
h_6F_kpgn,
h_6J_kpgn,
h_1A_kpgn,
h_5A_kpgn,
h_6G_kpgn,
h_1G_kpgn,
h_2A_kpgn,
h_5J_kpgn,
h_1J_kpgn,
h_6A_kpgn,
h_3F_kpgn])

p2 = plt.scatter(wp2, hp2, marker='d', color='blue')

wp3 = np.array([w4Bkpgp,
w3Ikpgp,
w1Ikpgp,
w6Bkpgp,
w2Ckpgp,
w2Bkpgp,
w6Ckpgp,
w1Hkpgp,
w3Hkpgp,
w4Ckpgp,
w6Dkpgp,
w2Ekpgp,
w4Dkpgp,
w2Ikpgp,
w6Ikpgp,
w1Bkpgp,
w4Ekpgp,
w5Ckpgp,
w6Ekpgp,
w6Fkpgp,
w6Jkpgp,
w1Akpgp,
w5Akpgp,
w6Gkpgp,
w1Gkpgp,
w2Akpgp,
w5Jkpgp,
w1Jkpgp,
w6Akpgp,
w3Fkpgp])

hp3 = np.array([h_4B_kpgp,
h_3I_kpgp,
h_1I_kpgp,
h_6B_kpgp,
h_2C_kpgp,
h_2B_kpgp,
h_6C_kpgp,
h_1H_kpgp,
h_3H_kpgp,
h_4C_kpgp,
h_6D_kpgp,
h_2E_kpgp,
h_4D_kpgp,
h_2I_kpgp,
h_6I_kpgp,
h_1B_kpgp,
h_4E_kpgp,
h_5C_kpgp,
h_6E_kpgp,
h_6F_kpgp,
h_6J_kpgp,
h_1A_kpgp,
h_5A_kpgp,
h_6G_kpgp,
h_1G_kpgp,
h_2A_kpgp,
h_5J_kpgp,
h_1J_kpgp,
h_6A_kpgp,
h_3F_kpgp])

p3 = plt.scatter(wp3, hp3, marker='^', color='green')

wp4 = np.array([w4Bkngn,
w3Ikngn,
w1Ikngn,
w6Bkngn,
w2Ckngn,
w2Bkngn,
w6Ckngn,
w1Hkngn,
w3Hkngn,
w4Ckngn,
w6Dkngn,
w2Ekngn,
w4Dkngn,
w2Ikngn,
w6Ikngn,
w1Bkngn,
w4Ekngn,
w5Ckngn,
w6Ekngn,
w6Fkngn,
w6Jkngn,
w1Akngn,
w5Akngn,
w6Gkngn,
w1Gkngn,
w2Akngn,
w5Jkngn,
w1Jkngn,
w6Akngn,
w3Fkngn])

hp4 = np.array([h_4B_kpgn,
h_3I_kngn,
h_1I_kngn,
h_6B_kngn,
h_2C_kngn,
h_2B_kngn,
h_6C_kngn,
h_1H_kngn,
h_3H_kngn,
h_4C_kngn,
h_6D_kngn,
h_2E_kngn,
h_4D_kngn,
h_2I_kngn,
h_6I_kngn,
h_1B_kngn,
h_4E_kngn,
h_5C_kngn,
h_6E_kngn,
h_6F_kngn,
h_6J_kngn,
h_1A_kngn,
h_5A_kngn,
h_6G_kngn,
h_1G_kngn,
h_2A_kngn,
h_5J_kngn,
h_1J_kngn,
h_6A_kngn,
h_3F_kngn])

p4 = plt.scatter(wp4, hp4, marker='o', color='cyan')

x = np.linspace(0, 6000, num=len(wp1))

# Add best fit lines
m1, b1 = np.polyfit(wp1,hp1, 1)
fit_p1 = plt.plot(x, m1*x+b1, '-r')

#m2, b2 = np.polyfit(wp2,hp2, 1)
#fit_p2 = plt.plot(x, m2*x+b2, '-b')

m3, b3 = np.polyfit(wp3,hp3, 1)
fit_p3 = plt.plot(x, m3*x+b3, '-g')

m4, b4 = np.polyfit(wp4,hp4, 1)
fit_p4 = plt.plot(x, m4*x+b4, '-c')


plt.xlabel('Watershed')
plt.ylabel('HALO')
plt.legend((p1, p2, p3, p4), ('KRT5-/GATA3+', 'KRT5+/GATA3-', 'KRT5+/GATA3+', 'KRT5-/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
plt.tight_layout()
plt.title('Watershed vs. HALO')

plt.show()

