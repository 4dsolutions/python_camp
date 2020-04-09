#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:27:04 2020

@author: Kirby Swallows Sans
"""
import random

class Dog:
    
    def __init__(self, nm, how_old):
        self.name = nm
        self.age = how_old
        self.stomach = [ ]
        
    def eat(self, food):
        self.stomach.append(food)
        
    def barf(self):
        contents = " ".join(self.stomach)
        self.stomach = [ ]
        return contents
    
    def bark(self, n=1):
        return "bark!" * n
    
    def __repr__(self):
        return 'Dog("{}", {})'.format(self.name, self.age)
    
def test_dog():
    doggie = Dog("Rover", 3)
    foods = """
    🍄 🍅 🍆 🍇 🍈 🍉 🍊 🍌 🍍 🍎 
    🍏 🍐 🍑 🍒 🍓 🍔 🍕 🍗 🍘 🍙 
    🍚 🍛 🍜 🍝 🍞 🍟 🍠 🍢 🍣 🍤 
    🍥 🍦 🍧 🍨 🍩 🍪 🍫 🍭 🍮 🍯 
    🍰 
    """.split()
    # eat between one and five things
    meal = random.choices(foods, k=random.randint(1, 5))
    print("Eating a meal of {} things".format(len(meal)))
    for f in meal:
        doggie.eat(f)
    # oh oh, something doggie ate was unsuitable
    print("doggie doesn't feel well.")
    print(doggie.barf())
    
if __name__ == "__main__":
    test_dog()
    