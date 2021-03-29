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
    
#Template Matching Info

#File:Sample4B.tiff
tm4Bkpgp = 118.0
tm4Bkngn = 267.0
tm4Bkpgn = 0.0
tm4Bkngp = 1307.0
#File:Sample3I.tiff
tm3Ikpgp = 43.0
tm3Ikngn = 337.0
tm3Ikpgn = 0.0
tm3Ikngp = 292.0
#File:Sample1I.tiff
tm1Ikpgp = 1606.0
tm1Ikngn = 87.0
tm1Ikpgn = 0.0
tm1Ikngp = 631.0
#File:Sample6B.tiff
tm6Bkpgp = 1529.0
tm6Bkngn = 246.0
tm6Bkpgn = 0.0
tm6Bkngp = 1276.0
#File:Sample2C.tiff
tm2Ckpgp = 596.0
tm2Ckngn = 558.0
tm2Ckpgn = 0.0
tm2Ckngp = 1395.0
#File:Sample2B.tiff
tm2Bkpgp = 123.0
tm2Bkngn = 51.0
tm2Bkpgn = 0.0
tm2Bkngp = 386.0
#File:Sample6C.tiff
tm6Ckpgp = 513.0
tm6Ckngn = 312.0
tm6Ckpgn = 0.0
tm6Ckngp = 1686.0
#File:Sample1H.tiff
tm1Hkpgp = 1111.0
tm1Hkngn = 81.0
tm1Hkpgn = 0.0
tm1Hkngp = 287.0
#File:Sample3H.tiff
tm3Hkpgp = 531.0
tm3Hkngn = 220.0
tm3Hkpgn = 0.0
tm3Hkngp = 1227.0
#File:Sample4C.tiff
tm4Ckpgp = 828.0
tm4Ckngn = 229.0
tm4Ckpgn = 0.0
tm4Ckngp = 1051.0
#File:Sample6D.tiff
tm6Dkpgp = 445.0
tm6Dkngn = 897.0
tm6Dkpgn = 1.0
tm6Dkngp = 1382.0
#File:Sample2E.tiff
tm2Ekpgp = 311.0
tm2Ekngn = 361.0
tm2Ekpgn = 0.0
tm2Ekngp = 1178.0
#File:Sample4D.tiff
tm4Dkpgp = 914.0
tm4Dkngn = 160.0
tm4Dkpgn = 0.0
tm4Dkngp = 1379.0
#File:Sample2I.tiff
tm2Ikpgp = 164.0
tm2Ikngn = 666.0
tm2Ikpgn = 0.0
tm2Ikngp = 821.0
#File:Sample6I.tiff
tm6Ikpgp = 42.0
tm6Ikngn = 738.0
tm6Ikpgn = 0.0
tm6Ikngp = 749.0
#File:Sample1B.tiff
tm1Bkpgp = 28.0
tm1Bkngn = 26.0
tm1Bkpgn = 0.0
tm1Bkngp = 401.0
#File:Sample4E.tiff
tm4Ekpgp = 796.0
tm4Ekngn = 417.0
tm4Ekpgn = 0.0
tm4Ekngp = 633.0
#File:Sample5C.tiff
tm5Ckpgp = 491.0
tm5Ckngn = 368.0
tm5Ckpgn = 0.0
tm5Ckngp = 1292.0
#File:Sample6E.tiff
tm6Ekpgp = 300.0
tm6Ekngn = 332.0
tm6Ekpgn = 0.0
tm6Ekngp = 921.0
#File:Sample6F.tiff
tm6Fkpgp = 56.0
tm6Fkngn = 369.0
tm6Fkpgn = 0.0
tm6Fkngp = 441.0
#File:Sample6J.tiff
tm6Jkpgp = 652.0
tm6Jkngn = 743.0
tm6Jkpgn = 0.0
tm6Jkngp = 1743.0
#File:Sample1A.tiff
tm1Akpgp = 234.0
tm1Akngn = 135.0
tm1Akpgn = 0.0
tm1Akngp = 648.0
#File:Sample5A.tiff
tm5Akpgp = 132.0
tm5Akngn = 68.0
tm5Akpgn = 0.0
tm5Akngp = 669.0
#File:Sample6G.tiff
tm6Gkpgp = 2816.0
tm6Gkngn = 138.0
tm6Gkpgn = 0.0
tm6Gkngp = 756.0
#File:Sample1G.tiff
tm1Gkpgp = 1507.0
tm1Gkngn = 83.0
tm1Gkpgn = 0.0
tm1Gkngp = 214.0
#File:Sample2A.tiff
tm2Akpgp = 113.0
tm2Akngn = 55.0
tm2Akpgn = 0.0
tm2Akngp = 667.0
#File:Sample5J.tiff
tm5Jkpgp = 484.0
tm5Jkngn = 59.0
tm5Jkpgn = 0.0
tm5Jkngp = 381.0
#File:Sample1J.tiff
tm1Jkpgp = 2374.0
tm1Jkngn = 145.0
tm1Jkpgn = 0.0
tm1Jkngp = 367.0
#File:Sample6A.tiff
tm6Akpgp = 743.0
tm6Akngn = 40.0
tm6Akpgn = 0.0
tm6Akngp = 509.0
#File:Sample3F.tiff
tm3Fkpgp = 304.0
tm3Fkngn = 66.0
tm3Fkpgn = 0.0
tm3Fkngp = 216.0


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
tmp1 = np.array([tm4Bkngp,
tm3Ikngp,
tm1Ikngp,
tm6Bkngp,
tm2Ckngp,
tm2Bkngp,
tm6Ckngp,
tm1Hkngp,
tm3Hkngp,
tm4Ckngp,
tm6Dkngp,
tm2Ekngp,
tm4Dkngp,
tm2Ikngp,
tm6Ikngp,
tm1Bkngp,
tm4Ekngp,
tm5Ckngp,
tm6Ekngp,
tm6Fkngp,
tm6Jkngp,
tm1Akngp,
tm5Akngp,
tm6Gkngp,
tm1Gkngp,
tm2Akngp,
tm5Jkngp,
tm1Jkngp,
tm6Akngp,
tm3Fkngp])

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

