#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
#One .txt file has a list of all prime numbers under 1000, and the other.
#txt file has a list of happy numbers up to 1000.

from difflib import Differ

file_1=open("C:\\Users\\HP\\Downloads\\happynumbers.txt",'r')
file_2=open("C:\\Users\\HP\\Downloads\\primenumbers.txt",'r')
differ=Differ()
for line in differ.compare(file_1.readlines(),file_2.readlines()):
    print(line)
print('vlues without any symbols overlap')