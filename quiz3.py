#Take a list, say for example this one:
#and write a program that prints out all the elements of the list that are less than 5
def less_than(a):

    for num in a:
        if num <5:
            print(num)

less_than([1,2,3,4,5,6,7,9])

