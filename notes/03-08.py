# -----------
# Wed,  8 Mar
# -----------

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
