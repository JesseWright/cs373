#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# ----------
# ReduceT.py
# ----------

# https://docs.python.org/3/library/functools.html

from functools import reduce
from operator  import add, sub
from unittest  import main, TestCase

from Reduce import        \
    reduce_for_range,     \
    reduce_for_enumerate, \
    reduce_for,           \
    reduce_while

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            reduce_for_range,
            reduce_for_enumerate,
            reduce_for,
            reduce_while,
            reduce]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(None, [],       2),  2)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(add, [2],       1),  3)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(add, [2, 3, 4], 1), 10)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(sub, [2, 3, 4], 1), -8)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% ReduceT
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
"""
