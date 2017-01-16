#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# ------------
# Coverage3.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

from Coverage3 import cycle_length

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(3), 8)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage-3.5 run --branch Coverage3T.py
.
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage-3.5 report -m
Name            Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------
Coverage3.py       10      0      4      0   100%
Coverage3T.py       7      0      0      0   100%
-----------------------------------------------------------
TOTAL              17      0      4      0   100%
"""
