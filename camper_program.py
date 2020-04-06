#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:57:31 2020

@author: mac
"""

import math
import random
import time


def squares():
    print("Choose a number 1 through 100.")
    number = int(input())
    square = number**2
    print("The square of", number, "is", square)
    print("Type 'repeat' to choose another number, or type 'done' to stop. If you want to use the square root calculator, type 'switch'. ")
    answer = str(input())
    if answer == str("repeat"):
        square_roots()
    elif answer == str("done"):
        print("Okay, thanks for using this program!")
    elif answer == str("switch"):
        square_roots()
        
def square_roots():    
    print("Choose a number 1 through 100.")
    num = int(input())
    root = math.sqrt(num)
    print("The square root of", num, "is", root)
    print("Type 'repeat' to choose another number, or type 'done' to stop. If you want to use the square calculator, type 'switch'")
    answer = str(input())
    if answer == str("repeat"):
        square_roots()
    elif answer == str("done"):
        print("Okay, thanks for using this program!")