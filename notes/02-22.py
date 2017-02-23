# -----------
# Wed, 22 Feb
# -----------

r = range(2, 5)
print(r)        # range(2, 5)
print(list(r))  # [2, 3, 4]
print(list(r))  # [2, 3, 4]

i = iter(r)
print(i)        # <range_iterator object at 0x101392480>
print(list(i))  # [2, 3, 4]
print(list(i))  # []

r = range(2, 5)
for v in r :
    print(v, end=" ") # 2 3 4

for v in r :
    print(v, end=" ") # 2 3 4

i = iter(r)
for v in i :
    print(v, end=" ") # 2 3 4

for v in i :
    print(v, end=" ") # <nothing>

def f () :
    print("abc")
    yield 2
    print("def")
    yield 3.45
    print("ghi")

p = f()     # <nothing>
print(p)    # <generator object f at 0x1013de9e8>
v = next(p) # abc
print(v)    # 2
v = next(p) # def
print(v)    # 3.45
v = next(p) # ghi and raise StopIteration

def range_iterator (b, e) :
    while (b != e) :
        yield b
        b += 1
