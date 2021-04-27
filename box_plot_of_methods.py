#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:23:11 2021

@author: genevieve.hayes
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

SAVEIMG = 1

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
w4Bkpgp = 9.0
w4Bkngn = 174.0
w4Bkpgn = 0.0
w4Bkngp = 2237.0
#File:Sample3I.tiff
w3Ikpgp = 52.0
w3Ikngn = 103.0
w3Ikpgn = 6.0
w3Ikngp = 83.0
#File:Sample1I.tiff
w1Ikpgp = 1904.0
w1Ikngn = 501.0
w1Ikpgn = 40.0
w1Ikngp = 578.0
#File:Sample6B.tiff
w6Bkpgp = 2619.0
w6Bkngn = 1141.0
w6Bkpgn = 40.0
w6Bkngp = 2552.0
#File:Sample2C.tiff
w2Ckpgp = 502.0
w2Ckngn = 1137.0
w2Ckpgn = 0.0
w2Ckngp = 3861.0
#File:Sample2B.tiff
w2Bkpgp = 43.0
w2Bkngn = 248.0
w2Bkpgn = 4.0
w2Bkngp = 673.0
#File:Sample6C.tiff
w6Ckpgp = 76.0
w6Ckngn = 1037.0
w6Ckpgn = 0.0
w6Ckngp = 4674.0
#File:Sample1H.tiff
w1Hkpgp = 1123.0
w1Hkngn = 227.0
w1Hkpgn = 10.0
w1Hkngp = 132.0
#File:Sample3H.tiff
w3Hkpgp = 395.0
w3Hkngn = 1333.0
w3Hkpgn = 4.0
w3Hkngp = 3346.0
#File:Sample4C.tiff
w4Ckpgp = 269.0
w4Ckngn = 867.0
w4Ckpgn = 4.0
w4Ckngp = 3993.0
#File:Sample6D.tiff
w6Dkpgp = 218.0
w6Dkngn = 798.0
w6Dkpgn = 2.0
w6Dkngp = 2655.0
#File:Sample2E.tiff
w2Ekpgp = 282.0
w2Ekngn = 483.0
w2Ekpgn = 5.0
w2Ekngp = 2241.0
#File:Sample4D.tiff
w4Dkpgp = 1492.0
w4Dkngn = 1068.0
w4Dkpgn = 3.0
w4Dkngp = 4730.0
#File:Sample2I.tiff
w2Ikpgp = 105.0
w2Ikngn = 562.0
w2Ikpgn = 1.0
w2Ikngp = 1450.0
#File:Sample6I.tiff
w6Ikpgp = 8.0
w6Ikngn = 594.0
w6Ikpgn = 0.0
w6Ikngp = 1352.0
#File:Sample1B.tiff
w1Bkpgp = 3.0
w1Bkngn = 210.0
w1Bkpgn = 0.0
w1Bkngp = 2608.0
#File:Sample4E.tiff
w4Ekpgp = 519.0
w4Ekngn = 970.0
w4Ekpgn = 32.0
w4Ekngp = 1106.0
#File:Sample5C.tiff
w5Ckpgp = 87.0
w5Ckngn = 1441.0
w5Ckpgn = 0.0
w5Ckngp = 4602.0
#File:Sample6E.tiff
w6Ekpgp = 125.0
w6Ekngn = 349.0
w6Ekpgn = 0.0
w6Ekngp = 2417.0
#File:Sample6F.tiff
w6Fkpgp = 11.0
w6Fkngn = 164.0
w6Fkpgn = 0.0
w6Fkngp = 530.0
#File:Sample6J.tiff
w6Jkpgp = 457.0
w6Jkngn = 849.0
w6Jkpgn = 1.0
w6Jkngp = 3510.0
#File:Sample1A.tiff
w1Akpgp = 22.0
w1Akngn = 276.0
w1Akpgn = 0.0
w1Akngp = 2673.0
#File:Sample5A.tiff
w5Akpgp = 67.0
w5Akngn = 260.0
w5Akpgn = 2.0
w5Akngp = 1658.0
#File:Sample6G.tiff
w6Gkpgp = 4916.0
w6Gkngn = 606.0
w6Gkpgn = 1.0
w6Gkngp = 973.0
#File:Sample1G.tiff
w1Gkpgp = 1880.0
w1Gkngn = 161.0
w1Gkpgn = 15.0
w1Gkngp = 53.0
#File:Sample2A.tiff
w2Akpgp = 75.0
w2Akngn = 431.0
w2Akpgn = 1.0
w2Akngp = 1888.0
#File:Sample5J.tiff
w5Jkpgp = 570.0
w5Jkngn = 253.0
w5Jkpgn = 3.0
w5Jkngp = 574.0
#File:Sample1J.tiff
w1Jkpgp = 3593.0
w1Jkngn = 345.0
w1Jkpgn = 31.0
w1Jkngp = 78.0
#File:Sample6A.tiff
w6Akpgp = 1242.0
w6Akngn = 1107.0
w6Akpgn = 5.0
w6Akngp = 1276.0
#File:Sample3F.tiff
w3Fkpgp = 535.0
w3Fkngn = 248.0
w3Fkpgn = 6.0
w3Fkngp = 242.0

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



