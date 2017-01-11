#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------
# UnitTests1.py
# -------------

def cycle_length (n) :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c
