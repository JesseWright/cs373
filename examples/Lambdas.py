#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Lambdas.py
# ----------

from typing import Callable

print("Lambdas.py")

def f () -> Callable[[int], int] :
    return lambda n : n ** 2

def g (p: int) -> Callable[[int], int] :
    return lambda n : n ** p

m = map(f(), [2, 3, 4])
assert list(m) == [4, 9, 16]
assert list(m) == []

m = map(g(2), [2, 3, 4])
assert list(m) == [4, 9, 16]
assert list(m) == []

print("Done.")
