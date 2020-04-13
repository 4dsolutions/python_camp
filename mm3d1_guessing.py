#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:34:52 2020

@author: MightyMoose3

An elegant rendering of the guessing game
concept.  Thanks to all.
"""

import random

answer = random.randint(1, 100)

while True:
    guess = input("What is your guess? > ")
    
    if guess.lower() == "q":
        print("OK you wanted to quit")
        break
    if not guess.isdigit():
        print("Try again")
        continue
    guess = int(guess)  
    if guess == answer:
        print("You win!")
        break
    if guess < answer:
        print("Too low")
    if guess > answer:
        print("Too high")
    
print("Game Over")
    
    