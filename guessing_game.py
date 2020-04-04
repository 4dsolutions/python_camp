#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:38:54 2020

This is a docstring

@author: Kirby Urner
"""

from random import randint

answer = randint(1, 100)
# print(answer)

guess_counter = 0
looping = True

while looping:

    guess = input("What is your guess? > ")

    if guess.isdigit():
        guess = int(guess)

        # check if correct or too high / low
        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        elif guess == answer:  # just right
            print("You got it!")
            looping = False

    else:

        if guess.isalpha() and guess.lower() == "quit":
            looping = False

    guess_counter += 1

    if guess_counter > 5:
        print("Too many guesses, better luck next time.")
        looping = False

print("Game Over")
