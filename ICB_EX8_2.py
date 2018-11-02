# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Generates a random number between 1 and 100 and prompts the user to guess it under threat of stealing the user's soul.
import random
rando = random.randint(1, 100)
guess = int(raw_input("Type a number between 1 and 100. If you are wrong, I will steal your soul: "))
while rando != "guess":
    print
    if guess < rando:
        print "Too low. One more chance for your soul."
        guess = int(raw_input("Type a number between 1 and 100. If you are wrong, I will steal your soul: "))
    elif guess > rando:
        print "Too high. One more chance for your soul."
        guess = int(raw_input("Type a number between 1 and 100. If you are wrong, I will steal your soul: "))
    else:
        print "Correct! I will not steal your soul. I am just a computer anyway."
        break
    print
