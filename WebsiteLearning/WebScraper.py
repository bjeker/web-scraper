import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.string
results = soup.find(id="ResultsContainer")

job_elements= results.find_all("div", class_="card-content")

with open('output.txt', 'w') as file:
    file.write(title)
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")

        file.write(title_element.text + '\n')