# -----------
# Wed, 20 Mar
# -----------

"""
algebras
    elements
    operations
    closed or open

integer arithmetic
    integers
    +, -, *, /
    closed on +, -, *
    open on /

relational algebra
    relations (tables)
    select
    project
    join (lots of flavors)
    closed on all operations

movie table
    title, director, year, genre
    "shane", "george stevens", 1954, "western"
    "star wars", "george lucas", 1977, "western"

[{"title": "shane", "director" : "george stevens"...}
 ...]

select(relation, unary predicate) -> relation
"""

def select (
        r: Iterable[Dict[str, int]],
        f: Callable[Dict[str, int], bool])
        -> Iterator[Dict[str, int]] :

    for d in r :
        if f(d) :
            yield d

    return (d for d in r if f(d))

    return filter(f, r)
