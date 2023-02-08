#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
name=input("enter your name:")
age=int(input("input your age:"))
current_year=int(2023)
date_of_birth=current_year-age
results=date_of_birth+int(100)
print(f"hello{ name }you will turn a hundred years on { results }")