# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:47:02 2018

Exercise08

@author: Patricia
"""

import pandas
import matplotlib.pyplot as plt

# Part 1 Analysis of Sports Teaam data

# data loaded into a data frame
scores=pandas.read_csv("UWvMSU_1-22-13.txt", sep="\t")

# add 2 columns to the dataframe: UW's score and MSU's score
length_scores = len(scores)
temp_UW = 0 # initialize empty scores
temp_MSU = 0
list_UW=[] # initialize empty lists
list_MSU=[]

for x in range(0,length_scores):
    if scores.iloc[x][1]=="UW":
        temp_UW = temp_UW + int(scores.iloc[x][2])
        # add the temp UW AND MSU score to the list
        list_UW.append(temp_UW)
        list_MSU.append(temp_MSU)
        
    elif scores.iloc[x][1]=="MSU":
        temp_MSU = temp_MSU + int(scores.iloc[x][2])
        # add the temp MSU AND UW score to the list
        list_MSU.append(temp_MSU)
        list_UW.append(temp_UW)

# insert the completes lists into the dataframe scores
scores.insert(3,"UWscore",list_UW)
scores.insert(4, "MSUscore",list_MSU)
# plot the scores
print("Michigan State is green")
print("University of Wisconsin is red")
plt.plot(scores["time"],scores["UWscore"],'r-',scores["time"],scores["MSUscore"],'g-')
plt.ylabel('Score')
plt.xlabel('Time')
plt.show


# Part 2: Guess my number
from random import randint
number = randint(0,100)

print("I'm thinking of a number  1-100. Can you guess my number? ")
input_num=int(input())
print(number)

while number != input_num:
    if input_num < number:
        print("You're wrong! Guess a higher number: ")
    elif input_num > number:
        print("You're wrong! Guess a lower number: ")
    input_num = int(input())

print("Correct! Good job.")
    
































