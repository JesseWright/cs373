# -----------
# Fri,  3 Feb
# -----------

"""
str
    indexable
    ordered
    immutable
    hashable
    constructor takes an iterable of strings

list
    indexable
    ordered
    mutable
    not hashable
    constructor takes an iterable of anything

tuple
    indexable
    ordered
    immutable
    hashable
    constructor takes an iterable of anything

set
    iterable, not indexable
    unordered
    mutable
    not hashable
    constructor takes an iterable of hashables

frozenset
    iterable, not indexable
    unordered
    immutable
    hashable
    constructor takes an iterable of hashables

dict
    iterable, not indexable
    unordered
    mutable
    not hashable
    constructor takes an iterable of iterables of key, value pairs; keys must be hashable
"""

i = 3 # ok,     i is an l-value
2 = 3 # not ok, 2 is an r-value

k = (i += j); # not ok

# Python operators do something or return something, but not both
# there is no pre-increment or post-increment operator

# true division always returns a float
# floor division with ints returns an int, with floats returns a float

