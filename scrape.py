from bs4 import BeautifulSoup
import requests 

url = "https://www.pararius.com/apartments/amsterdam"
page = requests.get(url)
# print(page)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
lists = soup.find_all('section', class_="listing-search-item")

for list in lists:
    title = list.find('a', class_="listing-search-item__link listing-search-item__link--title")
    location = list.find('div', class_="listing-search-item__sub-title")
    price = list.find('div', class_="listing-search-item__price")
    area = list.find('li', class_="illustrated-features__item--surface-area")
    info=[title]
    print(info)


