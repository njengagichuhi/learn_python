#Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different
#code,use the code from the solution), and instead of printing the results to a screen, write the results to a txt file.
#In your code, just make up a name for the file you are saving to.


import requests
from bs4 import BeautifulSoup

fi=open("abc.txr","w")

def decode():
    html_text=requests.get('https://www.nytimes.com/').text
    soup=BeautifulSoup(html_text,'lxml')
    head=soup.findAll('title')

    for i in head:
        fi.writelines(i.text)

    fi.close()
decode()

# "print(decode())\n"]
# fi.writelines(a)