#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# Copy.py
# -------

from copy import copy, deepcopy

print("Copy.py")

a = [2, 3, 4]

assert a[1]   == 3
assert a[-1]  == 4
assert a[1:2] == [3]
assert a[1:3] == [3, 4]
assert a[0:3] == [2, 3, 4]
assert a[:]   == [2, 3, 4]

b = [1, a, 5]

c = b[:]
assert b    is not c
assert b    ==     c
assert b[1] is     c[1]

c = copy(b)
assert b    is not c
assert b    ==     c
assert b[1] is     c[1]

c = deepcopy(b)
assert b    is not c
assert b    ==     c
assert b[1] is not c[1]
assert b[1] ==     c[1]

u = (2, 3, 4)

assert u[1:2] == (3,)
assert u[1:3] == (3, 4)
assert u[0:3] == (2, 3, 4)
assert u[:]   == (2, 3, 4)

v = (1, u, 5)

w = v[:]
assert v is w

w = copy(v)
assert v is w

w = deepcopy(v)
assert v is w

print("Done.")
