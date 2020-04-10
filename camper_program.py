#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyCamp: a collaborative project

TODO:

- [ ] Add tests
"""

import math
from fractions import Fraction


class Calculator:

    # These methods don't need any local state stored on the class
    # so we mark them with the @staticmethod decorator
    # and omit the 'self' parameter that instance methods would receive:

    @staticmethod
    def squares(num):
        return num ** 2

    @staticmethod
    def square_roots(num):
        return math.sqrt(num)

    @staticmethod
    def any_power(num, exp):
        return pow(num, exp)

    @staticmethod
    def evalFraction(fracstr):
        if "/" in fracstr:
            spl = fracstr.split("/")
            return float(spl[0]) / float(spl[1])
        else:
            return fracstr

    @staticmethod
    def isFrac(fracstr):
        if "/" in fracstr:
            return True
        else:
            return False


class CalculatorREPL:
    def __init__(self, calculator=None):
        # Parametrize so that we can specify
        # a different calculator implementation:
        self.calc = Calculator if calculator is None else calculator

    def squares(self):
        print("Choose a number 1 through 100.")
        number = int(input())
        square = self.calc.squares(number)
        print("The square of", number, "is", square)

    def square_roots(self):
        print("Choose a number 1 through 100.")
        num = int(input())
        root = self.calc.square_roots(num)
        print("The square root of", num, "is", root)

    def any_power(self):
        num = float(input("Choose a number > "))
        exp = input("Raise to what power? > ")
        if "/" in exp:
            exp = float(Fraction(exp))
        else:
            exp = float(exp)
        print(self.calc.any_power(num, exp))

    def isFrac(self, f):
        isfrac = self.calc.isFrac(f)
        if isfrac:
            print(f + " is a fraction")
        else:
            print(f + " is not a fraction")
        return isfrac

    def get_decimal(self):
        print("We are here")
        The_answer = input(
            'Would you like to find the decimal value of a fraction type "1" >>> '
        )
        if The_answer != "1":
            return
        print("Type a fraction like _/_ ")
        validfrac = False
        while not validfrac:
            fraction = input("What is your fraction >>> ")
            validfrac = self.isFrac(fraction)
        print("Your fraction = ", self.calc.evalFraction(fraction))

    def get_menu_options(self):
        # this could come in handy
        return {
            "1": ["Squares", self.squares],
            "2": ["Square roots", self.square_roots],
            "3": ["Raise to any power", self.any_power],
            "4": ["Get decimal", self.get_decimal],
            "0": ["Exit", None],
        }

    def run_loop(self):
        menu_options = self.get_menu_options()
        looping = True
        while looping:
            for n, (menustr, _) in menu_options.items():
                print(f"            {n}. {menustr}")
            print("\n            Pick one please")

            try:
                do_it = input("    >>> ")
                # print("You picked", do_it)

                if do_it not in menu_options:
                    print(
                        "Please pick one of "
                        f"{{ {' '.join(menu_options.keys())} }}"
                    )
                    continue

                option_chosen = menu_options.get(do_it)
                if option_chosen is None:
                    print(f"{do_it} is not a recognized option")
                    continue

                menustr, calculator_function = option_chosen
                if calculator_function is None:
                    looping = False
                else:
                    try:
                        calculator_function()
                    except ValueError as e:
                        print("Error: %r" % e)
                        continue
                    except KeyboardInterrupt:
                        print("\nReceived Ctrl-C. Returning to menu.")
                        continue
                    except EOFError:
                        print("\nReceived EOF (Ctrl-D). Returning to menu.")
                        continue
            except KeyboardInterrupt:
                print("\nReceived Ctrl-C. Exiting.")
                return
            except EOFError:
                print("\nReceived EOF (Ctrl-D). Exiting.")
                return


if __name__ == "__main__":
    CalculatorREPL().run_loop()
