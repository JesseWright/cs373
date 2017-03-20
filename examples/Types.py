#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = function-redefined
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = redefined-outer-name
# pylint: disable = redefined-variable-type
# pylint: disable = too-few-public-methods
# pylint: disable = unused-import

# --------
# Types.py
# --------

from typing import Dict, FrozenSet, List, Set, Tuple

from types import FunctionType

print("Types.py")

b = True
b = False
b = bool()
b = bool(True)
assert isinstance(b,    bool)
assert isinstance(bool, type)
assert issubclass(bool, bool)
assert issubclass(bool, object)

i = int()
i = int(2)
i = 2
assert isinstance(i,   int)
assert isinstance(int, type)
assert issubclass(int, int)
assert issubclass(int, object)

assert     issubclass(bool, int)
assert not issubclass(int,  bool)

f = float()
f = float(2.3)
f = 2.3
assert isinstance(f,     float)
assert isinstance(float, type)
assert issubclass(float, float)
assert issubclass(float, object)

c = complex()
c = complex(2, 3)
c = 2 + 3j
assert isinstance(c,       complex)
assert isinstance(complex, type)
assert issubclass(complex, complex)
assert issubclass(complex, object)

s = str()
s = str(["a", "b", "c"])
s = 'abc'
s = "abc"
assert isinstance(s,   str)
assert isinstance(str, type)
assert issubclass(str, str)
assert issubclass(str, object)

a = list()                      # type: List
a = list((2, "abc", 3.45))
a = [2, "abc", 3.45]
assert isinstance(a,    list)
assert isinstance(list, type)
assert issubclass(list, list)
assert issubclass(list, object)

u = tuple()                      # type: Tuple
u = tuple([2, "abc", 3.45])
u = (2, "abc", 3.45)
assert isinstance(u,     tuple)
assert isinstance(tuple, type)
assert issubclass(tuple, tuple)
assert issubclass(tuple, object)

x = set()                       # type: Set
x = set([2, "abc", 3.45])
x = {2, "abc", 3.45}
assert isinstance(x,   set)
assert isinstance(set, type)
assert issubclass(set, set)
assert issubclass(set, object)

y = frozenset()                         # type: FrozenSet
y = frozenset((2, "abc", 3.45))
assert isinstance(y,         frozenset)
assert isinstance(frozenset, type)
assert issubclass(frozenset, frozenset)
assert issubclass(frozenset, object)

d = dict()                                       # type: Dict
d = dict([(2, "def"), (3.45, 3), ("abc", 6.78)])
d = {2: "def", 3.45: 3, "abc": 6.78}
assert isinstance(d,    dict)
assert isinstance(dict, type)
assert issubclass(dict, dict)
assert issubclass(dict, object)

def g (v) :
    return v + 1
assert isinstance(g,            FunctionType)
assert isinstance(FunctionType, type)
assert issubclass(FunctionType, FunctionType)
assert issubclass(FunctionType, object)

h = lambda v : v + 1
assert isinstance(h,            FunctionType)
assert isinstance(FunctionType, type)
assert issubclass(FunctionType, FunctionType)
assert issubclass(FunctionType, object)

class A :
    def __init__ (self, i, f) :
        pass

z = A(2, 3.45)
assert isinstance(z, A)
assert isinstance(A, type)
assert issubclass(A, A)
assert issubclass(A, object)

assert isinstance(type, type)
assert issubclass(type, type)
assert issubclass(type, object)

print("Done.")
