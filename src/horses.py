from bs4 import BeautifulSoup

import requests

url = "www.hkjc.com/chinese/racing/ListByStable.asp?TrainerCode=JM"

r = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

print soup.title.string

for link in soup.find_all('a'):
    print(link.get('href'))