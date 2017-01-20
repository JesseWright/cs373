-----------
Fri, 20 Jan
-----------

"""
cycle of 3 is:
3 10 5 16 8 4 2 1

assertions are not good for user errors
and they're not good for testing

In Java "this" is in non-static methods
There is no "this" in static methods

Same thing happens in Python
"""

class A :
    def f (self, i) : # notice "self" is analagous to "this"
        ...

    @staticmethod
    def g (j) :       # notice no "self"
        ...

x = A()
x.f(2)    # non-static method invocation
A.f(x, 2) # same thing, makes no sense in Java

A.g()     # static method invocation