#COMBINED method
#File:Sample4B.tiff
tm4Bkpgp = 9.0
tm4Bkngn = 271.0
tm4Bkpgn = 0.0
tm4Bkngp = 1355.0
#File:Sample3I.tiff
tm3Ikpgp = 61.0
tm3Ikngn = 336.0
tm3Ikpgn = 6.0
tm3Ikngp = 291.0
#File:Sample1I.tiff
tm1Ikpgp = 1980.0
tm1Ikngn = 94.0
tm1Ikpgn = 40.0
tm1Ikngp = 681.0
#File:Sample6B.tiff
tm6Bkpgp = 2683.0
tm6Bkngn = 273.0
tm6Bkpgn = 40.0
tm6Bkngp = 1343.0
#File:Sample2C.tiff
tm2Ckpgp = 502.0
tm2Ckngn = 810.0
tm2Ckpgn = 0.0
tm2Ckngp = 1654.0
#File:Sample2B.tiff
tm2Bkpgp = 49.0
tm2Bkngn = 53.0
tm2Bkpgn = 4.0
tm2Bkngp = 413.0
#File:Sample6C.tiff
tm6Ckpgp = 76.0
tm6Ckngn = 395.0
tm6Ckpgn = 0.0
tm6Ckngp = 1897.0
#File:Sample1H.tiff
tm1Hkpgp = 1145.0
tm1Hkngn = 90.0
tm1Hkpgn = 10.0
tm1Hkngp = 330.0
#File:Sample3H.tiff
tm3Hkpgp = 403.0
tm3Hkngn = 298.0
tm3Hkpgn = 4.0
tm3Hkngp = 1309.0
#File:Sample4C.tiff
tm4Ckpgp = 273.0
tm4Ckngn = 302.0
tm4Ckpgn = 4.0
tm4Ckngp = 1369.0
#File:Sample6D.tiff
tm6Dkpgp = 220.0
tm6Dkngn = 917.0
tm6Dkpgn = 2.0
tm6Dkngp = 1415.0
#File:Sample2E.tiff
tm2Ekpgp = 289.0
tm2Ekngn = 365.0
tm2Ekpgn = 5.0
tm2Ekngp = 1172.0
#File:Sample4D.tiff
tm4Dkpgp = 1495.0
tm4Dkngn = 199.0
tm4Dkpgn = 3.0
tm4Dkngp = 1490.0
#File:Sample2I.tiff
tm2Ikpgp = 107.0
tm2Ikngn = 696.0
tm2Ikpgn = 1.0
tm2Ikngp = 888.0
#File:Sample6I.tiff
tm6Ikpgp = 8.0
tm6Ikngn = 766.0
tm6Ikpgn = 0.0
tm6Ikngp = 772.0
#File:Sample1B.tiff
tm1Bkpgp = 3.0
tm1Bkngn = 34.0
tm1Bkpgn = 0.0
tm1Bkngp = 426.0
#File:Sample4E.tiff
tm4Ekpgp = 567.0
tm4Ekngn = 428.0
tm4Ekpgn = 32.0
tm4Ekngp = 669.0
#File:Sample5C.tiff
tm5Ckpgp = 87.0
tm5Ckngn = 591.0
tm5Ckpgn = 0.0
tm5Ckngp = 1608.0
#File:Sample6E.tiff
tm6Ekpgp = 127.0
tm6Ekngn = 364.0
tm6Ekpgn = 0.0
tm6Ekngp = 1043.0
#File:Sample6F.tiff
tm6Fkpgp = 11.0
tm6Fkngn = 378.0
tm6Fkpgn = 0.0
tm6Fkngp = 462.0
#File:Sample6J.tiff
tm6Jkpgp = 459.0
tm6Jkngn = 862.0
tm6Jkpgn = 1.0
tm6Jkngp = 1940.0
#File:Sample1A.tiff
tm1Akpgp = 22.0
tm1Akngn = 184.0
tm1Akpgn = 0.0
tm1Akngp = 752.0
#File:Sample5A.tiff
tm5Akpgp = 69.0
tm5Akngn = 90.0
tm5Akpgn = 2.0
tm5Akngp = 734.0
#File:Sample6G.tiff
tm6Gkpgp = 4917.0
tm6Gkngn = 145.0
tm6Gkpgn = 1.0
tm6Gkngp = 910.0
#File:Sample1G.tiff
tm1Gkpgp = 1898.0
tm1Gkngn = 90.0
tm1Gkpgn = 15.0
tm1Gkngp = 331.0
#File:Sample2A.tiff
tm2Akpgp = 78.0
tm2Akngn = 70.0
tm2Akpgn = 1.0
tm2Akngp = 698.0
#File:Sample5J.tiff
tm5Jkpgp = 573.0
tm5Jkngn = 61.0
tm5Jkpgn = 3.0
tm5Jkngp = 480.0
#File:Sample1J.tiff
tm1Jkpgp = 3643.0
tm1Jkngn = 146.0
tm1Jkpgn = 31.0
tm1Jkngp = 607.0
#File:Sample6A.tiff
tm6Akpgp = 1254.0
tm6Akngn = 48.0
tm6Akpgn = 5.0
tm6Akngp = 511.0
#File:Sample3F.tiff
tm3Fkpgp = 546.0
tm3Fkngn = 69.0
tm3Fkpgn = 6.0
tm3Fkngp = 267.0

