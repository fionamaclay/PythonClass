def feed(animal):
    if animal['hungry'] == True:
        animal['hungry'] = False
        animal['weight'] = animal['weight'] + 1
        print(animal['name']+"'s weight is" , animal['weight'])
    else:
        print('The Pypet is not hungry!')

def exercise(animal):
    if animal['hungry'] == False:
        animal['hungry'] = True
        animal['weight'] = animal['weight'] - 1
        print(animal['name']+"'s weight is" , animal['weight'])
    else:
        print('I will not starve!')

mocha = {
    'name' : 'mocha',
    'age' : 8,
    'weight' : 11,
    'hungry' : True,
    'photo' : '<`)))><',
}
gizmo = {
    'name' : 'gizmo',
    'age' : 7,
    'weight' : 10.5,
    'hungry' : True,
    'photo' : '<:3 )~~~~',
}
pets =[mocha, gizmo]

print('Welcome to Pypet!')

for pet in pets:
    print("----------------")
    print('Hello ' + pet['name'])
    print(pet['photo'])
    feed(pet)
    print()
    exercise(pet)