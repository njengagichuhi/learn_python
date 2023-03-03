#Write a program (function!) that takes a list and returns a new list that contains
#all the elements of the first list minus all the duplicates
def fruits(a):
    b=list(set(a))

    return b
print(fruits(a=["mangoes","banans","oranges","banans"]))

def fruits(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b
print(fruits(["mangoes","banans","oranges","banans"]))








