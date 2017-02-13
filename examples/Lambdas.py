#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Lambdas.py
# ----------

from operator import add

print("Lambdas.py")

def f (bf, x, y, z) :
    return bf(x, y) * bf(y, z)

def g (uf, x, y, z) :
    return uf(x) * uf(y) * uf(z)

def h (x) :
    return lambda y : x + y

def my_add (x, y) :
    return x + y

assert f(my_add,              2, 3, 4) == 35 # (2+3) * (3+4)
assert f(   add,              2, 3, 4) == 35 # (2+3) * (3+4)
assert f(lambda x, y : x + y, 2, 3, 4) == 35 # (2+3) * (3+4)

assert g(h(2), 3, 4, 5) == 210 # (2+3) * (2+4) * (2+5)

print("Done.")
