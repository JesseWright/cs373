#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = unused-import

# -------------
# Indexables.py
# -------------

from typing import List

print("Iteration.py")

a = [2, 3, 4]                     # type: List
assert isinstance(a, list)
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
s = 0
for v in a :
    s += v
assert s == 9

a = [2, 3, 4]
for v in a :
    v += 1            # ?
assert a == [2, 3, 4]

a = [[2], [3], [4]]
for v in a :
    v += (5,)                        # ?
assert a == [[2, 5], [3, 5], [4, 5]]

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)                  # ?
assert a == [(2,), (3,), (4,)]

a = ["abc", "def", "ghi"]
for v in a :
    v += "x"                      # ?
assert a == ["abc", "def", "ghi"]

a = [[2, "abc"], (3, "def"), [4, "ghi"]]
s = 0
for u, _ in a :
    s += u
assert s == 9

x = {2, 3, 4}                     # set
assert isinstance(x, set)
assert not hasattr(x, "__next__")
assert     hasattr(x, "__iter__")
s = 0
for v in x :                      # order not guaranteed
    s += v
assert s == 9

d = {2: "abc", 3: "def", 4: "ghi"} # dict
assert isinstance(d, dict)
assert not hasattr(d, "__next__")
assert     hasattr(d, "__iter__")
s = 0
for k in d :                          # order not guaranteed
    s += k
assert s == 9

d = {2: "abc", 3: "def"}
k = d.keys()
l = d.keys()
assert k is not l
assert str(type(k)) == "<class 'dict_keys'>"
assert set(k) == {2, 3}
d[4] = "ghi"
assert set(k) == {2, 3, 4}
assert set(k) == {2, 3, 4}

d = {2: "abc", 3: "def", 4: "ghi"}
v = d.values()
assert str(type(v)) == "<class 'dict_values'>"
assert set(v) == {"abc", "def", "ghi"}

d = {2: "abc", 3: "def", 4: "ghi"}
kv = d.items()
assert str(type(kv)) == "<class 'dict_items'>"
assert set(kv) == {(2, "abc"), (3, "def"), (4, "ghi")}

r = range(10)
assert isinstance(r, range)
assert not hasattr(r, "__next__")
assert     hasattr(r, "__iter__")
assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(2, 10)
assert list(r) == [2, 3, 4, 5, 6, 7, 8, 9]

r = range(2, 10, 2)
assert list(r) == [2, 4, 6, 8]

r = range(10, 2, -2)
assert list(r) == [10, 8, 6, 4]

r = range(10)
assert hasattr(r, "__getitem__")
assert r[0] == 0
assert r[9] == 9
try :
    assert r[10] == 10 # error: out of range
    assert False
except IndexError :
    pass
#r[0] = 2              # TypeError: 'range' object does not support item assignment
s = 0
for v in r :
    s += v
assert s == 45
s = 0
for v in r :
    s += v
assert s == 45

r = range(15)
s = 0
for v in r :
    if v == 10 :
        break
    s += v
else :           # else clause in a for loop
    assert False # executes when the loop terminates normally
assert s == 45

print("Done.")
