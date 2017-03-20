#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# FactorialT.py
# -------------

from math     import factorial
from timeit   import timeit
from unittest import main, TestCase

from Factorial import         \
    factorial_recursion,      \
    factorial_tail_recursion, \
    factorial_while,          \
    factorial_range_for,      \
    factorial_range_iterator, \
    factorial_range_reduce

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            factorial_recursion,
            factorial_tail_recursion,
            factorial_while,
            factorial_range_for,
            factorial_range_iterator,
            factorial_range_reduce,
            factorial]

    def test_0 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(0), 1)

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(1), 1)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(2), 2)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(3), 6)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(4), 24)

    def test_5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(5), 120)

    def test_6 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                t = timeit(
                    f.__name__ + "(100)",
                    "from __main__ import " + f.__name__,
                    number = 1000)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% FactorialT.py
......
factorial_recursion
144.77 milliseconds

factorial_tail_recursion
149.86 milliseconds

factorial_while
70.56 milliseconds

factorial_range_for
48.67 milliseconds

factorial_range_iterator
67.27 milliseconds

factorial_range_reduce
11.52 milliseconds

factorial
1.07 milliseconds
.
----------------------------------------------------------------------
Ran 7 tests in 0.087s

OK
"""
