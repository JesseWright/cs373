#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# Reduce.py
# ---------

from typing import Callable, Iterable, Sequence, TypeVar

T = TypeVar("T")

def reduce_for_range (bf: Callable[[T, T], T], a: Sequence[T], v: T) :
    for i in range(len(a)) :
        w = a[i]
        v = bf(v, w)
    return v

def reduce_for_enumerate (bf: Callable[[T, T], T], a: Sequence[T], v: T) :
    for i, _ in enumerate(a) :
        w = a[i]
        v = bf(v, w)
    return v

def reduce_for (bf: Callable[[T, T], T], a: Iterable[T], v: T) :
    for w in a :
        v = bf(v, w)
    return v

def reduce_while (bf: Callable[[T, T], T], a: Iterable[T], v: T) :
    p = iter(a)
    try :
        while True :
            w = next(p)
            v = bf(v, w)
    except StopIteration :
        pass
    return v
