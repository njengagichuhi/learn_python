
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
#Let’s say I give you a list saved in a variable:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
def number(a):
    f=[]
    for i in a:
        if i%2==0 :
            f.append(i)
    return f
print(number([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))
