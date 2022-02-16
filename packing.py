def create_packing():
    to_pack = ["clothes", "toiletries", "charger"]

    fh = open("packing.txt", "w")

    for thing in to_pack:
        fh.write(f"- {thing}\n")

    fh.close()

def addto_packing():
    fh = open("packing.txt", "a")

    fh.write("- a good attitude\n")

    fh.close()


create_packing()
addto_packing()