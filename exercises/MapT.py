#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------
# MapT.py
# -------

# https://docs.python.org/3/library/functions.html#map

from timeit   import timeit
from unittest import main, TestCase

from Map import        \
    Map_Iterator,      \
    map_for_range,     \
    map_for_enumerate, \
    map_for,           \
    map_generator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            Map_Iterator,
            map_for_range,
            map_for_enumerate,
            map_for,
            map_generator,
            map]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(None, ())
                self.assertEqual(list(x), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(lambda v : v ** 2, (2,))
                self.assertEqual(list(x), [4])
                self.assertEqual(list(x), [])

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(lambda v : v ** 3, [2, 3])
                self.assertEqual(list(x), [8, 27])
                self.assertEqual(list(x), [])

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(lambda v : v ** 2, (2, 3, 4))
                self.assertEqual(list(x), [4, 9, 16])
                self.assertEqual(list(x), [])

    def test_5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                if f.__name__ == "map" :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda v : v ** 2, 10000 * [5]))",
                        "",
                        number = 100)
                else :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda v : v ** 2, 10000 * [5]))",
                        "from __main__ import " + f.__name__,
                        number = 100)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% MapT
....
Map_Iterator
783.32 milliseconds

map_range_for
466.25 milliseconds

map_for
414.43 milliseconds

map_generator
413.00 milliseconds

map
366.00 milliseconds
.
----------------------------------------------------------------------
Ran 5 tests in 2.433s

OK
"""
