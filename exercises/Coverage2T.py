#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# ------------
# Coverage2.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

from Coverage2 import cycle_length

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(2), 2)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage-3.5 run --branch Coverage2T.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage-3.5 report -m
Name            Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------
Coverage2.py       10      1      4      1    86%   18, 15->18
Coverage2T.py       7      0      0      0   100%
-----------------------------------------------------------
TOTAL              17      1      4      1    90%
"""
