# -----------
# Mon,  6 Mar
# -----------

def make_iterable (c) :
    class iterable :
        def __init__ (self, *t, **d) :
            self.t = t
            self.d = d

        def __iter__ (self) :
            return c(*self.t, **self.d)

    return iterable
