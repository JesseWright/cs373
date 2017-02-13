#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# Reduce.py
# ---------

def reduce_for_range (bf, a, v) :
    for i in range(len(a)) :
        w = a[i]
        v = bf(v, w)
    return v

def reduce_for (bf, a, v) :
    for w in a :
        v = bf(v, w)
    return v

def reduce_while (bf, a, v) :
    p = iter(a)
    try :
        while True :
            w = next(p)
            v = bf(v, w)
    except StopIteration :
        pass
    return v
