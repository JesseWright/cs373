#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ----------------
# RangeIterator.py
# ----------------

from typing import Iterator

class Range_Iterator () :
    def __init__ (self, b: int, e: int) -> None :
        self.b = b
        self.e = e

    def __iter__ (self) -> "Range_Iterator" :
        return self

    def __next__ (self) -> int :
        if self.b == self.e :
            raise StopIteration()
        v = self.b
        self.b += 1
        return v

def range_iterator_yield (b: int, e: int) -> Iterator[int] :
    while b != e :
        yield b
        b += 1
