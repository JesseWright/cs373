# -----------
# Wed, 22 Mar
# -----------

def project (r, *t) :
    for d in r :
        x = {}
        for a in t :
            if a in d :
                x[a] = d[a]
        yield x

def project (r, *t) :
    for d in r :
        yield {a : d[a] for a in t if a in d}

def project (r, *t) :
    return ({a : d[a] for a in t if a in d} for d in r)



def cross_join (r, s) :
    for u in r :
        for v in s :
            yield dict(u, **v)

def cross_join (r, s) :
    return (dict(u, **v) for u in r for v in s)
