"""Start on 5.4 for next time."""

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
        "items": ["book" , "desk"] ,
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
        "name": 'Battle Potion',
        "description": "A potion which boils the blood of one's enemies",
        "price": -10,
    },
    "sword": {
        "key": "sword",
        "name": "Battle Sword",
         "description": "A super sharp killing machine",
         "price": -11,
    },
    "pillow": {
         "key": "pillow",
         "name": "Plush Pillow",
         "description": "A soft pillow for sleepy time",
         "price": -5,
    },
    "desk" : {
        "key": "desk" ,
        "name": "Desk" ,
        "description": "A wooden desk with a large leather-bound book open on its surface" ,
    },
    "book": {
        "key": "book" ,
        "name": "Book" ,
        "description": "A leather-bound book open to an interesting passage..." ,
    },
}

def do_shop():
    """ To list items for sale """
    header(f'{fg.blue("Items for Sale!")}')
    for item in ITEMS.values():
        if "price" not in item:
            continue
        write(f"{item['name']}: {item['description']}")
    
def do_quit():
    """ To exit the game """
    write("Goodbye.")
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

    header(new_place['name'])
    wrap(new_place['description'])

def do_examine(args):
    """ To examine an object """
    debug(f"Trying to examine: {args}")
    if not args:
        error("What do you want to examine?")
        return
    
    place_name = PLAYER['place']
    place = PLACES[place_name]

    name = args[0].lower()

    if name not in place.get("items", []):
        error(f"Sorry, I don't know what {name} is.")
        return
    elif name not in ITEMS:
        error(f"Whoops! The information about {name} seems to be missing.")
        return

    item = ITEMS[name]

    header(item["name"])
    wrap(item["description"])


def do_look():
    """ To look around your current location"""
    debug("Trying to look around.")

    place_name = PLAYER["place"]
    place = PLACES[place_name]

    header(place["name"])
    wrap(place["description"])

    items = place.get("items", [])

    if items:
        names = []
        for key in items:
            item = ITEMS.get(key)
            names.append(item["name"])
        last = names.pop()
        text = ", ".join(names)
        if text:
            text = text + " and " + last
        
        print()
        write(f"You see {text}.")
            

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
        elif command == "x" or command == "exam" or command == "examine":
            do_examine(args)
        elif command == "l" or command == "look":
            do_look()
        else:
            error("No such command.")
            continue
        
def debug(message):
    if DEBUG:
        print("DEBUG: ", message)

def error(message):
    print(f"{fg.red('Error: ')} {message}")

def wrap(text):
    paragraph = textwrap.fill(
        text,
        WIDTH,
        initial_indent = MARGIN,
        subsequent_indent = MARGIN,
    )
    print(paragraph)

def write(text):
    print(MARGIN, text)

def header(title):
    print()
    write(f"{fx.bold(title)}")
    print()

if __name__ == "__main__":
    main()

