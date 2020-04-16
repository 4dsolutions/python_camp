# -*- coding: utf-8 -*-
"""
(c) Apache License
Demonstrates passing arguments from the OS shell (sys.argv)
Demonstrates unicode "strata" (unofficial term) in various
hexadecimal ranges

@author: Kirby Urner
"""

def cherokee():
    """
    U+13A0 – U+13FF   (5024–5119)
    http://www.alanwood.net/unicode/cherokee.html
    (page only shows up to 13F4)
    """
    for codepoint in range(int('13A0', 16), int('13F4', 16)):
        print(chr(codepoint), end="")
    print("----")
    
def emoji():
    for codepoint in range(int('1F600', 16), int('1F620', 16)):
        print(chr(codepoint), end=" ")
    print("----")

def food_emoji():
    emoji = [chr(codepoint) for codepoint in range(127812, 127857)]    
    for e in emoji:
        print(e, end=" ")
    print("----")

def hebrew():
    """
    http://www.alanwood.net/unicode/hebrew.html
    U+0590 – U+05FF   (1424–1535)
    """
    global letters
    letters = [chr(codepoint) 
                for codepoint in 
                    range(int('05D0', 16), 
                          int('05EA', 16))]
    print("".join(letters))
    print("----")
     
def greek():
    for codepoint in range(int('03D0', 16), int('03FF', 16)):
        print(chr(codepoint), end="")
    print("----")
        
def korean():
    for codepoint in range(int('BB00', 16), int('BBAF', 16)):
        print(chr(codepoint), end="")
    print("----")
        
def arabic():
    """
    http://www.alanwood.net/unicode/arabic.html
    U+0600 – U+06FF   (1536–1791)
    """
    print(" ".join([chr(codepoint) 
    for codepoint in range(int('0600', 16), 
                           int('06FF', 16))]))
    print("----")

def main():
    print("EMOJI:\n\n")
    emoji()
    print("HEBREW:\n\n")
    hebrew()
    print("GREEK & COPTIC:\n\n")        
    greek()
    print("KOREAN:\n\n")
    korean()
    print("ARABIC:\n\n")
    arabic()
    print()
    print("CHEROKEE:\n\n")
    cherokee()

html_top = """<!DOCTYPE html>
<html>
<head>
<title>Unicode Stuff</title>
</head>
<body>

<h1>Unicode Stuff</h1>
<p>"""
# Make an HTML sandwich!

html_bottom = """</p>
</body>
</html>"""

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
    
    # HTML sandwich
    print(html_top)
    main() # sandwich meat!
    print(html_bottom, end="")
    
    sys.stdout.flush()
    sys.stdout.close()
    sys.stdout = original
    
    # Now lets put in some line breaks, since HTML
    # pays no attention to newlines \n
    with open("unicode.html", "r", encoding='utf-8') as the_file:
        text = the_file.read().replace(":\n\n", "<br/>").replace("----","<br/><br/>")
        
    with open("unicode.html", "w", encoding='utf-8') as the_file:
        the_file.write(text)
        
    print("OK, open unicode.html in browser")
    
    
def the_help():
    options = "\n".join(sorted(menu_options.keys()))
    print("$ python -m unicode_fun name\n"
          "where name is:\n",
          options + "\n", sep="")

menu_options = {
        "arabic": arabic,
        "cherokee": cherokee,
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
    
    