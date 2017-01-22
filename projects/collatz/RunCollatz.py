#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = missing-docstring

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)
