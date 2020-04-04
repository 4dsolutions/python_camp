# -*- coding: utf-8 -*-
"""
(c) Apache License
Demonstrates passing arguments from the OS shell (sys.argv)
Demonstrates unicode "strata" (unofficial term) in various
hexadecimal ranges

@author: Kirby Urner
"""

def emoji():
    for codepoint in range(int('1F600', 16), int('1F620', 16)):
        print(chr(codepoint), end=" ")
    print()

def food_emoji():
    emoji = [chr(codepoint) for codepoint in range(127812, 127857)]    
    for e in emoji:
        print(e, end=" ")
    print()

def hebrew():
    for codepoint in range(int('05D0', 16), 
                           int('05DA', 16)):
        print(chr(codepoint), end="")
    print()
     
def greek():
    for codepoint in range(int('03D0', 16), int('03FF', 16)):
        print(chr(codepoint), end="")
    print()
        
def korean():
    for codepoint in range(int('BB00', 16), int('BBAF', 16)):
        print(chr(codepoint), end="")
    print()
        
def arabic():
    print([chr(codepoint) 
    for codepoint in range(int('0681', 16), 
                           int('06AF', 16))])
    print()

def main():
    print("\nEMOJI")
    emoji()
    print("\n\nHEBREW")
    hebrew()
    print("\n\nGREEK & COPTIC")        
    greek()
    print("\n\nKOREAN")
    korean()
    print("\n\nARABIC")
    arabic()
    print()

def the_help():
    print("$ python unicode_fun.py name\n"
          "where name is:\n"
          "arabic, hebrew, greek, korean, emoji, all\n")

menu_options = {
        "arabic": arabic,
        "hebrew": hebrew,
        "greek": greek,
        "korean": korean,
        "emoji": emoji, 
        "all": main,
        "--help": the_help,
        "-h": the_help}
    
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        requested_unicode = sys.argv[1]
        print(sys.argv)
        if requested_unicode in menu_options:
            # don't just eval() whatever is passed in!
            menu_options[requested_unicode]()
    else:       
        the_help()
    
    