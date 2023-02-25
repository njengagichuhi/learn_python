#Ask the user for a number and determine whether the number is prime or not.

def prime():

        my_num=int(input("enter a number:"))
        for i in range(1,my_num):
            if my_num%2==0:
                return "its not a prime number"
            else:
                return "its a prime number"
print(prime())
