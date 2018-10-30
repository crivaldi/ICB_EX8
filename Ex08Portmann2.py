# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:40:20 2018

Exercise 08 - Part 2 
Guess my number game

@author: Patricia
"""

# Part 2: Guess my number
from random import randint
number = randint(0,100)

print("I'm thinking of a number  1-100. Can you guess my number? ")
input_num=int(input())

while number != input_num:
    if input_num < number:
        print("You're wrong! Guess a higher number: ")
    elif input_num > number:
        print("You're wrong! Guess a lower number: ")
    input_num = int(input())

print("Correct! Good job.")
