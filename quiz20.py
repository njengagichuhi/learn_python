import requests
from bs4 import BeautifulSoup
html_text=requests.get(' http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture').text
soup=BeautifulSoup(html_text,"html.parser")
print(soup.get_text())