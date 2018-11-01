# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:54:34 2018

@author: Alicia
"""

import numpy
import pandas
from plotnine import *
import matplotlib.pyplot as plt

game=pandas.read_csv("UWvMSU_1-22-13.txt",sep="\t",header=0)

a=ggplot(game,aes(x="time",y="score"))
a+geom_point()+coord_cartesian()+theme_classic()
plt.plot(time,UWscore,'r-',time,MSUscore,'g-')


#Question 2 - Guess my Number
n = numpy.random.choice(1, 99)
guess = int(numpy.random.choice("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print("Guess is too low")
        guess = int(numpy.random.choice("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("Guess is too high")
        guess = int(numpy.random.choice("Enter an integer from 1 to 99: "))
    else:
        print("You guessed right!")
        break
    print