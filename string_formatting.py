from random import randint

def rand_nums(amount=10, ceil=500):
    """Return a list of random positive and negative ints and floats"""
    numbers = []
    for _ in range(amount):
        # get a random float
        num = randint(-ceil, ceil) + (1 / randint(1, 99))

        # randomly make it an int
        if randint(0, 1):
            num = int(num)

        numbers.append(num)

    return numbers

def format_email(user, domain, extension):
    email = "{}@{}.{}"
    email = email.format(user, domain, extension)
    print(email)

def format_address(street, city, state, zip):
    address = "{} \n{}, {} {}"
    address = address.format(street, city, state, zip)
    print(address)

print(format(" String Formatting " , "_^60"))
print()

print(format("Presentation" , ".<50"))
print()

print("Printing a float: " , format(5, "f"))
print()

print("Defaulted without including 's': " , format("hello" , ""))
print("Using 's':" , format("hello" , "s"))
print()

print("Defaulted without including 'd': " , format(5 , ""))
print("Using 'd':" , format(5 , "d"))
print()

print(format("Precision" , ".<50"))
print()

print(format(2.5 , ".2f"))
print(format("Monday" , ".3s"))
print(format("Fiona" , ".2s"))
print()

print(format("Alignment Width" , ".<50"))
print()

print(format("hello" , "^20"))
print(format(22 , ">5d"))
print()

print(format(">" , ">5s") , format("=" , ">5s") , "\n")
for x in (25, -436, 8, 150, -32, 10):
    print(format(x ,">5d") , format(x , "=5d") , sep="  ")
print()

print(format(2 , "0>2d"))
print(format(5.2 , "0>5.2f"))
print()

print(format("Exercise 34 (String Formating)" , "_>64s"))
print()

print("1.")
print(format(48.7052 , ".2f"))
print()

print("2.")
print(format(2.5 , ".2f"))
print()

print("3.")
print(format(.25 , ".0%"))
print()

print("4.")
print(format("September" , ".3s"))
print()

print("5.")
print(format("Game Over" , "^80s"))
print()

print("6.")
print(format("8 of 10" , ">80s"))
print()

print("7.")
print(format("Question" , "=<30"))
print()

print(format("Exercise 35 (Align Numbers)" , "_>64s"))
print()

numbers = []
numbers.append(55)

rand_nums()

print(format("String Formatting Pt. 2", "_^57s"))
ex_one = "{0:.3s}".format("Monday")
print(ex_one)

ex_two = "{0:.3s} {1:.2f}".format("Monday", 5.234)
print(ex_two)

ex_three = "{1:.2f} {0:.3s}".format("Monday", 5.234)
print(ex_three)

ex_four = "The price on {0:.3s} is: {1:.2f}.".format("Monday", 5.234)
print(ex_four)

blueprint = "The price on {day:.3s} is: {cost:.2f}."
blueprint = blueprint.format(
    day="Monday",
    cost=5.234,
)
print(blueprint)
print()

print(format("Exercise 36", "_>60"))
print()

email = "{user:.3s}@{domain:.5s}.{extension:.3s}"
email = email.format(
    user="joe",
    domain="gmail",
    extension="com",
)
print(email)
print()

print("Bonus:")

format_email("joe", "gmail", "com")
format_email("fiona", "coolaf", "edu")
print()

print(format("f-strings", "_<60s"))
print()

day = "Tuesday"
cost = 1000000.5436
print(f"Fiona's bagel on {day:.3s} cost {cost:.2f} dollars!")
print()

print(format("Exercise 37 (Street Address):", "_>60s"))
print()

street = "1600 Pennsylvania Ave. NW"
city = "Washington"
state = "DC"
zip = 20500

print(f"{street} \n{city}, {state} {zip}")
print()
format_address("2541 S Lincoln St", "Denver", "CO", 80210)