p1 = plt.scatter(tmp1, hp1, marker='*', color='red')

tmp2 = np.array([tm4Bkpgn,
tm3Ikpgn,
tm1Ikpgn,
tm6Bkpgn,
tm2Ckpgn,
tm2Bkpgn,
tm6Ckpgn,
tm1Hkpgn,
tm3Hkpgn,
tm4Ckpgn,
tm6Dkpgn,
tm2Ekpgn,
tm4Dkpgn,
tm2Ikpgn,
tm6Ikpgn,
tm1Bkpgn,
tm4Ekpgn,
tm5Ckpgn,
tm6Ekpgn,
tm6Fkpgn,
tm6Jkpgn,
tm1Akpgn,
tm5Akpgn,
tm6Gkpgn,
tm1Gkpgn,
tm2Akpgn,
tm5Jkpgn,
tm1Jkpgn,
tm6Akpgn,
tm3Fkpgn])

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

p2 = plt.scatter(tmp2, hp2, marker='d', color='blue')

tmp3 = np.array([tm4Bkpgp,
tm3Ikpgp,
tm1Ikpgp,
tm6Bkpgp,
tm2Ckpgp,
tm2Bkpgp,
tm6Ckpgp,
tm1Hkpgp,
tm3Hkpgp,
tm4Ckpgp,
tm6Dkpgp,
tm2Ekpgp,
tm4Dkpgp,
tm2Ikpgp,
tm6Ikpgp,
tm1Bkpgp,
tm4Ekpgp,
tm5Ckpgp,
tm6Ekpgp,
tm6Fkpgp,
tm6Jkpgp,
tm1Akpgp,
tm5Akpgp,
tm6Gkpgp,
tm1Gkpgp,
tm2Akpgp,
tm5Jkpgp,
tm1Jkpgp,
tm6Akpgp,
tm3Fkpgp])

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

p3 = plt.scatter(tmp3, hp3, marker='^', color='green')

tmp4 = np.array([tm4Bkngn,
tm3Ikngn,
tm1Ikngn,
tm6Bkngn,
tm2Ckngn,
tm2Bkngn,
tm6Ckngn,
tm1Hkngn,
tm3Hkngn,
tm4Ckngn,
tm6Dkngn,
tm2Ekngn,
tm4Dkngn,
tm2Ikngn,
tm6Ikngn,
tm1Bkngn,
tm4Ekngn,
tm5Ckngn,
tm6Ekngn,
tm6Fkngn,
tm6Jkngn,
tm1Akngn,
tm5Akngn,
tm6Gkngn,
tm1Gkngn,
tm2Akngn,
tm5Jkngn,
tm1Jkngn,
tm6Akngn,
tm3Fkngn])

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

p4 = plt.scatter(tmp4, hp4, marker='o', color='cyan')

x = np.linspace(0, 3000, num=len(tmp1))

# Add best fit lines
m1, b1 = np.polyfit(tmp1,hp1, 1)
fit_p1 = plt.plot(x, m1*x+b1, '-r')

#m2, b2 = np.polyfit(wp2,hp2, 1)
#fit_p2 = plt.plot(x, m2*x+b2, '-b')

m3, b3 = np.polyfit(tmp3,hp3, 1)
fit_p3 = plt.plot(x, m3*x+b3, '-g')

m4, b4 = np.polyfit(tmp4,hp4, 1)
fit_p4 = plt.plot(x, m4*x+b4, '-c')


plt.xlabel('Template Matching')
plt.ylabel('HALO')
plt.legend((p1, p2, p3, p4), ('KRT5-/GATA3+', 'KRT5+/GATA3-', 'KRT5+/GATA3+', 'KRT5-/GATA3-'), fontsize=10, ncol=1, framealpha=0, fancybox=True,bbox_to_anchor=(1.04,1))
plt.tight_layout()
plt.title('Template Matching vs. HALO')

plt.show()

