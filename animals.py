#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:27:04 2020

@author: Kirby Swallows Sans
"""

class Dog:
    
    def __init__(self, nm, how_old):
        self.name = nm
        self.age = how_old
        self.stomach = [ ]
        
    def eat(self, food):
        self.stomach.append(food)
        
    def get_sick(self):
        self.stomach = [ ]
    
    def bark(self, n=1):
        return "bark!" * n
    
    def __repr__(self):
        return 'Dog("%s", %s)' % (self.name, self.age)
    
