#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = unused-import

# --------
# Cache.py
# --------

from typing import Dict, FrozenSet, List, Set, Tuple

print("Cache.py")

i = 2
j = 2 + 0
assert i is j

i = 257
j = 257
assert i is j

i = 257            # cache: [-5, 256]
j = 257 + 0
assert i is not j
assert i ==     j
i -= 1
assert i is not j
assert i !=     j
j -= 1
assert i is j

i = -6             # cache: [-5, 256]
j = -6 + 0
assert i is not j
assert i ==     j
i += 1
assert i is not j
assert i !=     j
j += 1
assert i is j

f = 2.34
g = 2.34
assert f is g

f = 2.34
g = 2.34 + 0
assert f is not g
assert f ==     g

s = "abc"
t = "abc"
assert s is t

s = "abc"
t = "ab" + "c"
assert s is t

s = "abc"
p = "ab"
q = "c"
t = p + q
assert s is not t
assert s ==     t

a = []            # type: List
b = []            # type: List
assert a is not b
assert a ==     b

u = ()        # type: Tuple
v = ()        # type: Tuple
assert u is v

x = set()         # type: Set
y = set()         # type: Set
assert x is not y
assert x ==     y

w = frozenset() # type: FrozenSet
z = frozenset() # type: FrozenSet
assert w is z

d = {}            # type: Dict
e = {}            # type: Dict
assert d is not e
assert d ==     e

print("Done.")
