# start at 1.7 Conditional Expressions in the 
# Python Practice Book 
# https://anandology.com/python-practice-book/getting-started.html
print("Review Practice:")
print("hello")
number = 5
name = "fiona"
print(len(name))
letters = ["a" , "b" , "c"]
woman = {
    "name" : "fiona" ,
    "age" : 20 ,
    "location" : "denver" ,
}
print(letters[1])
print(woman["name"])
text = str(number)
print(type(text))

def square(x):
    return x * x

def sum_of_squares(x, y):
    return square(x) + square(y)

f = square

def fxy(f, x, y):
    return f(x) + f(y)

num = 0
print("global num is:", num)

def incr(num):
    print("in incr() num is:", num)

    total = num + 1
    return total

def welcome(name):
    return "welcome " + name + "!"

text = welcome("fiona")
print(text)

pi = 3.14
def area(r):
    return pi * r * r

numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print("1.5 Functions:")
print(welcome("gizmo"))
print(welcome("mocha"))
print(welcome("alissa"))

print("---------------------")
result = incr(5)
print("the result is:", result)
print("global num is:", num)
print("---------------------")

result = incr(8)
print("the result is:", result)
print("global num is:", num)
print("---------------------")

result = incr(2)
print("the result is:", result)
print("global num is:", num)
print("---------------------")

print("numcalls:", numcalls)

print(square(5))
print(square(2) + square(3))
print(square(square(3)))
print(sum_of_squares(2, 3))
print(f(4))
print(fxy(square, 2, 3))
print("---------------------")
print(area(3))
print(area(2))
print("---------------------")

print("numcalls:", numcalls)
print("square of 2:", square(2))
print("numcalls:", numcalls)
print("--------------------")

print("1.7 Conditional Expressions:")
print("2 < 3 is" , 2 < 3)
print("2 > 3 is" , 2 > 3)
x = 5
print ("2 < x < 10 is" , 2 < x < 10)
print(2 < 3 < 4 < 5)
print("python > perl is" , "python" > "perl")
print("python > java is" , "python" > "java")
print("---------------------")
print("True and True is" , True and True)
print("True and False is" , True and False)
print("Example:")
print("2 < 3 and 5 < 4 is" , 2 < 3 and 5 < 4)
print("2 < 3 or 5 < 4 is" , 2 < 3 or 5 < 4)
print("----------------------")

if x % 2 == 0:
    print('even')
x = 3
if x % 2 == 0:
    print ("x is even")
else:
    print("x is odd")
print("----------------------")

x = 42
if x < 10:
    print('x is one digit number.')
elif x < 100:
    print("x is two digit number.")
else:
    print("x is big number.")
print("-----------------------")

x = 2
if x == 2:
    print(x)
else:
    print(y)

x = 3
if x == 2:
    print(x)
else:
    print("no")
print("-------------------------")

print("Letter Grade If Statement Example:")
x = 89
if x >= 100:
    print("A+")
elif x >= 90:
    print("A")
elif x >= 88:
    print("A-")
elif x >= 80:
    print("B")
elif x >= 78:
    print("B-")
elif x >= 70:
    print("D")
elif x >= 65:
    print("D-")
else:
    print("F")
print("---------------------------")

print("1.8 Lists:")
x = [1 , 2 , 3]
x = ["hello" , "world"]
x = [1 , 2 , "hello" , "world" , ["another" , "list"]]

print("the length of x is" , len(x))

x = [1 , 2 , 3]
print("the second item in the list is" , x[1])
x[1] = 4
print(x[1])
print(x)
print("----------------------------")

print("1.9 Modules:")
x = range(10)
print(x)
for x in [1 , 2 , 3 , 4]:
    print(x)
for i in range(10):
    print(i , i*i , i*i*i)
