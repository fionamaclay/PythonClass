""" Start on part 3.2, 
and work on installing modules for next time"""

from console import fg
from console import bg
from console import fx

import re
import textwrap

WIDTH = 60
MARGIN = "  "

"""
  =========
  World Map
  =========

            market
              |
  home -- town square -- woods -- hill
              |                    |
            bakery                cave

"""
DEBUG = False

PLAYER = {
    "place": "home" ,
}

PLACES = {
    "home": {
        "key": "home" , 
        "name": "Your cottage" ,
        "east": "town-square" ,
        "description": "Your humble bode and an ideal place to rest after tiresome adventures." ,
    },
    "town-square": {
        "key": "town-square" ,
        "name": "The Town Square" ,
        "west": "home" ,
        "description": "The hustlin' and bustlin' meeting place for the town." ,
    },
}

ITEMS = {
    "potion": {
        "key": "potion",
        "name": 'battle potion',
        "description": "boils the blood of one's enemies",
        "price": -10,
    },
    "sword": {
        "key": "sword",
        "name": "battle sword",
         "description": "super sharp killing machine",
         "price": -11,
    },
    "pillow": {
         "key": "pillow",
         "name": "plush pillow",
         "description": "soft pillow for sleepy time",
         "price": -5,
    },
}

def do_shop():
    """ To shop """
    print("Items for sale.")
    for item in ITEMS.values():
        print("item:" , item["name"])
        print("description:" , item["description"])
    
def do_quit():
    """ To exit the game """
    print("Goodbye.")
    quit()

def do_go(args):
    """ To move somewhere else """
    debug(f"Trying to go: {args}")
    if not args:
        error("Which way do you want to go?")
        return
    
    direction = args[0].lower()

    if direction not in ("north", "south", "east", "west"):
        error(f"Sorry, I don't know how to go: {direction}")
        return

    old_name = PLAYER['place']
    old_place = PLACES[old_name]
    new_name = old_place.get(direction)
    
    if not new_name:
        error(f"Sorry, you can't go {direction} from here.")
        return

    new_place = PLACES.get(new_name)

    if not new_place:
        error(f"Whoops! The information about {new_name} seems to be missing.")
        return

    PLAYER['place'] = new_name

    wrap(new_place['name'])
    wrap(new_place['description'])

def main():
    print("Welcome!")
    while True:
        debug(f"You are at: {PLAYER['place']}")
        
        reply = input("> ").strip()
        args = reply.split()

        if not args:
            continue

        command = args.pop(0)

        debug(f"Command: {command}, Args: {args}")

        if command == "q" or command == "quit":
            do_quit()
        elif command == "shop":
            do_shop()
        elif command == "g" or command == "go":
            do_go(args)
        else:
            error("No such command.")
            continue
      
def debug(message):
    if DEBUG:
        print("DEBUG: ", message)

def error(message):
    print("Error: ", message)

def wrap(text):
    paragraph = textwrap.fill(
        text,
        WIDTH,
        initial_indent = MARGIN,
        subsequent_indent = MARGIN,
    )
    print(paragraph)

if __name__ == "__main__":
    main()


