#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyCamp: a collaborative project

Bugs found:
    
    To fix:
    crashes when user types words
"""

import math
import random
import time

def squares():
    print("Choose a number 1 through 100.")
    number = int(input())
    square = number**2
    print("The square of", number, "is", square)
        
def square_roots():    
    print("Choose a number 1 through 100.")
    num = int(input())
    root = math.sqrt(num)
    print("The square root of", num, "is", root)

def any_power():
    num = float(input("Choose a number > "))
    exp = float(input("Raise to what power? > "))
    print( pow(num, exp))
    
# this could come in handy
menu_options = {"1": squares, 
                "2": square_roots,
                "3": any_power,
                "0": "exit"}
        
def menu():
    looping = True
    while looping:
        # can we make this a loop that keeps asking?
        print("""
        1. Squares 
        2. Square roots 
        3. Raise to Any Power
        0. Exit
        
        Pick one please""")
        
        do_it = input("    >>> ")
        # print("You picked", do_it)
        
        if not do_it in menu_options:
            print("Please pick 1, 2, 3, 0")
            continue
            
        do_it = int(do_it)
        
        if do_it == 0:
            looping = False
        elif do_it == 1:
            squares()
        elif do_it == 2:
            square_roots()
        elif do_it == 3:
            any_power()
            
    
menu()