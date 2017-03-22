#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# Select.py
# ---------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

from typing import Callable, Dict, Iterable, Iterator

def select_yield (
        r: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]          :
    for d in r :
        if f(d) :
            yield d

def select_generator (
        r: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]          :
    return (d for d in r if f(d))

def select_filter (
        r: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]          :
    return filter(f, r)
