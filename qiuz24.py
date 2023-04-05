#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
#One .txt file has a list of all prime numbers under 1000, and the other.
#`txt file has a list of happy numbers up to 1000.
#find the numbers that are overlapping

file_1=open("C:\\Users\\HP\\Downloads\\happynumbers.txt",'r')
p=[int(i) for i in file_1]
file_2=open("C:\\Users\\HP\\Downloads\\primenumbers.txt",'r')
c=[int(i)for i in file_2]
print(p)
print(c)

print('overlaping list ')
for i in p:
    if i in c:
        print(i)
