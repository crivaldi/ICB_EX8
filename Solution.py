# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:18:15 2018

@author: Annaliese
"""

########################################

# Problem 1

# import packages
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# set working directory
os.chdir("Ex 8")

# import the tab- delimited data
data = pd.read_csv('footballdatatext.txt', sep = "\t")

# define variables
time = data['time']

UWscore = np.zeros(51)
MSUscore = np.zeros(51)
for row in range(50):
    if data.iloc[row, 1] == "UW":
        UWscore[row+1] = UWscore[row] + data.iloc[row, 2]
    else :
        MSUscore[row+1] = MSUscore[row] + data.iloc[row, 2]
    if UWscore[row+1] == 0:
        UWscore[row+1] = UWscore[row]
    if MSUscore[row+1] == 0:
        MSUscore[row+1] = MSUscore[row]
  
row = 3    
if data.iloc[row, 1] == "UW":
        UWscore[row+1] = UWscore[row] + data.iloc[row, 2]
else :
        MSUscore[row+1] = MSUscore[row] + data.iloc[row, 2]
if UWscore[row+1] == 0:
        UWscore[row+1] = UWscore[row]
if MSUscore[row+1] == 0:
        MSUscore[row+1] = MSUscore[row]

# remove first observation from score
UWscore = UWscore[1:]
MSUscore = MSUscore[1:]

# plot the data
plt.plot(time, UWscore, 'r-', time, MSUscore, 'g-')

########################################################

# Problem 2

# set choice vector
vector = range(1, 101)

# make selection
number = np.random.choice(vector)
def user_input(guess):
    print("Guess:" + str(guess))
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    else:
        print("Correct!")

user_input(32) # Lower
user_input(15) # Lower
user_input(8) # Correct
