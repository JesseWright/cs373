#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests2.py
# -------------

# https://docs.python.org/3.5/library/unittest.html
# https://docs.python.org/3.5/library/unittest.html#assert-methods

from unittest import main, TestCase

from UnitTests2 import cycle_length

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 5), 5)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% UnitTests2T.py
.F.
======================================================================
FAIL: test_2 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests2T.py", line 34, in test_2
    self.assertEqual(cycle_length( 5), 5)
AssertionError: 6 != 5

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
"""
