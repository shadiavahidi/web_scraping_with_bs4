from bs4 import BeautifulSoup
import requests
import pandas as pd

# first part
page = requests.get('https://books.toscrape.com/')
print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

book_name = soup.find(name='article', class_='product_pod')
book_name_text = book_name.get_text()
book_name_ = book_name.find(name='h3').find('a')['title']
print(book_name_)

book_price = soup.find_all('p', class_='price_color')
print(len(book_price))
for price in book_price:
    book_price_ = price.get_text('p')[1::]

    print(book_price_)

book_select = soup.select_one('.product_pod   h3').select_one('a')['title']
print(book_select)

# second part

book_price = soup.find('p', class_='price_color').get_text('p')[2::]
print(book_price)

book_star = soup.find('p')
book_star_ = book_star['class'][1]
print(book_star_)

url = 'https://books.toscrape.com/'
book_address = book_name.find(name='h3').find('a')['href']
book_url = (url + book_address)
print(book_url)

#  third part
book_name = soup.find_all(name='article', class_='product_pod')
book_name_ = []
for book in book_name:
    book_text = book.get_text()
    name = book.find('h3').find('a')['title']
    book_name_.append(name)

# print(book_name_)

book_price_ = []
book_price = soup.find_all('p', class_='price_color')
print(len(book_price))
for price in book_price:
    price_of_book = price.get_text('p')[2::]
    book_price_.append(price_of_book)

# print(book_price_)

book_url = soup.find_all('article', class_='product_pod')
book_address = []
for address in book_url:
    b_add = address.get_text()
    b_url = address.find('h3').find('a')['href']
    b_address = url + b_url
    book_address.append(b_address)

# print(book_address)


book_star = soup.find_all('article', class_='product_pod')
book_star_ = []
for star in book_star:
    stars = star.get_text()
    str = star.find('p')['class'][1]
    book_star_.append(str)

# print(book_star_)


info_book = list(zip(book_name_, book_price_, book_star_, book_address))

df = pd.DataFrame(info_book,
                  columns=['Name', 'Price', 'Star', 'Link'])
print(df)

df.to_csv('info_book', index=False)
