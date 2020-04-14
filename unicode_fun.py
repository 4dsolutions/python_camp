# -*- coding: utf-8 -*-
"""
(c) Apache License
Demonstrates passing arguments from the OS shell (sys.argv)
Demonstrates unicode "strata" (unofficial term) in various
hexadecimal ranges

@author: Kirby Urner
"""
import sys

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
    global letters
    letters = [chr(codepoint) 
                for codepoint in 
                    range(int('05D0', 16), 
                          int('05EB', 16))]
    print("".join(letters))
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
    print(" ".join([chr(codepoint) 
    for codepoint in range(int('0681', 16), 
                           int('06AF', 16))]))
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

def html():
    """
    This is a fancy advanced option.  The point of saving all the
    output to an HTML file is maybe your browser will do an even 
    better job of rendering these unicode characters, worth a try.
    
    https://kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python
    https://www.blog.pythonlibrary.org/2016/06/16/python-101-redirecting-stdout/
    """
    original = sys.stdout
    sys.stdout = open("unicode.html", "w", encoding='utf-8')
    print("<html><head><title>Unicode Stuff</title></head>")
    print("<body>")
    main() # everything will go to the file this way
    print("</body>")
    print("</html>")
    sys.stdout.flush()
    sys.stdout.close()
    sys.stdout = original
    # Now lets put in some line breaks, since HTML
    # pays little attention to newlines \n
    with open("unicode.html", "r", encoding='utf-8') as the_file:
        text = the_file.read().replace("\n", "<br />")
    with open("unicode.html", "w", encoding='utf-8') as the_file2:
        the_file2.write(text)
    print("OK, open unicode.html in browser")
    
    
def the_help():
    options = " ".join(sorted(menu_options.keys()))
    print("$ python -m unicode_fun name\n"
          "where name is:\n",
          options + "\n")

menu_options = {
        "arabic": arabic,
        "hebrew": hebrew,
        "greek": greek,
        "korean": korean,
        "emoji": emoji, 
        "food" : food_emoji,
        "all": main,
        "html": html,
        "--help": the_help,
        "-h": the_help}
    
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        requested_unicode = sys.argv[1]
        # print(sys.argv)
        if requested_unicode in menu_options:
            # don't just eval() whatever is passed in!
            menu_options[requested_unicode]()
    else:       
        the_help()
    
    