#Ask the user for a number.
#Depending on whether the number is even or odd, print out an appropriate message to the user

def a_number():
    num=int(input("enter a number:"))
    if num%2==0:
        print("its an even number")
    else:
        print("its an odd number")
a_number()


