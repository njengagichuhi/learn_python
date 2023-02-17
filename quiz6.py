#Ask the user for a string and print out whether this string is a palindrome or not.
# #(A palindrome is a string that reads the same forwards and backwards.)
def palindrom():
    word=input("enter s word:")
    if word==word[::-1]:
        print("its a palindrom")
    else:
        print("try next time")

palindrom()


