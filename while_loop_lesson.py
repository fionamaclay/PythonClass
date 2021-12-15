import random

num = 0

while num < 10:
    num = random.randint(0, 20)
    print("your number is:", num)
print()

name = ""
while not name:
    name = input("What is your name? ")

print(f"Hello there {name}!")
print()

flip = ""
while flip not in ["heads" , "tails"]:
    flip = input("Heads or tails? ")

print(f"{flip} is correct!")
print()

num = 0
while num < 50:
    num = random.randint(0 , 100)
    print("your number is:" , num)
print()

import random
while True:
    num = random.randint(0 , 10)
    print("The number is: " , num)
    reply = input("Keep going? ")
    if reply == "no":
        break
print()

num = 0
while num < 500:
    num = random.randint(1 , 1000)
    print("Your number is: " , num)
    if num%10 == 0:
        break