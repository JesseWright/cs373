#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = function-redefined
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-name-in-module
# pylint: disable = redefined-variable-type
# pylint: disable = too-few-public-methods

# ------------
# Callables.py
# ------------

from functools import reduce
from types     import FunctionType, MethodType

print("Callables.py")

def my_function (i, j) :
    return i + j

f = my_function

assert isinstance(f, FunctionType)
assert hasattr(f, "__call__")
assert f(2, 3)                 == 5
assert reduce(f, [2, 3, 4], 0) == 9



def my_closure (j) :
    return lambda i : i + j

f = my_closure(2)

assert isinstance(f, FunctionType)
assert hasattr(f, "__call__")
assert f(3)                    == 5
assert list(map(f, [2, 3, 4])) == [4, 5, 6]



class A (object) :
    def __init__ (self, j) :
        self.j = j

    def my_method (self, i) :
        return i + self.j

x = A(2)
assert isinstance(x, A)

f = x.my_method

assert isinstance(f, MethodType)
assert hasattr(f, "__call__")
assert f(3)                    == 5
assert list(map(f, [2, 3, 4])) == [4, 5, 6]

f = A.my_method

assert isinstance(f, FunctionType)
assert hasattr(f, "__call__")
assert f(x, 3) == 5



class A :
    def __init__ (self, j) :
        self.j = j

    def __call__ (self, i) :
        return i + self.j

f = A(2)
assert isinstance(f, A)

assert hasattr(f, "__call__")
assert f(3)                    == 5
assert list(map(f, [2, 3, 4])) == [4, 5, 6]

print("Done.")
