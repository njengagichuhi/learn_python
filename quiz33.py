#Create a dictionary (in your file) of names and birthdays.
#When you run your program it should ask the user to enter a name,
#and return the birthday of that person back to them.

def birtday(names_birthdays):
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    print("Albert Einstein\nBenjamin Franklin\nAda Lovelace")
    while True:
        user_request=input(" Who's birthday do you want to look up?:")


        if user_request=="Albert Einstein":
            print("his birthday is on",names_birthdays["Albert Einstein"])
        elif user_request=="Benjamin Franklin":
            print("his birthday is on", names_birthdays["Benjamin Franklin"])
        elif user_request=="Ada Lovelace":
            print("his birthday is on", names_birthdays["Benjamin Franklin"])
        else:
            print("sorry the name doesnt exist")
            continue
print(birtday(names_birthdays={"Albert Einstein":'7/03/1994',"Benjamin Franklin":'8/11/200',"Ada Lovelace":'23/09/1994'}))