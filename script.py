#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:47:03 2018

Biocomputing Exercise 8

@author: syli
"""

#%% Challenge 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dat = pd.read_table("UWvMSU_1-22-13.txt")
dat['UWscore'] = 0
dat['MSUscore'] = 0

for i in range(0,dat.shape[0]):
    if i == 0:
        if dat.loc[i,'team'] == "UW":
            dat.loc[i,'UWscore'] = dat.loc[i,'score']
        else: 
            dat.loc[i,'MSUscore'] = dat.loc[i,'score']
    else: 
        if dat.loc[i,'team'] == "UW":
            dat.loc[i,'UWscore'] = dat.loc[i-1,'UWscore']+ dat.loc[i,'score']
            dat.loc[i,'MSUscore'] = dat.loc[i-1,'MSUscore']
        else:
            dat.loc[i,'MSUscore'] = dat.loc[i-1,'MSUscore']+ dat.loc[i,'score']
            dat.loc[i,'UWscore'] = dat.loc[i-1,'UWscore']

plt.plot(dat.loc[:,"time"],dat.loc[:,"UWscore"],'r-',dat.loc[:,"time"],dat.loc[:,"MSUscore"],'g-')
plt.legend(['UW','MSU'],loc='upper left')
plt.xticks(np.arange(0, 41, 10))
plt.xlabel('Time', fontsize=15)
plt.ylabel('Score', fontsize=15)
plt.grid()
plt.show()


#%% Challenge 2
