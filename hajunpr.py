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

URL = "https://chemistry.illinois.edu/academics/course-catalog"
webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "lxml")

ls = []

for ele in soup.find_all('div', {'class':'views-field views-field-nothing-1'}):
    name = ele.find('h2').text
    ls.append(f"{name}")

for i in ls:
    print(i)

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