# -----------
# Wed,  1 Feb
# -----------

"""
str
    indexable
    ordered
    immutable
    constructor takes an iterable of strings

list
    indexable
    ordered
    mutable
    constructor takes an iterable of anything

tuple
    indexable
    ordered
    immutable
    constructor takes an iterable of anything

set
    iterable, not indexable
    unordered
    mutable
    constructor takes an iterable of hashables
"""

i = 2 # ok,     i is an l-value
2 = 3 # not ok, 2 is an r-value

int k = (i += j);
