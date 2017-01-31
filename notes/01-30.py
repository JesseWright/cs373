# -----------
# Mon, 30 Jan
# -----------

def f (...) :
    ...
    if (<something wrong>) :
        raise E(...)
    ...

def g (...)
    ...
    try :
        ...
        x = f(...)
        ...
    except E as e :
        ...
    else :
        ...
    finally :
        ...
    ...

...
g(...)
...

x = [2, 3, 4]
print(type(x)) # list
x[1] = 5

x = (2, 3, 4)
print(type(x)) # tuple
x[1] = 5       # not ok

x = [6]
print(type(x)) # list
print(len(x))  # 1

x = (6)
print(type(x)) # int

x = (6,)
print(type(x)) # tuple
print(len(x))  # 1

# in Java

A x = new A(...)
A y = new A(...)

S.O.P(x == y)     # identity comparison
S.O.P(x.equals(y) # content  comparison

# in Python

x = A(...)
y = A(...)

print(x is y) # identity comparison
print(x == y) # content  comparison
