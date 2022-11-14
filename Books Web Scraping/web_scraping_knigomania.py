from bs4 import BeautifulSoup
import requests
import pandas as pd

next_page_available = True
page = 1  # Starting page

enter_book_title = input("Enter Book title: ")

book_title = []
book_price = []

# Continues searching and adding items to the lists until the next page symbol(>) is no longer visible.
while next_page_available:

    URL = "https://knigomania.bg/catalogsearch/result/?p=" + str(page) + "&q=" + str(enter_book_title).replace(" ", "+")

    req = requests.get(URL)
    soup = BeautifulSoup(req.text, "html.parser")

    # Scans the page looking for results and adds them to the lists.
    for element in soup.findAll(attrs={'class': 'item product product-item'}):
        name = element.find('a', attrs={'class': 'product-item-link'})
        price = element.find('span', attrs={'class': 'price-container price-final_price tax weee'})
        book_title.append(name.text)
        book_price.append(price.text)

    # Checks if the next page symbol(>) is no longer visible on the page.
    if soup.find("li", class_='item pages-item-next') is None:
        next_page_available = False

    page += 1

# Creates an Excel file containing all the books and prices that were scraped.
df = pd.DataFrame({'Book Titles': book_title, 'Book Price': book_price})
df.to_excel('KnigomaniaBooks.xlsx', index=False)
