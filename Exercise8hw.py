#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:53:26 2018

@author: saurylara
"""
#Import matplot
import numpy 
import pandas
import matplotlib.pyplot as plt

#Import the UWvMSU file
UWvMSU=pandas.read_csv("/Users/saurylara/Desktop/ICB_EX8/UWvMSU_1-22-13.txt",sep="\t",header=0)
print(UWvMSU)

#Designate variables for data representing time values of different quarters
numQuarterOne = UWvMSU[UWvMSU['time'] < 10]
print(numQuarterOne)

numQuarterTwo = UWvMSU[UWvMSU['time'].between(10, 20, inclusive=True)]
print(numQuarterTwo)

numQuarterThree = UWvMSU[UWvMSU['time'].between(20, 30, inclusive=True)]
print(numQuarterThree)

numQuarterFour = UWvMSU[UWvMSU['time'].between(30, 40, inclusive=True)]
print(numQuarterFour)

#Create a new column representative of the quarter number
quarterList = []

for x in range(len(numQuarterOne)):
    quarterList.append("QuarterOne")
    
for x in range(len(numQuarterTwo)):
    quarterList.append("QuarterTwo")
    
for x in range(len(numQuarterThree)):
    quarterList.append("QuarterThree")
    
for x in range(len(numQuarterFour)):
    quarterList.append("QuarterFour")

UWvMSU["quarter"] = quarterList
print(UWvMSU)

#Create a for loop that allows for cumulative scores to be attained
UWsum = 0
MSUsum = 0

UWscore = []
MSUscore = []

for i in range(50):
   print(UWvMSU.iloc[i]['team'])
   if UWvMSU.iloc[i]['team'] =='UW':
        print("UW score")
        UWsum = UWsum + UWvMSU.iloc[i]['score'] 
        UWscore.append(UWsum)
        MSUscore.append(MSUsum)
   else: 
        MSUsum = MSUsum + UWvMSU.iloc[i]['score'] 
        MSUscore.append(MSUsum)
        UWscore.append(UWsum)
        
print(MSUscore)
print(UWscore)

#Obtain the values for time in the dataset
time = UWvMSU["time"]
print(time)

#Plot the cumulative data on a graph with quarter number on the x-axis and score on the y-axis
plt.plot(time,UWscore,'r-',time,MSUscore,'g-')
plt.xticks([5,15,25,35],["1st","2nd","3rd","4th"])

#Import the "random" module and define the "random" function
import random
n = random.randint(1, 100)

#Construct a while loop to guess a random number
guess = int(raw_input("I'm thinking of a number from 1 to 100: "))
while n != "guess":
    print
    if guess < n:
        print "Higher"
        guess = int(raw_input("I'm thinking of a number from 1 to 100: "))
    elif guess > n:
        print "Lower"
        guess = int(raw_input("I'm thinking of a number from 1 to 100: "))
    else:
        print "correct!"
        break
    print
