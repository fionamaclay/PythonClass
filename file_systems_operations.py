""" Begin on "Removing files" for next time"""

from pathlib import Path

# Exercise 68
def ex_68():
    cwd = Path.cwd()
    for f in cwd.iterdir():
        if f.name.startswith(".") or f.name.startswith("__"):
            continue
        if f.is_dir():
            print(f"{f.name}/")
        else:
            print(f.name)

# Exercise 69
def ex_69():
    path = Path.cwd()
    for f in path.rglob("*.txt"):
        print(f.name)

# Exercise 70
def ex_70():
    new_dir = Path("data") / "tmp"
    print(f"Creating directory: {new_dir}")
    new_dir.mkdir(exist_ok=True)

# Exercise 71
def ex_71():
    path = Path("data/tmp")
    print(f"Removing directory: {path}")
    path.rmdir()

# Exercise 72
new_dir = Path("data") / "tmp"
new_dir.mkdir(exist_ok=True)
def ex_72():
    for n in range(1, 10):
        path = new_dir / f"file_{n}.txt"
        print (f"Touching file: {path}")
        path.touch()

ex_72()