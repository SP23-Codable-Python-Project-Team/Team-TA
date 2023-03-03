import requests
from bs4 import BeautifulSoup
import csv
from lxml import etree

HEADERS = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}

# url = "https://ugroupcu.com/property-details/502-e-healey-champaign/"
url = "https://mechse.illinois.edu/"
response = requests.get(url,"html")


#parse response with BS
soup = BeautifulSoup(response.text, 'lxml')

#extract data

ls = []
for ele in soup.find_all('div',{'class':'lower py-4'}):
    title = ele.find('div',{'class':'flex'}).text
    name = ele.find('h2').text
    # ls.append(f"{title}")
    ls.append(f"{name}")

for i in ls:
    print(i)

# webpage = requests.get(url)
# soup = BeautifulSoup(webpage.content, "html.parser")
# dom = etree.HTML(str(soup))
# res = (dom.xpath('//*[@class="col-lg-5"]/text()'))
# print(res)
# for article in res:
#     print(article)
#     print("--------------")