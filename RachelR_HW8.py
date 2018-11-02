# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:48:15 2018

@author: Rachel R
"""

#HW 8 Question 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
bball=pd.read_csv("UWvMSU_1-22-13.txt",sep="\t",header=0)
UW=bball[bball.team.str.contains('UW')]
UWscore=np.cumsum(UW.score)
MSU=bball[bball.team.str.contains('MSU')]
MSUscore=np.cumsum(MSU.score)
plt.plot(bball.time,UWscore,'-r',bball.time,MSUscore,'-g') 
plt.xlabel('Time')
plt.ylabel('Scores')
plt.grid(True)
plt.savefig("cscore.png")
plt.show() #usingg plt package did not work so I will run a ggplot
from plotnine import *
cscore = (bball.groupby(by=['team', 'time']).sum().groupby(level=[0]).cumsum())
cteam = cscore.reset_index(level=['team', 'time'])
a=ggplot(cteam,aes(x="time",y="score", color="team"))
a+geom_point()+geom_line()

#HW 8 Question 2
print("I'm thinking of a number 1-100...")
number = np.random.choice(101)
guess = int(raw_input("guess:"))
while number != 'guess':
    guess = int(raw_input("guess:"))
    if guess > number:
        print('Lower')
        guess = int(raw_input("guess"))
    elif guess < number:
        print('Higher')
        guess = int(raw_input("guess:"))
    else:
        print('Correct!')
        break 
print
