# -----------
# Mon, 27 Feb
# -----------

"""
three tokens: =, *, **
two contexts: function call, function definition
"""

def print (v, *, end="\n") :
    ...

def f (x, y, *, t, **d) :
    return list(x, y, t, d)

f(2, 3, y=4)


