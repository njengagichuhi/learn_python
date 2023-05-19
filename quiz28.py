#Implement a function that takes  input as three variables,
#and returns the largest of the three.
#Do this without using the Python max() function!
#The goal of this exercise is to think about some internals that Python normally
#takes care of for us. All you need is some variables and if statements!
var1=input('enter name1:')
var2=input('enter name2:')
var3=input('enter name3:')
def maxmum():
    if var1>var2 or var1>var3:
        print(var1)
    elif var2>var1 or var2<var3:
        print(var2)
    elif var3>var1 or var3<var2:
        print(var3)
    elif var1==var2 or var2==var3:
        print("they are all equal")
    else:
        print( 'enter a name!!')
maxmum()





