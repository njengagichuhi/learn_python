#Use the BeautifulSoup and requests Python packages to print
# out a list of all the article titles on the New York Times homepage.
def decode():
    import requests
    from bs4 import BeautifulSoup
    html_text=requests.get('https://www.nytimes.com/').text
    soup=BeautifulSoup(html_text,'lxml')
    head=soup.select('title')
    return (head)
print(decode())

