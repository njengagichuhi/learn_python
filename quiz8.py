import random
gues=["rock","paper","scissors"]

while True:

        b=random.choice(gues)
        user_input=input("enter a word:").lower()
        if user_input==b:
            print("its s tie")
        elif  b=="paper" and user_input=="rock" or b=="scissors"and user_input=="paper" or b=="rock" and user_input=="scissors":
            print("you loose")
        elif  user_input=="paper" and b=="rock" or user_input=="scissors"and b=="paper" or user_input=="rock" and b=="scissors":
            print("you loose")
        else:
            print("enter the correct word")
        usr_command = input("DO you to quit")
        if usr_command == "quit":
            break

