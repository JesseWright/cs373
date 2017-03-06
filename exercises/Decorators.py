#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------------
# Decorators.py
# ---- ---------

def make_iterable (c) :
    class iterable :
        def __init__ (self, *t, **d) :
            self.t = t
            self.d = d

        def __iter__ (self) :
            return c(*self.t, **self.d)

    return iterable
