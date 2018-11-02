# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 20:44:59 2018

@author: Alexis
"""
import pandas as pd
import matplotlib.pyplot as plt
Score_data=pd.read_csv('UWvMSU_1-22-13.txt',sep=("\t"),header=0) #reads the file to df
MSUTot=0; #init the MSU total
UWTot=0; #init the UW total
MSUArray=[] 
UWArray=[] 

for element in range(50): #For loop to go through 
    if (Score_data.iloc[element]['team']=='UW'): #if the row is UW
        UWTot=UWTot+Score_data.iloc[element]['score'] #Gets  the score if UW
        MSUArray.append(MSUTot) #appends the current total for MSU
        UWArray.append(UWTot) #Appends the current total for UW
    else:
        MSUTot=MSUTot+Score_data.iloc[element]['score'] #if the row is MSU
        MSUArray.append(MSUTot) #Appends the current total for MSU
        UWArray.append(UWTot)#Appends the current total for MSU
    
Score_data['UWTot']=UWArray #Adds a new column to df
Score_data['MSUTot']=MSUArray #Adds a new column to df
#plotting 
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(Score_data['time'],Score_data['MSUTot'],'g-') #plots one line
ax.plot(Score_data['time'],Score_data['UWTot'],'r-') #plots other line
ax.yaxis.tick_right() #moves y ticks to the right 
ax.set_xticks([5,15,25,35],minor=False) #sets ticks for major 
ax.set_xticklabels(["1st", "2nd", "3rd", "4th"],minor=False)  #Sets the xticklabes for minor
ax.set_xticks([10,20,30,40],      minor=True) #Sets  the xticks for minor
ax.set_yticks([10,20,30,40,50],      minor=True) #Sets the yticks for minor
ax.set_xticklabels([''], minor=True) #makes the minor labels not show
ax.grid(which='minor') #turns on grid for minor ticks
ax.set_xlim([0,40]) 
ax.set_ylim([0,50])