cp1 = np.array([tm4Bkngp,
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


cp2 = np.array([tm4Bkpgn,
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


cp3 = np.array([tm4Bkpgp,
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


cp4 = np.array([tm4Bkngn,
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

plt.title('Watershed vs. HALO')
plt.ylim([0,80000])
plt.tight_layout()

plt.show()

# In[]: Watershed Histogram ALL

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 22})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(5.5, 9.5)
plt.ylabel("Total Number of Cells Identified",fontsize=25)

p1G_h = plt.bar("K-/G+", np.sum(wp1), width, color='g')
p2G_h = plt.bar("K-/G-", np.sum(wp4), width, color='c')
p3G_h = plt.bar("K+/G+", np.sum(wp3), width, color='r')
p4G_h = plt.bar("K+/G-", np.sum(wp2), width, color='b')

plt.title("Watershed Method",fontsize=25)
plt.ylim([0,80000])
plt.tight_layout()
if SAVEIMG == 1:
    filename_output = "histograms_all/total_watershed_histogram.tiff"
    plt.savefig(filename_output)
    
plt.show()

# In[]: Template Matching Histogram ALL

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 22})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(5.5, 9.5)
plt.ylabel("Total Number of Cells Identified",fontsize=25)

p1G_h = plt.bar("K-/G+", np.sum(tmp1), width, color='g')
p2G_h = plt.bar("K-/G-", np.sum(tmp4), width, color='c')
p3G_h = plt.bar("K+/G+", np.sum(tmp3), width, color='r')
p4G_h = plt.bar("K+/G-", np.sum(tmp2), width, color='b')

plt.title("Template Matching Method",fontsize=25)
plt.ylim([0,80000])
plt.tight_layout()
if SAVEIMG == 1:
    filename_output = "histograms_all/total_TM_histogram.tiff"
    plt.savefig(filename_output)
    
plt.show()

# In[]: Combined Histogram ALL

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 22})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(5.5, 9.5)
plt.ylabel("Total Number of Cells Identified",fontsize=25)

p1G_h = plt.bar("K-/G+", np.sum(cp1), width, color='g')
p2G_h = plt.bar("K-/G-", np.sum(cp4), width, color='c')
p3G_h = plt.bar("K+/G+", np.sum(cp3), width, color='r')
p4G_h = plt.bar("K+/G-", np.sum(cp2), width, color='b')

plt.title("Combined Method",fontsize=25)
plt.ylim([0,80000])
plt.tight_layout()
if SAVEIMG == 1:
    filename_output = "histograms_all/total_Combined_histogram.tiff"
    plt.savefig(filename_output)
    
plt.show()

# In[]: HALO Histogram ALL

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 22})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(5.5, 9.5)
plt.ylabel("Total Number of Cells Identified",fontsize=25)

