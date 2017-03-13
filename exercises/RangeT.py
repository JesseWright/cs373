#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# RangeT.py
# ---------

from unittest import main, TestCase

from Range import \
    Range_1,      \
    Range_2

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            Range_1,
            Range_2,
            range]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 2)
                p = iter(x)
                self.assertIsNot(p, x)
                self.assertIs(iter(p), p)
                self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 3)
                p = iter(x)
                self.assertIsNot(p, x)
                self.assertIs(iter(p), p)
                self.assertEqual(next(p), 2)
                self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 4)
                p = iter(x)
                self.assertIsNot(p, x)
                self.assertIs(iter(p), p)
                self.assertEqual(next(p), 2)
                self.assertEqual(next(p), 3)
                self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 5)
                self.assertEqual(list(x), [2, 3, 4])
                self.assertEqual(list(x), [2, 3, 4])

if __name__ == "__main__" :
    main()
