#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# --------
# Range.py
# --------

from typing import Iterator

class Range_1 :
    class iterator () :
        def __init__ (self, b: int, e: int) -> None :
            self.b = b
            self.e = e

        def __iter__ (self) -> "Range_1.iterator" :
            return self

        def __next__ (self) -> int :
            if self.b == self.e :
                raise StopIteration()
            v = self.b
            self.b += 1
            return v

    def __init__ (self, b: int, e: int) -> None :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return Range_1.iterator(self.b, self.e)

class Range_2 :
    def __init__ (self, b: int, e: int) -> None :
        self.b = b
        self.e = e

    def __iter__ (self) -> Iterator[int] :
        b = self.b
        while b != self.e :
            yield b
            b += 1
