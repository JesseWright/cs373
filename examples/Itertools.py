#!/usr/bin/env python3

#pylint: disable = too-many-statements

# ------------
# Itertools.py
# ------------

from itertools import count, islice, slice, tee, _tee

print("Itertools.py")

a = [0, 1, 2, 3, 4]
assert a[2] == 2
try :
    assert a[5] == 0
    assert False
except IndexError as e :
    assert isinstance(e.args, tuple)
    assert len(e.args)     == 1
    assert e.args[0][-18:] == "index out of range"

a = [5, 4, 3, 2, 1]
assert a[-3] == 3
try :
    assert a[-6] == 0
    assert False
except IndexError as e :
    assert isinstance(e.args, tuple)
    assert len(e.args)     == 1
    assert e.args[0][-18:] == "index out of range"

a = [0, 1, 2, 3, 4]

assert a[ 1: 4] == [1, 2, 3]
assert a[-4:-1] == [1, 2, 3]
assert a[ 1:  ] == [1, 2, 3, 4]
assert a[  : 4] == [0, 1, 2, 3]
assert a[ 0: 5] == [0, 1, 2, 3, 4]
assert a[-9: 9] == [0, 1, 2, 3, 4]
assert a[  :  ] == [0, 1, 2, 3, 4]
assert a[ 4: 1] == []

assert a[ 1: 4: 2] == [1, 3]
assert a[ 1:  : 2] == [1, 3]
assert a[  : 4: 2] == [0, 2]
assert a[  :  : 2] == [0, 2, 4]

assert a[ 4: 1:-2] == [4, 2]
assert a[ 4:  :-2] == [4, 2, 0]
assert a[  : 1:-2] == [4, 2]
assert a[  :  :-2] == [4, 2, 0]

assert a[ :  :-1] == [4, 3, 2, 1, 0]

assert a[1:4] is not a[1:4]
assert a[1:4] ==     a[1:4]

s = slice(1, 4)
assert isinstance(s, slice)
assert a[s] == [1, 2, 3]
assert a[s] is not a[s]
assert a[s] ==     a[s]

p = islice(a, 4)
assert isinstance(p, islice)
assert     hasattr(p, "__next__")
assert not hasattr(p, "__getitem__")
assert list(p) == [0, 1, 2, 3]
assert list(p) == []

p = islice(a, 1, 4)
assert list(p) == [1, 2, 3]
assert list(p) == []

p = islice(a, 1, 4, 2)
assert list(p) == [1, 3]
assert list(p) == []

t = tee(a)
assert isinstance(t, tuple)
assert len(t) == 2
assert isinstance(t[0], _tee)
assert     hasattr(t[0], "__next__")
assert not hasattr(t[0], "__getitem__")
assert list(t[0]) == [0, 1, 2, 3, 4]
assert list(t[0]) == []
assert isinstance(t[1], _tee)
assert     hasattr(t[1], "__next__")
assert not hasattr(t[1], "__getitem__")
assert list(t[1]) == [0, 1, 2, 3, 4]
assert list(t[1]) == []

t = tee(a, 3)
assert list(t[0]) == [0, 1, 2, 3, 4]
assert list(t[0]) == []
assert list(t[1]) == [0, 1, 2, 3, 4]
assert list(t[1]) == []
assert list(t[2]) == [0, 1, 2, 3, 4]
assert list(t[2]) == []

x = count()                          # 0, 1, 2, ...
assert isinstance(x, count)
assert     hasattr(x, "__next__")
assert not hasattr(x, "__getitem__")
#assert x[0] == 0                    # TypeError: 'itertools.count' object is not indexable
for v in x :
    assert v >= 0
    if v == 10 :
        break
for v in x :
    assert v > 10
    if v == 20 :
        break

x = count(3, 2) # 3, 5, 7, 9, ...
for v in x :
    assert v >= 3
    if v > 10 :
        break

print("Done")
