import requests
from bs4 import BeautifulSoup

urls_manga = []


def get_manga_of_page():
	page = requests.get('http://fanfox.net/manga')
	soup = BeautifulSoup(page.text, 'html.parser')
	max_page = BeautifulSoup(page.text, 'html.parser').find()
	for p in soup.findAll('p', 'manga-list-1-item-title'):
		for a in p.select('a[href]'):
			urls_manga.append(a['href'].split('/manga')[1])


# get_manga_of_page()
# print(urls_manga)

page = requests.get('http://fanfox.net/manga')
soup = BeautifulSoup(page.text, 'html.parser')
x = soup.select(".pager-list-left")
y = x[x.length - 1]
print(y)