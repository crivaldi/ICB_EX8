# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:28:38 2018

@author: vysan
"""

import random 
number=random.randint(1,100)
f=0
while f==0:
    guess=int(input("Guess:"))
    if guess < number:
        print "Higher"
    elif guess > number:
        print "Lower"
    else:
        print "Correct!"
        f=1

    
        

        
    
