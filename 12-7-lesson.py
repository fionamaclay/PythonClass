""" Exercises
---------

1. Assign your name (capitalized) to the variable text 
and find out what the "minimum" letter is.
2. Find out the maximum length of a list of strings.
   ie: ["title", "author", "year"]
"""
# def max_length(name):
#    len(name)
#    print(f"the maximum length in the list is {name}, {len(name)} characters long.")

text = ["F" , "I" , "O" , "N" , "A"]
text_two = "FIONA"

print("the minimum letter is:" , min(text))
print("the minimum letter is:" , min(text_two))

print()

strings = ["alissa" , "fiona" , "katrina" , "mocha" , "gizmo"]
print("the max word is: " , max(strings))
print("the length of the max word is: " , len(max(strings)))
print("However, this is not what we are looking for.")

print()

strings_two = [len("alissa") , len("fiona") , len("katrina") , len("mocha") , len("gizmo")]
print("the max length in strings_two is: " , max(strings_two))

print()

sizes = []

for name in strings:
    max_name = 
    print(f"{max_name} is {len(max_name)} characters long.")