from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# webpage = requests.get(URL, headers=HEADERS)

# soup = BeautifulSoup(webpage.content, "lxml")
# print(soup)
# # Outer Tag Object
# title = soup.find("h1", attrs={"data-qa":'product_name'})
# # Inner NavigableString Object
# title_value = title.string
# # Title as a string value
# title_string = title_value.strip()
# # Printing types of values for efficient understanding
# print(type(title))
# print(type(title_value))
# print(type(title_string))
# print()

# # Printing Product Title
# print("Product Title = ", title_string)

# url = 'https://notes.ayushsharma.in/technology'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
            'Accept-Language' : 'en-US,en;q=0.5',
            'Accept-Encoding' : 'gzip', 
            'DNT' : '1', # Do Not Track Request Header 
            'Connection' : 'close'}

URL = "https://jsmliving.com/search-available-units?building=All&available=9&rent%5Bmin%5D=0&rent%5Bmax%5D=4500&sort_bef_combine=field_numerical_address_value_ASC"
webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "lxml")

jsmAddress = []
jsmPrice = []
jsmBedBath = []


for ele in soup.find_all('div', {'class':'field field--name-field-building field--type-entity-reference field--label-hidden field--item'}):
    address = ele.find('a').text
    jsmAddress.append(f"{address}")

# for i in jsmAddress:
#     print(i)


for ele in soup.find_all('div', {'class':'unit__card-description'}):
    price = ele.find('div', {'class':'unit__card-rent'}).text
    jsmPrice.append(f"{price}")

# for i in jsmPrice:
#     print(i)


for ele in soup.find_all('div', {'class':'unit__card-description'}):
    bedBath = ele.find('div', {'class':'unit__card-stats'}).text
    jsmBedBath.append(f"{bedBath}")

# for i in jsmBedBath:
#     print(i)

for i in jsmAddress:
    for j in jsmPrice:
        for k in jsmBedBath:
            print(i)
            print(j)
            print(k)
            break
        break

# # Outer Tag Object
# title = soup.find("h2", attrs={"class":})
# # Inner NavigableString Object
# title_value = title.string
# # Title as a string value
# title_string = title_value.strip()
# # Printing types of values for efficient understanding
# print(type(title))
# print(type(title_value))
# print(type(title_string))
# print()

# # Printing Product Title
# print("Product Title = ", title_string)