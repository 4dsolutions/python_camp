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
from fractions import Fraction

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
    exp = input("Raise to what power? > ")
    if "/" in exp:
        exp = float(Fraction(exp))
    else:
        exp = float(exp)
    print( pow(num, exp))

def evalFraction(f):
  if '/' in f:
    spl = f.split('/')
    return float(spl[0])/float(spl[1])
  else:
    return f

def isFrac(f):
  if '/' in f:
    print (f + " is a fraction")
  else:
    print(f + " is not a fraction")

def get_decimal():
    print("We are here")
    The_answer = input('Would you like to find the decimal value of a fraction type "1" >>> ')
    if (The_answer == "1"):
      print ('Type a fraction like _/_ ')
      fraction = input("What is your fraction >>> ")
      isFrac(fraction)
      if ('/' not in fraction):
        while isFrac(fraction) == False:
          fraction = input("What is your fraction >>> ")
          isFrac(fraction)
      print("Your fraction = ", evalFraction(fraction))


# this could come in handy
menu_options = {"1": squares, 
                "2": square_roots,
                "3": any_power,
                "4": get_decimal,
                "0": "exit"}
        
def menu():
    looping = True
    while looping:
        # can we make this a loop that keeps asking?
        print("""
        1. Squares 
        2. Square roots 
        3. Raise to Any Power
        4. Get Decimal
        0. Exit
        
        Pick one please""")
        
        do_it = input("    >>> ")
        # print("You picked", do_it)
        
        if not do_it in menu_options:
            print("Please pick 1, 2, 3, 4, 0")
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
        elif do_it == 4:
            get_decimal()
            
if __name__ == "__main__":    
    menu()

