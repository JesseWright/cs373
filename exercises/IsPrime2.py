#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# IsPrime2.py
# -----------

from math import sqrt

def is_prime (n: int) -> int :
    assert n > 0
    if n == 2 :
        return True
    if (n == 1) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n)) + 1, 2) :
        if (n % i) == 0 :
            return False
    return True
