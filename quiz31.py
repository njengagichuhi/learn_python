import random
def rand(f):
    Lines = f.readlines()

    e=random.choice(Lines)
    print(e)
    w= [i for i in e]
    x=[]
    chances=10
    while chances >0:

        user_input=input("enter a letter in uppercase:")
        for i in user_input:
            if i in w:
             x.append(i)
             print(x)
            else:
                print('doesnt exist in the word')
        continue

    if len(x)==len(w):
        print('ere')
    else:
        print("the letter is not in the word!!")



print(rand(f = open("J:\sowpods.file.txt", "r")))
