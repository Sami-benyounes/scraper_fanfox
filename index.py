import requests
from bs4 import BeautifulSoup

page = requests.get('http://fanfox.net/manga')
soup = BeautifulSoup(page.text, 'html.parser')

urls_manga = []


for p in soup.findAll('p', 'manga-list-1-item-title'):
	for a in p.select('a[href]'):
		urls_manga.append(a['href'].split('/manga')[1])

print(urls_manga)

