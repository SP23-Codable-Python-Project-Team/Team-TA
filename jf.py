# from bs4 import BeautifulSoup
# import requests

# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
# # }

# url = "https://www.amazon.com/Temtop-Professional-0-3%CE%BCm-10%CE%BCm-Particulate-Certified/dp/B087MZ93W2/ref=sr_1_1_sspa?crid=11VCURDTZFYKL&keywords=pms+particle+counter&qid=1677280436&sprefix=pms+particle+counter%2Caps%2C104&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.765d4786-5719-48b9-b588-eab9385652d5&psc=1&smid=AON8DME687K1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMThGNUlLM1dXOEQ3JmVuY3J5cHRlZElkPUEwNjU4MTkzMkhRUVJISUsyR0o3MiZlbmNyeXB0ZWRBZElkPUEwMDI5MjMxMVFGSFAxN0xLWlhXSSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

# result = requests.get(url)

# print(result.text)
# # doc = BeautifulSoup(result.content, "html.parser")

# # results = doc.find(id = 'ResultContainer')
# # title = results.find_all('h2', class_='')
# # print(doc.prettify())
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

r = requests.get("https://www.amazon.com/Temtop-Professional-0-3%CE%BCm-10%CE%BCm-Particulate-Certified/dp/B087MZ93W2/ref=sr_1_1_sspa?crid=11VCURDTZFYKL&keywords=pms+particle+counter&qid=1677280436&sprefix=pms+particle+counter%2Caps%2C104&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.765d4786-5719-48b9-b588-eab9385652d5&psc=1&smid=AON8DME687K1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMThGNUlLM1dXOEQ3JmVuY3J5cHRlZElkPUEwNjU4MTkzMkhRUVJISUsyR0o3MiZlbmNyeXB0ZWRBZElkPUEwMDI5MjMxMVFGSFAxN0xLWlhXSSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=", headers=headers)
c = r.text

print(c)