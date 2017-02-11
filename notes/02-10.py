# -----------
# Fri, 10 Feb
# -----------

# Java
TreeSet<Integer> x = new TreeSet<Integer>()
...
Integer s = 0
Iterator<Integer> p = x.iterator();
while (p.hasNext()) {
    v = p.next();
    s += v;}
S.O.P(s); # 9

# Python
a = {2, 3, 4}
s = 0
for v in a :
    s += v
print(s) # 9

print(type(a)) # set
p = iter(a)
print(type(p)) # set iterator

s = 0
try :
    while True :
        v  = next(p)
        s += v
except StopIteration :
    pass
print(s)

reduce(<binary function>, <iterable>, <seed>)

"""
Python caches literal ints, floats, and strings.
It also caches int values in the range [-5, 256]
"""
