# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 01:44:10 2018

@author: vysan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
df=pd.read_csv("UWvMSU_1-22-13.txt",delimiter="\t")
print df
df["UWscore"]=df.loc[df["team"]=="UW","score"].cumsum()
print df
df["MSUscore"]=df.loc[df["team"]=="MSU","score"].cumsum()
print df
dfinal=df.fillna(method="ffill")
dfinal.fillna(0)
print dfinal
first=dfinal[dfinal["time"].between(0,10)]
second=dfinal[dfinal["time"].between(10,20)]
third=dfinal[dfinal["time"].between(20,30)]
fourth=dfinal[dfinal["time"].between(40,50)]
to_quarter={"first":"1st","second":"2nd","third":"3rd","fourth":"4th"}
#I got stuck with creating a new column with the new strings for the quarters.  

plt.plot(dfinal["time"],dfinal["UWscore"],"r-",dfinal["time"],dfinal["MSUscore"],"g-")
plt.grid(True)
plt.axis([0, 40, 0, 50])
plt.xticks([0, 10, 20, 30, 40])
plt.axes().spines["left"].set_position(("data",40))









