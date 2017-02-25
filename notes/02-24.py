# -----------
# Fri, 24 Feb
# -----------

class Map :
    def __init__ (self, uf, a) :
        self.uf = uf
        self.p  = iter(a)

    def __iter__ (self) :
        return self

    def __next__ (self) :
        return self.uf(next(self.p))

def map (uf, a) :
    for v in a :
        yield uf(v)

def map (uf, a) :
    return (uf(v) for v in a)

class Range :
    class Iterator :
        ...

    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return Range.Iterator(self.b, self.e)

class Range :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        b = self.b
        while b != self.e :
            yield b
            b += 1
