# -----------
# Wed,  8 Mar
# -----------

"""
In the Java library, class Stack EXTENDS class Vector.

That was a mistake, since clients of Stack can invoke any Vector method on a Stack.

The correct design would have been for Stack to CONTAIN Vector.

That design pattern is called the Adapter Pattern.
"""

class cache :
    def __init__ (self, f) :
        self.f = f
        self.d = {}

    def __call__ (self, n) :
        if n not in self.d :
            self.d[n] = self.f(n)
        return self.d[n]

def cache (f) :
    d = {}

    def g (n) :
        if n not in d :
            d[n] = f(n)
        return d[n]

    return g
