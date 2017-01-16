#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests1.py
# -------------

# https://docs.python.org/3.5/library/unittest.html
# https://docs.python.org/3.5/library/unittest.html#assert-methods

from unittest import main, TestCase

from UnitTests1 import cycle_length

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
% UnitTests1T.py
FFF
======================================================================
FAIL: test_1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1T.py", line 21, in test_1
    self.assertEqual(cycle_length( 1), 1)
  File "/v/filer4b/v41q001/downing/public_html/exercises/python/UnitTests1.py", line 20, in cycle_length
    assert c > 0
AssertionError

======================================================================
FAIL: test_2 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1T.py", line 24, in test_2
    self.assertEqual(cycle_length( 5), 6)
AssertionError: 5 != 6

======================================================================
FAIL: test_3 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1T.py", line 27, in test_3
    self.assertEqual(cycle_length(10), 7)
AssertionError: 6 != 7

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)
"""
