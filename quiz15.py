#Write a program (using functions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order.
def revers():
    say_something=input("enter a sentence:")
    b=say_something.split()
    c=b[::-1]
    d=" ".join(c)
    return d
print(revers())