#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low,too high or exactly right
import random
def game():
    while True:
            guess=random.randint(0,9)
            user_input=input("enter a number:")

            if user_input.isnumeric():
                user_input = int(user_input)

                if guess==user_input:
                    print("you are exactly right")

                elif user_input > guess:
                    print("your gues is too high")
                elif user_input < guess:
                    print("your gues is too low")
                else:
                    print("enter correct word")
            else:
                print("do you want to quit")
            user_in=input("i quit:")
            if user_in== "quit":

                break
print(game())


