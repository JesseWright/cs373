# -----------
# Fri, 17 Feb
# -----------

# two xs, the first global, the second local

x = 2

def f () :
    def g () :
        x = 3
        return x
    def h () :
        return x
    return (g, h)

g, h = f()
print(g()) # 3
print(h()) # 2

# one x, global

x = 2

def f () :
    def g () :
        global x
        x = 3
        return x
    def h () :
        return x
    return (g, h)

g, h = f()
print(g()) # 3
print(h()) # 3

# two xs, the first local to f, the second local to g

def f () :
    x = 2
    def g () :
        x = 3
        return x
    def h () :
        return x
    return (g, h)

g, h = f()
print(g()) # 3
print(h()) # 2

# one x, local to f

def f () :
    x = 2
    def g () :
        nonlocal x
        x = 3
        return x
    def h () :
        return x
    return (g, h)

g, h = f()
print(g()) # 3
print(h()) # 3
