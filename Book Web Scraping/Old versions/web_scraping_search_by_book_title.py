from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

book_name = input("Enter book name: ")

book_title = []
book_price = []

driver = webdriver.Chrome()
driver.get('https://bookoholic.net/search.html?phrase='+str(book_name))

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for element in soup.findAll(attrs={'class': 'c-product-grid__hover-product-info'}):
    name = element.find('a', attrs={'class': 'c-product-grid__product-title-link js-has-data-productId'})
    price = element.find('span', attrs={'class': 'c-price-exclude-taxes__no-wholesale-price-list-price price-value'})
    book_title.append(name.text)
    book_price.append(price.text)


# Print in console
#
# for x in book_title:
#    print(x)
# for y in book_price:
#    print(y)


df = pd.DataFrame({'Book Titles': book_title, 'Book Price': book_price})
df.to_excel('books2.xlsx', index=False)
