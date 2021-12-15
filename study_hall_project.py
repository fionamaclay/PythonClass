"""Generate the lyrics for:
   "99 bottles of beer on the wall"

    Example:
        99 bottles of beer on the wall.
            99 bottles of beer, take one down pass it around.
            98 bottles of beer on the wall.
            98 bottles of beer on the wall.
"""
bottles = 99
def take_one_down(bottles):
    new = bottles - 1
    
    if bottles > 1:
        word = "bottles"
    elif bottles == 1:
        word = "bottle"

    if new > 1:
        new_word = "bottles"
    elif new == 1:
        new_word = "bottle"
    elif new == 0:
        new = "No more"
        new_word = "bottles"

    print(bottles , word , "of beer on the wall,")
    print(bottles , word , "of beer. you'll take one down, pass it around--")
    print(new , new_word , "of beer on the wall!")
 
for bottles in range(99, 0, -1):
    if bottles == 99:
        take_one_down(bottles)
    elif bottles <= 98:
        print()
        print("Again!")
        take_one_down(bottles)