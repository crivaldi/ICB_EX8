# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:54:34 2018

@author: Alicia
"""
#Question 1
import pandas
import matplotlib.pyplot as plt

df=pandas.read_csv("UWvMSU_1-22-13.txt",sep="\t",header=0)
print(df)
df["UWscore"]=df.loc[df["team"]=="UW","score"].cumsum()
df["MSUscore"]=df.loc[df["team"]=="MSU","score"].cumsum()
df2=df.fillna(method="ffill")
df2=df.fillna(0)
print(df2)
sorted_data=df2.sort_values('time')
print(sorted_data)
df2.loc[df2['time'].between(0,10.99),'Quarter']='First'
df2.loc[df2['time'].between(11,20.99),'Quarter']='Second'
df2.loc[df2['time'].between(21,30.99),'Quarter']='Third'
df2.loc[df2['time'].between(31,40.99),'Quarter']='Fourth'
print(df2)
plt.plot(df2["Quarter"],df2["UWscore"],"r-",df2["Quarter"],df2["MSUscore"],"g-")
plt.grid(True)
plt.axes(["First","Fourth", 0, 50])
plt.xticks(['First','Second','Third','Fourth'])
plt.axes().spines["left"].set_position(("data",40))
#Note that when I convert time to quarters on the x-axis it returns lines with vertical additions at each x-axis tick (I am not sure how to get rid of this)
#If I were to comment out the lines that create the 'Quarter' column and change plt.plot(df2["Quarter"],df2["UWscore"],"r-",df2["Quarter"],df2["MSUscore"],"g-")
#to plt.plot(df2["time"],df2["UWscore"],"r-",df2["time"],df2["MSUscore"],"g-") I would get a continuous graph but the x-axis would only be labeled by time and not by quarters

#Question 2 - Guess My Number
import random

n = random.randint(1, 100)
print('I am thinking of a number between 1 and 100.')
guess = input("Take a guess ")
guess = int(guess)
while n != "guess":
    print(guess)
    if guess < n:
        print('Your guess is too low.')
        guess = input("Take a guess ")
        guess = int(guess)
    elif guess > n:
        print('Your guess is too high.')
        guess = input("Take a guess ")
        guess = int(guess)
    else:
        print("You guessed right!")
        break
    print



