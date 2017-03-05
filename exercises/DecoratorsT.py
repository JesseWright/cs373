#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# --------------
# DecoratorsT.py
# --------------

from unittest import main, TestCase

from Decorators import \
    make_iterable

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

assert cycle_length( 1) == 1
assert cycle_length( 5) == 6
assert cycle_length(10) == 7

def cycle_length_1 (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

def pre_gtz (f) :
    def g (n) :
        assert n > 0
        return f(n)
    return g

cycle_length_1 = pre_gtz(cycle_length_1)

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

def post_gtz (f) :
    def g (n) :
        v = f(n)
        assert v > 0
        return v
    return g

cycle_length_1 = post_gtz(cycle_length_1)

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

def range_iterator (b, e) :
    while b != e :
        yield b
        b += 1

@make_iterable
def range_iterable (b, e) :
    while b != e :
        yield b
        b += 1

map_iterable = make_iterable(map)

class MyUnitTests (TestCase) :
    def test_1 (self) :
        x = range_iterator(2, 5)
        self.assertEqual(list(x), [2, 3, 4])
        self.assertEqual(list(x), [])

    def test_2 (self) :
        x = range_iterable(2, 5)
        self.assertEqual(list(x), [2, 3, 4])
        self.assertEqual(list(x), [2, 3, 4])

    def test_3 (self) :
        x = map(lambda v : v ** 2, (2, 3, 4))
        self.assertEqual(list(x), [4, 9, 16])
        self.assertEqual(list(x), [])

    def test_4 (self) :
        x = map_iterable(lambda v : v ** 2, (2, 3, 4))
        self.assertEqual(list(x), [4, 9, 16])
        self.assertEqual(list(x), [4, 9, 16])

if __name__ == "__main__" :
    main()
