#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:39:11 2018

@author: Alicia
"""

#Problem1
import pandas as pd
import matplotlib.pyplot as mpl
data = pd.read_csv('UWvMSU_1-22-13.txt',sep = '\t')

UW = data.copy()
MSU = data.copy()

del UW["team"]
del MSU["team"]

UW.iloc[0,1]=0
MSU.iloc[0,1]=0

UW.iloc[-1,1]=0 #Because when i=0 with UW.iloc[i-1,1], the -1 loops back to the bottom to count
MSU.iloc[-1,1]=0

for i in range(0,len(data.iloc[:,1])):
        if data.iloc[i,1] == "UW":
               UW.iloc[i,1]=UW.iloc[i-1,1]+data.iloc[i,2]
               MSU.iloc[i,1]=MSU.iloc[i-1,1]
        else:
               MSU.iloc[i,1]=MSU.iloc[i-1,1]+data.iloc[i,2]
               UW.iloc[i,1]=UW.iloc[i-1,1]
            
mpl.plot(data.iloc[:,0],UW.iloc[:,1],'r-',data.iloc[:,0],MSU.iloc[:,1],'g-')

#Problem2