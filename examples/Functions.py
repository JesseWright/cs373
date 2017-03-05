#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ------------
# Functions.py
# ------------

print("Functions.py")

a = [2, 3, 4]
r = reversed(a)
assert str(type(r)) == "<class 'list_reverseiterator'>"
assert list(r) == [4, 3, 2]
assert list(r) == []

a = ["abc", "def", "ghi"]
e = enumerate(a)
assert str(type(e)) == "<class 'enumerate'>"
assert list(e) == [(0, "abc"), (1, "def"), (2, "ghi")]
assert list(e) == []

a = ["abc", "def", "ghi"]
e = enumerate(a, 2)
assert list(e) == [(2, "abc"), (3, "def"), (4, "ghi")]
assert list(e) == []

a = ["c", "B", "a"]
s = sorted(a)
assert a == ["c", "B", "a"]
assert s == ["B", "a", "c"]

a = ["c", "B", "a"]
s = sorted(a, key=str.lower)
assert a == ["c", "B", "a"]
assert s == ["a", "B", "c"]

a = ["a", "B", "c"]
s = sorted(a, reverse=True)
assert a == ["a", "B", "c"]
assert s == ["c", "a", "B"]

a = ["a", "B", "c"]
s = sorted(a, key=str.lower, reverse=True)
assert a == ["a", "B", "c"]
assert s == ["c", "B", "a"]

class A :
    pass

assert all([])
assert all([
    A(),
    True,
    2,
    3.45,
    "abc",
    [2, 3, 4],
    (2, 3, 4),
    {2, 3, 4},
    {2 : "abc", 3 : "def", 4 : "ghi"}])

class B :
    def __bool__ (self) :
        return False

assert not any([])
assert not any([B(), False, 0, 0.0,  "", [], (), set(), {}])

print("Done.")
