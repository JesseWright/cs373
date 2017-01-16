#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# Coverage1T.py
# -------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

from Coverage1 import cycle_length

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(1), 1)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage-3.5 run --branch Coverage1T.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage-3.5 report -m
Name            Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------
Coverage1.py       10      4      4      1    50%   15-19, 14->15
Coverage1T.py       7      0      0      0   100%
-----------------------------------------------------------
TOTAL              17      4      4      1    67%
"""
