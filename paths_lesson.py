"""Figure out what the heck is going on with the error in the function: main_two()"""

# Fi -- The reason it wasn't working is because you installed the pathlib library.
#       pathlib comes with Python, so you don't need to install it
#       I think the version that you installed is (maybe?) for old versions of Python
#       So I think it got confused by the unexpected type.
#
#       Also, the open() in your main() function wasn't working either
#       but since you were opening a file that didn't exist (contacts.txt)
#       it just never got to the the open() call on line 26.
#
#       I changed both files to ones that exist, so they both work now.
#


from pathlib import Path

def main():
    path = Path("todo.txt")

    if not path.exists():
        print("Sorry, the file: contacts.txt does not exist.")
        return

    if not path.is_file():
        print("Silly goose! contacts.txt is not a file.")
        return

    fh = open(path)
    contents = fh.read()
    fh.close()
    print(contents)

def main_two():
    path = Path(__file__).parent / "mug_brownie.md"
    print(path.is_file())

    with open(path) as fh:
        contents = fh.read()
    
    print(contents)

def print_contents():
    path = Path(__file__).parent / "scores.txt"

    with open(path) as fh:
        contents = fh.read()

    print(f"~~~ {path.stem.upper()} ~~~")
    print(contents)


main()
print("-----------------------------------")
main_two()
print("-----------------------------------")
print_contents()