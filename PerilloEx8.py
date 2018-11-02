import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

####Answer to number 1####

scores=pd.read_csv("UWvMSU_1-22-13.csv")

UW=scores[scores.team.str.contains("UW")]
UW
UW_Scores=np.cumsum(UW.score)
UW_Time=(UW.time)

MSU=scores[scores.team.str.contains("MSU")]
MSU
MSU_Scores=np.cumsum(MSU.score)
MSU_Time=(MSU.time)

plt.plot(UW_Time, UW_Scores, 'r-', MSU_Time, MSU_Scores, 'g-') 
plt.title("UW (red) versus MSU (green) 1/22/13")
plt.xlabel("Time")
plt.ylabel("Number of Points")


plt.legend()


####Answer to number 2####
def guess_game():
    number=range(1, 100)
    num=np.random.choice(n)
    guess = int(raw_input("Enter an integer from 1 to 99:"))
    while num != guess:
        if guess < num:
            print "guess is low"
            guess = int(raw_input("Enter an integer from 1 to 99:"))
        elif guess > num:
            print "guess is high"
            guess = int(raw_input("Enter an integer from 1 to 99:"))
    print "you guessed it!"
            
guess_game()
