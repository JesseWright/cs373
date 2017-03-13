#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = unused-import

# ------------
# Variables.py
# ------------

from copy   import copy
from typing import Tuple

print("Variables.py")

i = 2
j = i
assert i is j
j += 1
assert i == 2
assert j == 3

a = [2, 3, 4]
b = a
assert a is b
b[1] += 1
assert a[1] == 4
assert a is b

u = (2, 3, 4)
v = u
assert u is v
#v[1] += 1    # TypeError: 'tuple' object does not support item assignment

a = [2, 3, 4]
b = copy(a)
assert a is not b
assert a ==     b
b[1] += 1
assert a[1] == 3
assert b[1] == 4

u = (2, 3, 4)
v = copy(u)
assert u is v

a = [2, 3, 4]
b = a
assert a is b
b += [5]
assert a == [2, 3, 4, 5]
assert a is b

a = [2, 3, 4]
b = a
assert a is b
b += (5,)
assert a == [2, 3, 4, 5]
assert a is b

a = [2, 3, 4]
b = a
assert a is b
b = b + [5]
assert a == [2, 3, 4]
assert b == [2, 3, 4, 5]

a = [2, 3, 4]
b = a
assert a is b
#b = b + (5,) # TypeError: can only concatenate list (not "tuple") to list

x = (2, 3, 4) # type: Tuple[int, ...]
y = x
assert x is y
y += (5,)
assert x == (2, 3, 4)
assert y == (2, 3, 4, 5)

u = (2, 3, 4)
v = u
assert u is v
#v += [5]     # TypeError: can only concatenate tuple (not "list") to tuple

x = (2, 3, 4)
y = x
assert x is y
y = y + (5,)
assert x == (2, 3, 4)
assert y == (2, 3, 4, 5)

u = (2, 3, 4)
v = u
assert u is v
#v = v + [5]  # TypeError: can only concatenate tuple (not "list") to tuple

print("Done.")
