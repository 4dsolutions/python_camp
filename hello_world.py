"""
What you see here at the top is called a 'docstring' or
'documentation string'.  These are typically multi-line
(but don't have to be) and so are demarcated with triple
quotes.

This is not the only place you'll find docstrings, in a
typical Python program.  However they're not to be thought
of as "multi-line comments".  Comments are for another
purpose.
"""

def main():
    """Here's another typical place for a docstring"""  # triple quotes OK

    your_name = input("Here there, what's your name? > ")

    print("Well hello there ", your_name, ".  And Hello World!", sep="") # no separator


if __name__ == "__main__":
    main()
