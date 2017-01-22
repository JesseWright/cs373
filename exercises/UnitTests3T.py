#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests3.py
# -------------

# https://docs.python.org/3.5/library/unittest.html
# https://docs.python.org/3.5/library/unittest.html#assert-methods

from unittest import main, TestCase

from UnitTests3 import cycle_length

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% UnitTests3T.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""
