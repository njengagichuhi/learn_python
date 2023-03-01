def fibonacci():
    use_input=int(input("enter you range:"))
    l=[0, 1]
    for i in range(use_input):
        l.append(l[i]+l[i+1])

    return l


print(fibonacci())
