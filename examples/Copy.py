#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = redefined-variable-type

# -------
# Copy.py
# -------

from copy import copy, deepcopy

print("Copy.py")

x = [2, 3, 4]

assert x[1]   == 3
assert x[-1]  == 4
assert x[1:2] == [3]
assert x[1:3] == [3, 4]
assert x[0:3] == [2, 3, 4]
assert x[:]   == [2, 3, 4]

y = [1, x, 5]

z = y[:]
assert y    is not z
assert y    ==     z
assert y[1] is     z[1]

z = copy(y)
assert y    is not z
assert y    ==     z
assert y[1] is     z[1]

z = deepcopy(y)
assert y    is not z
assert y    ==     z
assert y[1] is not z[1]
assert y[1] ==     z[1]

x = (2, 3, 4)

assert x[1:2] == (3,)
assert x[1:3] == (3, 4)
assert x[0:3] == (2, 3, 4)
assert x[:]   == (2, 3, 4)

y = (1, x, 5)

z = y[:]
assert y is z

z = copy(y)
assert y is z

z = deepcopy(y)
assert y is z

print("Done.")
