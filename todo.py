fh = open("todo.txt")

for line in fh.readlines():
    print("* " , line , end="")

fh.close()