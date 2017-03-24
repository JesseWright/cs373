# -----------
# Fri, 24 Mar
# -----------

def theta_join (
    r: Iterable[Dict[str, int]],
    s: Iterable[Dict[str, int]],
    f: Callable[[Dict[str,int], Dict[str, int]], bool]
    -> Iterator[Dict[str, int]] :
    for v1 in r :
        for v2 in s :
            if f(v1, v2) :
                yield dict(v1, **v2)

    return (dict(v1, **v2) for v1 in r for v2 in s if f(v1, v2))


def natural_join (
    r: Iterable[Dict[str, int]],
    s: Iterable[Dict[str, int]]
    -> Iterator[Dict[str, int]]
    def f (v1, v2) :
        for k in v1 :
            if k in v2 :
                if v1[k] != v2[k]
                    return False
        return True
    def f (v1, v2) :
        all([v1[k] == v2[k] for k in v1 if k in v2])
    for v1 in r :
        for v2 in s :
            if f(v1, v2) :
                yield dict(v1, **v2)
