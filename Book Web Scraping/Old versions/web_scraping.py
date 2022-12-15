from bs4 import BeautifulSoup
import requests
import pandas as pd
import itertools

book_name = input("Book Title: ")

book_title = []
book_price = []

# URL = "https://bookoholic.net/category/16/angliyski-knigi.html?page="
URL = "https://bookoholic.net/search.html?phrase=" + str(book_name) + "&page="



for pages in range(1, 6):
    req = requests.get(URL + str(pages))

    soup = BeautifulSoup(req.text, "html.parser")

    for element in soup.findAll(attrs={'class': 'c-product-grid__hover-product-info'}):
        name = element.find('a', attrs={'class': 'c-product-grid__product-title-link js-has-data-productId'})
        price = element.find('span', attrs={'class': 'c-price-exclude-taxes__no-wholesale-price-list-price price-value'})
        book_title.append(name.text)
        book_price.append(price.text)

for names in book_title:
    print(names)
for prices in book_price:
    print(prices)

# df = pd.DataFrame({'Book Titles': book_title, 'Book Price': book_price})
# df.to_excel('books2.xlsx', index=False)
