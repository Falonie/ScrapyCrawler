import requests
from lxml import html

with open('E:\约克法修\APP.txt', 'r') as f:
    base_url = 'http://www.wandoujia.com/search?key={}&source='
    # for line in f.readlines():
    #     # base_url='http://www.wandoujia.com/search?key={}&source='
    #     print(base_url.format(line.strip()))
    # print(f.readlines())
    start_urls = [base_url.format(i.strip()) for i in f.readlines()]
    # print(start_urls)

url = 'http://www.wandoujia.com/search?key=%E4%BA%91%E6%8A%95%E6%B1%87&source='
response = requests.get(url=url).text
# print(response)
sel = html.fromstring(response)
for item in sel.xpath('//li[@class="search-item search-searchitems"]/div[@class="app-desc"]'):
    product_name = item.xpath('h2/a/text()')[0]
    download = item.xpath('div[@class="meta"]/span/text()')[0]
    # print(product_name, download)

for i in sel.xpath('//li[@class="search-item search-searchitems"][1]/div[@class="app-desc"]/h2/a/text()'):
    print(i)