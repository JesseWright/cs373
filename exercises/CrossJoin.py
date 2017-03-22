#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------
# CrossJoin.py
# ------------

# http://en.wikipedia.org/wiki/Cartesian_product

from typing import Dict, Iterable, Iterator

def cross_join_yield (
        r: Iterable[Dict[str, int]],
        s: Iterable[Dict[str, int]]) \
        -> Iterator[Dict[str, int]]  :
    for u in r :
        for v in s :
            yield dict(u, **v)

def cross_join_generator (
        r: Iterable[Dict[str, int]],
        s: Iterable[Dict[str, int]]) \
        -> Iterator[Dict[str, int]]  :
    return (dict(u, **v) for u in r for v in s)
