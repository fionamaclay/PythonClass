def create_xmas_shopping():
    people = [
        "alissa", 
        "mom", 
        "connie",
        "dad", 
        "mocha"
    ]
    fh = open("xmas_shopping.txt", "w")

    for name in people:
        fh.write(f"[ ] {name}\n")

    fh.close()

def addto_xmas_shopping():
    fh = open("xmas_shopping.txt", "a")

    fh.write("[ ] nina\n")

    fh.close()

create_xmas_shopping()
addto_xmas_shopping()


    