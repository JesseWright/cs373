#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods
# pylint: disable = unused-import

# ------
# Map.py
# ------

from typing import Callable, Iterable, Sequence, TypeVar

T = TypeVar("T")

class Map_Iterator :
    def __init__ (self, uf: Callable[[T], T], a: Iterable[T]) -> None :
        self.uf = uf
        self.p  = iter(a)

    def __iter__ (self) :
        return self

    def __next__ (self) :
        return self.uf(next(self.p))

def map_for_range (uf: Callable[[T], T], a: Sequence[T]) :
    for i in range(len(a)) :
        yield uf(a[i])

def map_for_enumerate (uf: Callable[[T], T], a: Sequence[T]) :
    for i, _ in enumerate(a) :
        yield uf(a[i])

def map_for (uf: Callable[[T], T], a: Iterable[T]) :
    for v in a :
        yield uf(v)

def map_generator (uf: Callable[[T], T], a: Iterable[T]) :
    return (uf(v) for v in a)
