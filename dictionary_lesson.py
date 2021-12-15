from pprint import pprint

shapes = {
    "triangle" : 3,
    "square" : 4,
    "rectangle" : 4,
    "pentagon" : 5,
    "hexagon" : 6,
}
print("shapes:")
pprint(shapes, width=59 , sort_dicts=False)
print()

print("Triangle:" , shapes["triangle"])
print("Square:" , shapes["square"])
print("Pentagon:" , shapes["pentagon"])
print()

hexagon = shapes.get("hexagon" , "unknown")
print("hexagon:" , hexagon)

octagon = shapes.get("octagon" , "unknown")
print("octagon:" , octagon)
print()

triangle = shapes.get("triangle" , "unknown")
rectangle = shapes.get("rectangle" , "unknown")

print("A triangle has" , triangle , "sides.")
print("A rectangle has" , rectangle , "sides.")

print("A triangle has" , shapes["triangle"] , "sides.")
print("A rectangle has" , shapes["rectangle"] , "sides.")

#name = input("shape: ")
#sides = shapes.get(name , None)
#if not sides:
 #   print("Sorry, I don't know the shape:" , name)
#else:
 #   print("A" , name , "has" , sides , "sides.")

shapes["circle"] = 0
shapes["star"] = 10
shapes.update({"heptagon" : 7 , "drop" : 0 , "parallelogram": 4})
shapes["oval"] = 0
shapes["square"] = "four"

print()
print("shapes:")
pprint(shapes , sort_dicts=False)

del shapes["star"]

print()
print("new shapes:")
pprint(shapes , sort_dicts=False)

print("------------------------")

numbers = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "ten" : 10,
}
print("numbers:")
pprint(numbers)