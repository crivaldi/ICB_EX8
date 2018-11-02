# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 23:58:52 2018

@author: Alexis
"""

import numpy as np
NumbersArray=np.arange(1,101) #Makes an array from 1-100
NumberPicked=np.random.choice(NumbersArray) #Randomly picks a number
NumberCorrect=0 #toggle if you have chosen correctly

while(NumberCorrect==0): #while not chosen correctly
    Guess=input("I am thinking of a number from 1-100. What is it?") #what is shown to user
    if Guess==NumberPicked: 
        print('Correct!')
        NumberCorrect=1
    elif Guess>NumberPicked:
        print('Lower')
    elif Guess<NumberPicked:
        print('Higher')
    else:
        print('error') 