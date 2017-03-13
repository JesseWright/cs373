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

def cycle_length_1 (n) :
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

def cycle_length_2 (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

def pre_gtz (f) :
    def g (n) :
        assert n > 0
        return f(n)
    return g

cycle_length_2 = pre_gtz(cycle_length_2)

def post_gtz (f) :
    def g (n) :
        v = f(n)
        assert v > 0
        return v
    return g

cycle_length_2 = post_gtz(cycle_length_2)

@pre_gtz
@post_gtz
def cycle_length_3 (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

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
    def setUp (self) :
        self.a = [
            cycle_length_1,
            cycle_length_2,
            cycle_length_3]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f( 1), 1)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f( 5), 6)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(10), 7)

    def test_4 (self) :
        x = range_iterator(2, 5)
        self.assertEqual(list(x), [2, 3, 4])
        self.assertEqual(list(x), [])

    def test_5 (self) :
        x = range_iterable(2, 5)
        self.assertEqual(list(x), [2, 3, 4])
        self.assertEqual(list(x), [2, 3, 4])

    def test_6 (self) :
        x = map(lambda v : v ** 2, (2, 3, 4))
        self.assertEqual(list(x), [4, 9, 16])
        self.assertEqual(list(x), [])

    def test_7 (self) :
        x = map_iterable(lambda v : v ** 2, (2, 3, 4))
        self.assertEqual(list(x), [4, 9, 16])
        self.assertEqual(list(x), [4, 9, 16])

if __name__ == "__main__" :
    main()
