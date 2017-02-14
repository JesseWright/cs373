# -----------
# Mon, 13 Feb
# -----------

def reduce (bf, a, v) :
    for w in a :
        v = bf(v, w)
    return v

"""
reduce takes a seed so that it can return that seed
if the iterable is empty

the real reduce takes a seed optionally and raises an exception
if the iterable is empty
"""
