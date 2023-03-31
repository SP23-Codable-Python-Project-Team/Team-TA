import requests
from bs4 import BeautifulSoup

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

URL = "https://www.americancampus.com/student-apartments/il/champaign/campustown-rentals/floor-plans#/"
webpage = requests.get(URL, headers=HEADERS)

# content = """<section data-v-f69a7a02 aria-label="Property listing">"""
# content = """<div data-v-f69a7a02 class="grid">"""

# soup = BeautifulSoup(content, 'html.parser')

webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "lxml")
# print(soup)
ls = []

# BeautifulSoup('<div data-v-38788375 data-v-07b96579 class="rating score orange">7.5</div>').find('div', attrs={'class': 'rating score orange'}).text

# BeautifulSoup('div data-v-a57b4422 data-v-f69a7a02 class="property"></div>').find('h6', attrs={'class':'property-price'}).text

BeautifulSoup('h2 data-v-a57b4422="" class="property-title" style="color: rgb(19, 41, 75);">101 E. Green - 2 Bed - 1 Bath A</h2>').find('h2', attrs={'style':'color: rgb(19, 41, 75);'}).text

# for ele in soup.find_all('section', {'data-v-f69a7a02 aria-label':'Propety listing'}):
#     print(ele)
#     name = ele.find('div', attrs={'data-v-a57b4422 data-v-f69a7a02 class':'property'}).text
#     ls.append(f"{name}")

# for i in ls:
#     print(i)