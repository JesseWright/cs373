#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------
# ThetaJoin.py
# ------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

from typing import Callable, Dict, Iterable, Iterator

def theta_join_yield (
        r: Iterable[Dict[str, int]],
        s: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int], Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]                          :
    for u in r :
        for v in s :
            if f(u, v) :
                yield dict(u, **v)

def theta_join_generator (
        r: Iterable[Dict[str, int]],
        s: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int], Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]                          :
    return (dict(u, **v) for u in r for v in s if f(u, v))
