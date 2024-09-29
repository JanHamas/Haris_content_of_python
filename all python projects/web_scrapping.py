from bs4 import BeautifulSoup
import requests

url = input("Enter url: ")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2',{'class':'post-title'})
print(title[0].get_text())
