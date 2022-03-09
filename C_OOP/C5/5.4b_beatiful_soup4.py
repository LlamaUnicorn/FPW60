# pip3 install beautifulsoup4
# pip3 install lxml

from bs4 import BeautifulSoup
import requests

base = 'https://ru.stackoverflow.com'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', id='question-mini-list')
# print(div)

a = div.find_all('a', class_='s-link')
# print(a)

for _ in a:
    print(_.getText(), base + _.get('href'))