# -----------
# Mon, 20 Feb
# -----------

"""
Java has a CLOSED object model
all instances of a class have the same data and
the amount of data is unchangeable over time

Python has an OPEN object model
instances of the same class can have different data and
the amount of that data can change per instance over time

Python wraps many specially-named methods with functions:
https://docs.python.org/3/reference/datamodel.html

map() takes an N-arg function followed by N iterables and
returns a generator of the results of invoking that function
on corresponding elements of the iterables

zip() takes N iterables and returns a generator of tuples
of the correspoinding elements of the iterables
"""

class RangeIterator :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __next__ (self) :
        if self.b == self.end :
            raise StopIteration
        v = self.b
        self.b += 1
        return v

    def __iter__ (self):
        return self
