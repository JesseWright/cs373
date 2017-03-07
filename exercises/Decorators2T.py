#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------
# Decorators2T.py
# ---------------

from unittest import main, TestCase

from Decorators2 import \
    cache_class,        \
    cache_function

@cache_class
def cycle_length_1 (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

@cache_function
def cycle_length_2 (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

@cache_class
def cycle_length_3 (n) :
    assert n > 0
    if n == 1 :
        c = 1
    elif (n % 2) == 0 :
        c = 1 + cycle_length_3(n // 2)
    else :
        c = 1 + cycle_length_3((3 * n) + 1)
    assert c > 0
    return c

@cache_function
def cycle_length_4 (n) :
    assert n > 0
    if n == 1 :
        c = 1
    elif (n % 2) == 0 :
        c = 1 + cycle_length_4(n // 2)
    else :
        c = 1 + cycle_length_4((3 * n) + 1)
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length_4(10), 7)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
Decorators2T.py
{10: 7}
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



Decorators2T.py
{10: 7}
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



Decorators2T.py
{1: 1}
{1: 1, 2: 2}
{1: 1, 2: 2, 4: 3}
{8: 4, 1: 1, 2: 2, 4: 3}
{8: 4, 1: 1, 2: 2, 4: 3, 16: 5}
{16: 5, 1: 1, 2: 2, 4: 3, 5: 6, 8: 4}
{16: 5, 1: 1, 2: 2, 4: 3, 5: 6, 8: 4, 10: 7}
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



Decorators2T.py
{1: 1}
{1: 1, 2: 2}
{1: 1, 2: 2, 4: 3}
{8: 4, 1: 1, 2: 2, 4: 3}
{8: 4, 1: 1, 2: 2, 4: 3, 16: 5}
{16: 5, 1: 1, 2: 2, 4: 3, 5: 6, 8: 4}
{16: 5, 1: 1, 2: 2, 4: 3, 5: 6, 8: 4, 10: 7}
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
