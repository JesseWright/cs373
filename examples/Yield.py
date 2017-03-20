#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# --------
# Yield.py
# --------

from typing import Iterator

print("Yield.py")

def f () -> Iterator[int] :
    yield 2
    yield 3
    yield 4

p = f()
assert p is iter(p)
n = next(p)
assert n == 2
n = next(p)
assert n == 3
n = next(p)
assert n == 4
try :
    n = next(p)
except StopIteration :
    pass

p = f()
assert list(p) == [2, 3, 4]
assert list(p) == []

p = f()
assert list(p) == [2, 3, 4]



def g () -> Iterator[int] :
    for v in [2, 3, 4] :
        yield v

p = g()
assert p is iter(p)
n = next(p)
assert n == 2
n = next(p)
assert n == 3
n = next(p)
assert n == 4
try :
    n = next(p)
except StopIteration :
    pass

p = g()
assert list(p) == [2, 3, 4]
assert list(p) == []

p = g()
assert list(p) == [2, 3, 4]

print("Done.")
