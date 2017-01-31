# -----------
# Fri, 27 Jan
# -----------

"""
assertions are not good for testing
and they're not good for user errors

unit tests are good for testing
exceptions are good for user errors

let's explore what we can do in the absence of exceptions

three avenues of communication between functions:

1. return values
2. global variables
3. parameters

Java and Python hold primitive types by value   (e.g. int, double)
Java and Python hold composite types by address (e.g. Java's ArrayList, Python's list)

for paramter passing to work, we need a composite type, see below
"""

def f (..., y2) :
    ...
    if (<something wrong>) :
        y2[0] = -1
        return 0
    ...

def g (...) :
    ...
    y = [0]
    x = f(..., y)
    if (y[0] == -1) :
        <something wrong>
    ...

...
g(...)
...
