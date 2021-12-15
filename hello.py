print('hello, world!')
x = 0
y = 0
def incr(x):
    y = x + 1
    return y
    incr(5)
    print(x, y)

pi = 3.14
def area(r):
    return pi * r * r

numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print(square(5))
print(square(2*5))

x = 1
def f():
    return x
print(x)
print(f())