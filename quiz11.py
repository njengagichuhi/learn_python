#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#and makes a new list of only the first and last elements of the given list.
#For practice, write this code inside a function.
def my_list(a):
    first_elm=a[0]
    last_elm=a[-1]
    result=[first_elm,last_elm]
    return result
print(my_list(a=  [5, 10, 15, 20, 25] ))
