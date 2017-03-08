#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# --------------
# Decorators2.py
# --------------

class cache_class :
    def __init__ (self, f) :
        self.f = f
        self.d = {}

    def __call__ (self, n) :
        if n not in self.d :
            self.d[n] = self.f(n)
        print(self.d)
        return self.d[n]

def cache_function (f) :
    d = {}
    def g (n) :
        if n not in d :
            d[n] = f(n)
        print(d)
        return d[n]
    return g
