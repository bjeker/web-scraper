import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.string
results = soup.find(id="ResultsContainer")

titles = soup.find_all('a', class_='_3ryJoIoycVkA88fy40qNJc')

with open('reddit.txt', 'w') as file:
    file.write(title)
    for title in titles:
        file.write(str(title.get("href")) + '\n')