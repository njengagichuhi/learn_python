#This time, we’re going to do exactly the opposite.
#You, the user, will have in your head a number between 0 and 100.
#The program will guess a number, and you, the user, will say whether
#it is too high, too low, or your number.import random
import random
print("WELCOM TO A GUESSING GAME")
num_of_guess=5
for i in range (num_of_guess):
    p=random.randint(0,100)
    user_input=input("enter a num in range 0-100:")
    if int(user_input) == int(p):
        print("they match.you win")
        break

    elif  int(user_input) >= int(p):
        print("your gues is too low")
    elif   int(user_input) <= int(p):
        print("your gues is too high")
    elif (i == guesses_allowed - 1):
        rint("Sorry, you have run out of guesses. You lose!")

    else:
        print("good buy")
    print("your guess",p)
    print("the number is",user_input)

if (i == num_of_guess - 1):
    print("Sorry, you have run out of guesses. You lose!")
