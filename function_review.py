"""2021-12-15 -- functions review and expressions evaluating"""

DRINKS = ["beer" , "wine" , "sake" , "whiskey"]

def greeting(name , language , time):
    if language == "spanish":
        message = "buenos"
    else:
        message = "good"
    print(message , time , name)
    alcohol = ['beer', 'wine', 'sake', 'whiskey']

def is_allowed(beverage, age):
    if beverage in DRINKS and age < 21:
        return False
    else:
        return True

def buy(name , buyer , quantity , price):
    if not is_allowed(name, buyer['age']):
        return False
    elif buyer['inventory']['cash'] < price:
        return False
    
    if name not in buyer['inventory'].keys():
        buyer['inventory'][name] = 0

    # add to inventory  
    new_ammt = buyer['inventory'][name] + quantity
    print(f"{buyer['name']} now has {new_ammt} drinks of {name}.")

    # subtracting from cash
    remaining = buyer['inventory']['cash'] - (price * quantity)
    buyer['inventory']['cash'] = remaining
    print(f"{buyer['name']} has {remaining} dollars left.")
    
    buyer['inventory'][name] = quantity


def drink(name , drinker , quantity):
    if not is_allowed(name, drinker['age']):
        return
    elif name not in drinker['inventory'].keys() or drinker['inventory'][name] < quantity:
        return
    new_inv = drinker['inventory'][name] - quantity
    drinker['inventory'][name] = new_inv
    print(f"{drinker['name']} has {new_inv} drinks left of {name}.")

# homework
# --------
# 1. drink()
# write a drink function that takes the arguments name, drinker and quantity
# it should call the is_allowed() function to check if the person is allowed to drink that beverage
#   and return False if they are not
# then it should subtract quantity from their inventory for that particular drink
# 2. in buy(), check if the buyer already has that kind of drink in their inventory
#    and if so, add to the existing count

# expression evaluating
# ---------------------
# notes: order of operation for
# replace variable names with values
# */ before +-
# inner then outter
# left to right

name = "alissa"
description = "tired"

message = (name.title() + " is " + description + "\n") * 3
# message = ("alissa".title() + " is " + "mean" + "\n") * 3
# message = ("Alissa" + " is " + "mean" + "\n") * 3
# message = ("Alissa is mean \n") * 3
# message = "Alissa is mean \n" * 3
# message = "Alissa is mean \nAlissa is mean \nAlissa is mean \n"

print(message)

bugsie = {
    "name": "Bugsie" ,
    "age": 19 ,
    "height": 72 ,
    "inventory": {
        "cash": 100 ,
        "beer": 0 ,
        "wine": 0 ,
        "sake": 0 ,
        "whiskey": 0 ,
    }
}

nina = {
    "name": "Nina" ,
    "age": 21 ,
    "height": 68 ,
    "inventory": {
        "cash": 1000 , 
        "beer": 5 ,
        "wine": 2 ,
        "sake": 0 ,
        "whiskey": 3 ,
    }
}


greeting("alissa", "eng", "morning")
# good morning alissa

greeting("alissa", "eng", "evening")
# good evening alissa

greeting("connnor", "spanish", "d??as")
# buenos d??as connor

greeting("mocha", "spanish", "noches")
# buenos noches mocha

greeting(name="john", language="en", time="afternoon")

greeting(language="en", time="day", name="tia")
print()

greeting(language="martian", time="martian night,", name="martian")
print()

print(is_allowed("wine", 7))
print(is_allowed("beer", 43))
print(is_allowed("milk", 17))
print(is_allowed("soda", 25))
print()

print("Bugsie has: ", bugsie['inventory'])
print("Nina has: ", nina['inventory'])

buy("beer", bugsie, 1 , 5)
buy("wine", nina, 4 , 5)
buy("pepsi", bugsie, 12, 2)
buy("pepsi", bugsie, 2, 2)

print("Bugsie has: ", bugsie['inventory'])
print("Nina has: ", nina['inventory'])

drink("beer", nina, 1)

drink("juice", nina, 1)

buy("milk" , nina , 2 , 4)