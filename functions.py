import random

def number():
    num = random.randint(0, 100)
    return num

def hello():
    print("Hello.")
hello()

def welcome():
    print("Welcome to coding class!")

def hr():
    print("-" * 100)
hr()

def hello(name):
    message = "Hello " + name + "."
    print(message)
hello("Fiona")

def greeting(time, name):
    """Return greeting based on time of day"""
    message = "Good " + time + name + "."
    print(message)
greeting("morning, ", "Mom")

def header(title):
    message = title + "\n" + ("-" * len(title))
    print(message)
header("Chapter 69: The Return")
print()

def birthday(name, month, day, year):
    message = name + "'s birthday is on " + month + " " + str(day) + ", " + str(year) + "."
    print(message)

def winners(first, second, third):
    """Print the contest winner"""
    print(f"The first place winner is: {first}.")
    print(f"The second place winner is: {second}.")
    print(f"The third place winner is: {third}.")

def print_stuff():
    print("I'm printing stuff.")
    return
    print("I'm done printong stuff.")

def hr(width):
    if width < 0:
        print("width can't be negative.")
        return

def letter_count(text):
    message = "There are " + str(len(text)) + " characters in " + text + "."
    return message

def is_vowel(text):
    letters = ["a", "e", "i", "o", "u"]
    if text.lower() in letters:
        return True
    else:
        return False

def tip(cost, percent):
    percent = percent / 100
    amount = cost * percent
    return amount

def total(bill, tip_percent):
    total = tip(bill, tip_percent) + bill
    return format(total, ".2f")

winners("Me", "Myself", "I")
print()
winners("I", "Me", "Myself")
print()
winners(first="Me", second="Myself", third="I")
print()
winners("I", second="Me", third="Myself")
print()
winners(second="Fi", third="Mocha", first="Gizmo")
print()

print("a", "b", "c", sep="\n")

print("I'm", end="...")
print("so", end="...")
print("sleepy", end="...")
print()

birthday("Fiona", "November", 22, 2000)
birthday(name="Mom", month="March", day=27, year=1967)
print()

rand = number()
new_number = rand * 5
print("your number is", rand)
print("your number times 5 is", new_number)

print(number())
print(letter_count("gizmo"))
print(is_vowel("a"))
print(is_vowel("f"))
print(is_vowel("A"))

letter = "f"
answer = is_vowel(letter)
print(f"is {letter} a vowel?", answer)

letter = "b"
answer = is_vowel(letter)
print(f"is {letter} a vowel?", answer)
print()

cost = 15
percent = 20
amount = tip(cost, percent)
print(f"A {percent}% tip on a ${cost} bill is {amount}.")
print()

print("Your total is", total(100, 20))
print("Your total is", total(25, 30))

