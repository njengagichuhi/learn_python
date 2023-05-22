import random
def rand():
    f = open("J:\sowpods.file.txt", "r")
    Lines = f.readlines()
    e=random.choice(Lines)
    return e
print(rand())

