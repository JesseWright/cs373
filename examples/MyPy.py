#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = missing-docstring

# -------
# MyPy.py
# -------

# http://mypy-lang.org

from typing import Callable, Dict, Iterable, Iterator, List, Sequence, Set, Tuple

print("MyPy.py")

def f () -> None :
    pass

f()
# x = f() # mypy error: "f" does not return a value



def f_int (n: int) :
    assert n

f_int(2)
# f_int(2.3) # mypy error: Argument 1 to "g" has incompatible type "float"; expected "int"



def f_list (a: List[int]) :
    assert a

f_list([2, 3, 4])
# f_list([2, 3.4, 5]) # mypy error: List item 1 has incompatible type "float"
# f_list((2, 3, 4))   # mypy error: Argument 1 to "f_list" has incompatible type "Tuple[int, int, int]"; expected List[int]



def f_tuple (a: Tuple[int, str]) :
    assert a

f_tuple((2, "abc"))
# f_tuple(("abc", 2)) # mypy error: Argument 1 to "f_tuple" has incompatible type "Tuple[str, int]"; expected "Tuple[int, str]"
# f_tuple([2, "abc"]) # mypy error: Argument 1 to "f_tuple" has incompatible type List[object]; expected "Tuple[int, str]"



def f_sequence (a: Sequence[int]) :
    assert a

f_sequence([2, 3, 4])
f_sequence((2, 3, 4))
# f_sequence((2, 3.4, 5)) # mypy error: Argument 1 to "f_sequence" has incompatible type "Tuple[int, float, int]"; expected Sequence[int]
# f_sequence({2, 3, 4})   # mypy error: Argument 1 to "f_sequence" has incompatible type Set[int]; expected Sequence[int]



def f_set (a: Set[int]) :
    assert a

f_set({2, 3, 4})
# f_set({2, 3.4, 5}) # mypy error: Argument 2 to <set> has incompatible type "float"; expected "int"
# f_set([2, 3, 4])   # mypy error: Argument 1 to "f_set" has incompatible type List[int]; expected Set[int]



def f_dict (a: Dict[int, str]) :
    assert a

f_dict({2: "abc", 3: "def", 4: "ghi"})
# f_dict({2: "abc", "def": 3, 4: "ghi"}) # mypy error: List item 1 has incompatible type "Tuple[str, int]"



def f_iterable (a: Iterable[int]) :
    assert a

f_iterable([2, 3, 4])
f_iterable((2, 3, 4))
f_iterable({2, 3, 4})
f_iterable({2: "abc", 3: "def", 4: "ghi"})
f_iterable((map(lambda v : v**2, (2, 3, 4))))
# f_iterable(2)                               # mypy error: Argument 1 to "f_iterable" has incompatible type "int"; expected Iterable[int]



def f_iterator (a: Iterator[int]) :
    assert a

f_iterator((map(lambda v : v**2, (2, 3, 4))))
# f_iterator([2, 3, 4])                       # mypy error: Argument 1 to "f_iterator" has incompatible type List[int]; expected Iterator[int]



def f_callable (c: Callable[[int], int]) :
    assert c

def g (v: int) -> int :
    return v

def h (v: float) -> float :
    return v

f_callable(g)
# f_callable(h) # mypy: error: Argument 1 to "f_callable" has incompatible type Callable[[float], float]; expected Callable[[int], int]

print("Done.")