p1G_h = plt.bar("K-/G+", np.sum(hp1), width, color='g')
p2G_h = plt.bar("K-/G-", np.sum(hp4), width, color='c')
p3G_h = plt.bar("K+/G+", np.sum(hp3), width, color='r')
p4G_h = plt.bar("K+/G-", np.sum(hp2), width, color='b')

plt.title("HALO Analysis",fontsize=25)
plt.ylim([0,80000])
plt.tight_layout()
if SAVEIMG == 1:
    filename_output = "histograms_all/total_Halo_histogram.tiff"
    plt.savefig(filename_output)
    
plt.show()


# In[]: Bland-Altman Plot
width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 21})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(9.5, 5.5)

def bland_altman_plot(data1, data2, *args, **kwargs):
    data1     = np.asarray(data1)
    data2     = np.asarray(data2)
    mean      = np.mean([data1, data2], axis=0)
    diff      = data1 - data2                   # Difference between data1 and data2
    md        = np.mean(diff)                   # Mean of the difference
    sd        = np.std(diff, axis=0)            # Standard deviation of the difference
    lower     = md - 1.96*sd
    upper     = md + 1.96*sd

    plt.scatter(mean, diff, *args, **kwargs)
    plt.axhline(md,           color='gray', linestyle='--')
    plt.axhline(md + 1.96*sd, color='gray', linestyle='--')
    plt.axhline(md - 1.96*sd, color='gray', linestyle='--')
    
    plt.text(data1.max()*0.85, upper * 0.85, " 1.96 SD", color = "grey", fontsize = "14")
    plt.text(data1.max()*0.85, lower * 1.2, "-1.96 SD", color = "grey", fontsize = "14")
    

ba_p4 = bland_altman_plot(wp4, hp4)
#ba_p4 = plotblandaltman(wp4, hp4, 'Bland-Altman Plot KRT5-/GATA3-',1000)
plt.title('Bland-Altman Plot KRT5-/GATA3-')
plt.xlabel("Mean of Watershed and HALO")
plt.ylabel("Difference of Watershed and HALO")
plt.show()

# In[]: Box Plot

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 21})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10.5, 5.5)

plt.boxplot((wp4,tmp4,cp4,hp4))
plt.title('KRT5-/GATA3- Box Plot')
plt.xticks([1, 2, 3, 4], ['Watershed', 'Template Matching', 'Combined', 'HALO'])

if SAVEIMG == 1:
    filename_output = "box_plots/box_plot_kngn.tiff"
    plt.savefig(filename_output)

plt.show()

# In[]: Box Plot

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 21})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10.5, 5.5)

plt.boxplot((wp1,tmp1,cp1,hp1))
plt.title('KRT5-/GATA3+ Box Plot')
plt.xticks([1, 2, 3, 4], ['Watershed', 'Template Matching', 'Combined', 'HALO'])

if SAVEIMG == 1:
    filename_output = "box_plots/box_plot_kngp.tiff"
    plt.savefig(filename_output)

plt.show()

# In[]: Box Plot

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 21})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10.5, 5.5)

plt.boxplot((wp3,tmp3,cp3,hp3))
plt.title('KRT5+/GATA3+ Box Plot')
plt.xticks([1, 2, 3, 4], ['Watershed', 'Template Matching', 'Combined', 'HALO'])

if SAVEIMG == 1:
    filename_output = "box_plots/box_plot_kpgp.tiff"
    plt.savefig(filename_output)

plt.show()

# In[]: Box Plot

width = 0.7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
matplotlib.rc('text', usetex='false')
matplotlib.rcParams.update({'font.size': 21})
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10.5, 5.5)

plt.boxplot((wp2,tmp2,cp2,hp2))
plt.title('KRT5+/GATA3- Box Plot')
plt.xticks([1, 2, 3, 4], ['Watershed', 'Template Matching', 'Combined', 'HALO'])

if SAVEIMG == 1:
    filename_output = "box_plots/box_plot_kpgn.tiff"
    plt.savefig(filename_output)

plt.show()