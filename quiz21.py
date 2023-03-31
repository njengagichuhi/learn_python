#Write a function that takes an ordered list of numbers (a list where the elements are in order
#from smallest to largest)
#and another number.
#The function decides whether or not the given number is inside the
#list and returns (then prints) an appropriate boolean.
def list_of_num(list,m):
    l=0
    h=len(list)-1
    while l<=h:
        mid= (l+h)//2
        if list[mid]==m:
            return True

        else:
             if list[mid]<m:
                l= mid+1
             else:
                h=mid-1
    return False
print(list_of_num([2,3,4,5,6,7,8,9,22,55,66],4))

