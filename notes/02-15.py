# -----------
# Wed, 15 Feb
# -----------

f = lambda x, y : x + y
assert f(2, 3) == 5

def f (x) :
    g = lambda y : x + y
    x += 3
    return g

print(f(2)(4)) # 9

def f (x) :
    g = lambda y : x + y
    x += [3]
    return g

print(f([2])([4])) # [2, 3, 4]

a  = [2, 3, 4]
x  = (v + 1 for v in a)
a += [5]
print(list(x))         # [3, 4, 5, 6]

a  = (2, 3, 4)
x  = (v + 1 for v in a)
a += (5,)
print(list(x))         # [3, 4, 5]

a = [2, 3, 4]
print(type(a)) # list

p = iter(a)
print(type(p)) # list iterator

print(a is p)  # false

q = iter(p)
print(type(q)) # list iterator

print(q is p)  # true

a = [2, 3, 4]

p = iter(a)
v = next(p)   # first element of a
g(v)

for v in p :  # rest of the elements of a
    h(v)
