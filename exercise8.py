#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:11:04 2018

@author: mlpoterek
"""

#Question 1: Graphing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

location = r'/Users/mlpoterek/Biocomp/ICB_EX8/UWvMSU_1-22-13.txt'
df = pd.read_csv(location, sep = '\t')

uw_temp = 0
uw_list = [] 
msu_list = []
msu_temp = 0

for x in range(0,len(df)):
    if df.iloc[x][1]=="UW":
        uw_temp = uw_temp + int(df.iloc[x][2])
        uw_list.append(uw_temp)
        msu_list.append(msu_temp)
        
    elif df.iloc[x][1]=="MSU":
        msu_temp = msu_temp + int(df.iloc[x][2])
        msu_list.append(msu_temp)
        uw_list.append(uw_temp)

df.insert(3,"UW_total",uw_list)
df.insert(4, "MSU_total",msu_list)

plt.plot(df["time"],df["UW_total"],'b-',df["time"],df["MSU_total"],'g-')
plt.ylabel('Score')
plt.xlabel('Time')
plt.show


#Question 2: Guess my number
import random

print("I'm thinking of a number 1-100...")
number = random.randint(1, 100)
incorrect = True

while (incorrect):
    print("Guess: ")
    guess = input()
    guess = int(guess)
    
    if guess < number:
        print("Higher")
    
    if guess > number:
        print("Lower")

    if guess == number:
        print("Correct!")
        break

