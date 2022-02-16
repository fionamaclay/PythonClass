fh = open("mug_brownie.md")

for line in fh.readlines():
    print(line, end="")

fh.close()

