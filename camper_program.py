#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyCamp: a collaborative project

How to test this program:

.. code:: bash

    python ./camper_program.py -t

    python -m pip install pytest-cov
    python ./camper_program.py --coverage

TODO:

- [ ] TST: Get as close as possible || reasonable to 100% coverage

"""

import math
import unittest
from fractions import Fraction
from io import StringIO
from unittest.mock import patch


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


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator

    def test_squares(self):
        squares = self.calc.squares
        # pytest has good error messages for 'assert ...' expressions
        # unittest has good error messages for self.assertEqual exprs
        assert squares(2) == 4
        self.assertEqual(squares(2), 4)
        self.assertEqual(squares(0), 0)
        self.assertEqual(squares(1), 1)
        self.assertEqual(squares(-1), 1)

    def test_square_roots(self):
        square_roots = self.calc.square_roots
        self.assertEqual(square_roots(0), 0)
        self.assertEqual(square_roots(1), 1)
        self.assertEqual(square_roots(4), 2)
        with self.assertRaises(ValueError):
            self.assertEqual(square_roots(-1), 1j)

    def test_any_power(self):
        any_power = self.calc.any_power
        self.assertEqual(any_power(0, 0), 1)
        self.assertEqual(any_power(10, 0), 1)
        self.assertEqual(any_power(-1, 0), 1)
        self.assertEqual(any_power(-1, 2), 1)
        self.assertEqual(any_power(4, 0.5), 2)
        self.assertEqual(any_power(1.2, 2), 1.44)
        self.assertEqual(any_power(1j, 2), -1 + 0j)
        # with self.assertRaises(AssertionError):
        #     self.assertEqual(any_power(-1, 1/2), 0+1j)

    def test_evalFraction(self):
        evalf = self.calc.evalFraction
        self.assertEqual(evalf("0/1"), 0)
        self.assertEqual(evalf("1/1"), 1)
        self.assertEqual(evalf("1/2"), 1 / 2)
        self.assertEqual(evalf("2/3"), 2 / 3)
        with self.assertRaises(ZeroDivisionError):
            evalf("1/0")
        self.assertEqual(evalf("0"), "0")
        with self.assertRaises(TypeError):
            self.assertEqual(evalf(0), 0)

    def test_isFrac(self):
        isfrac = self.calc.isFrac
        self.assertTrue(isfrac("1/2"))
        self.assertTrue(isfrac("1/2/3"))  # TODO
        self.assertFalse(isfrac("0"))
        self.assertFalse(isfrac("0.1"))
        self.assertFalse(isfrac("1.0"))


class TestCalculatorREPL(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatorREPL()
        self.stdout = patch("sys.stdout", new_callable=StringIO())

    def test_init(self):
        repl = CalculatorREPL()
        self.assertTrue(repl)
        self.assertEqual(repl.calc, Calculator)

        repl = CalculatorREPL(calculator=dict)
        self.assertTrue(repl)
        self.assertEqual(repl.calc, dict)

    @patch("sys.stdin", StringIO("1"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_squares_1(self, stdout):
        self.calc.squares()
        stdout.seek(0)
        self.assertEqual(next(stdout), "Choose a number 1 through 100.\n")
        self.assertEqual(next(stdout), "The square of 1 is 1\n")

    @patch("sys.stdin", StringIO("101"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_squares_101(self, stdout):
        self.calc.squares()
        stdout.seek(0)
        self.assertEqual(next(stdout), "Choose a number 1 through 100.\n")
        self.assertEqual(next(stdout), "The square of 101 is 10201\n")

    @patch("sys.stdin", StringIO("0"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_square_roots_1(self, stdout):
        self.calc.square_roots()
        stdout.seek(0)
        self.assertEqual(next(stdout), "Choose a number 1 through 100.\n")
        self.assertEqual(next(stdout), "The square root of 0 is 0.0\n")

    @patch("sys.stdin", StringIO("10201"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_square_roots_10201(self, stdout):
        self.calc.square_roots()
        stdout.seek(0)
        self.assertEqual(next(stdout), "Choose a number 1 through 100.\n")
        self.assertEqual(next(stdout), "The square root of 10201 is 101.0\n")

    @patch("sys.stdin", StringIO("-1"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_square_roots_negative1(self, stdout):
        with self.assertRaises(ValueError):
            self.calc.square_roots()

    @patch("sys.stdin", StringIO("10\n0"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_any_power_10_0(self, stdout):
        self.calc.any_power()
        stdout.seek(0)
        self.assertEqual(
            next(stdout), "Choose a number > Raise to what power? > 1.0\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_isFrac(self, stdout):
        output = self.calc.isFrac("1/1")
        self.assertTrue(output)
        stdout.seek(0)
        self.assertEqual(next(stdout), "1/1 is a fraction\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_isFrac(self, stdout):
        output = self.calc.isFrac("0")
        self.assertFalse(output)
        stdout.seek(0)
        self.assertEqual(next(stdout), "0 is not a fraction\n")

    @patch("sys.stdin", StringIO("0"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_decimal__not_1(self, stdout):
        self.calc.get_decimal()
        stdout.seek(0)
        next(stdout)  # "We are here"
        self.assertEqual(
            next(stdout),
            "Would you like to find the decimal value of a fraction "
            'type "1" >>> ',
        )
        with self.assertRaises(StopIteration):
            next(stdout)

    @patch("sys.stdin", StringIO("1\n1/2"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_decimal__1_2(self, stdout):
        self.calc.get_decimal()
        stdout.seek(0)
        next(stdout)  # "We are here"
        self.assertEqual(
            next(stdout),
            "Would you like to find the decimal value of a fraction "
            'type "1" >>> Type a fraction like _/_ \n',
        )
        self.assertEqual(
            next(stdout), "What is your fraction >>> 1/2 is a fraction\n"
        )

    def test_get_menu_options(self):
        output = self.calc.get_menu_options()
        self.assertIsInstance(output, dict)
        self.assertIn("0", output)
        self.assertEqual(output["0"], ["Exit", None])

    @patch("sys.stdin", StringIO("0"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_loop_0(self, stdout):
        output = self.calc.run_loop()
        self.assertEqual(output, None)
        stdout.seek(0)
        lines = list(stdout)
        self.assertRegex(lines[-2], "Pick one please\n$")
        self.assertRegex(lines[-1], ">>> $")
        # raise Exception(list(enumerate(lines)))

    @patch("sys.stdin", StringIO("1\n1"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_loop_0(self, stdout):
        output = self.calc.run_loop()
        menulen = len(self.calc.get_menu_options()) + 2
        self.assertEqual(output, None)
        stdout.seek(0)
        lines = list(stdout)[menulen:]
        self.assertRegex(lines[0], "Choose a number 1 through 100.\n$")
        self.assertEqual(lines[1], "The square of 1 is 1\n")
        self.assertEqual(lines[-1], "Received EOF (Ctrl-D). Exiting.\n")
        # raise Exception(list(enumerate(lines)))

    @patch("sys.stdin", StringIO("-1"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_loop_invalid_option(self, stdout):
        output = self.calc.run_loop()
        menulen = len(self.calc.get_menu_options()) + 2
        self.assertEqual(output, None)
        stdout.seek(0)
        lines = list(stdout)[menulen:]
        self.assertRegex(lines[0], ">>> Please pick one of (.*)\n$")
        self.assertEqual(lines[-1], "Received EOF (Ctrl-D). Exiting.\n")


if __name__ == "__main__":
    import os
    import sys
    import subprocess

    if "-t" in sys.argv[1:]:
        sys.argv.remove("-t")
        sys.argv.append("-v")
        unittest.main()
    elif "--pytest" in sys.argv[1:] or "--coverage" in sys.argv[1:]:
        # You can install pytest and pytest-cov and coverage.py by running:
        #   python -m pip install pytest-cov
        cmd = ["pytest", "-v"]
        try:
            sys.argv.remove("--pytest")
        except ValueError:
            pass
        try:
            sys.argv.remove("--coverage")
            modname = os.path.splitext(os.path.basename(__file__))[0]
            cmd += [f"--cov={modname}", "--cov-report=term-missing"]
        except ValueError:
            pass
        cmd = cmd + [__file__] + sys.argv[1:]
        print(f"+ {' '.join(cmd)}")
        subprocess.call(cmd)
    else:
        CalculatorREPL().run_loop()
