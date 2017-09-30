import requests, re
from lxml import html,etree
from itertools import zip_longest

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
cookies = {
    'Cookie': 'JSESSIONID=B1FC1ADE2AA88889AC5655E0A4B317EA.tomcat1; Hm_lvt_1eb7d1072a92f7ee3d7efa0ce15c8f4b=1506482192; Hm_lpvt_1eb7d1072a92f7ee3d7efa0ce15c8f4b=1506482198'}

for i in range(1, 10):
    data = {'page': i}
    # print(data)
    # data={'page':3}
    url = 'http://www.maidongpin.com/pc/list/supplylistPage'
    response = requests.get(url=url, headers=headers, cookies=cookies).text
    r = requests.post(url=url, data=data, headers=headers, cookies=cookies).text
    # print(response)
    sel = html.fromstring(r)
    # print(sel.xpath('//div[@class="grid_1200"]/ul[@class="list_prd"]/li/div[2]/span[1]/text()'))
    for i in sel.xpath('//div[@class="grid_1200"]/ul[@class="list_prd"]/li'):
        href = i.xpath('div[1]/a/@href')
        name = i.xpath('div[2]/span[1]/text()')
        # print(name, href)

        # print([{'page':i for i in range(1,11)}])
        # print([dict(page=i) for i in range(1,11)])
r=requests.post(url='http://www.maidongpin.com/pc/list/supplylistPage',headers=headers,cookies=cookies).text
sel=html.fromstring(r)
print(sel.xpath('//div[@class="float_right"]/ul[@class="page_bd"]/li[last()-1]/@title'))

url2 = 'http://www.maidongpin.com/pc/detail/supplyDetail?supplyId=912636333053337600'
# print(requests.get(url=url2,headers=headers,cookies=cookies).text)
selector = html.fromstring(requests.get(url=url2, headers=headers, cookies=cookies).text)
# print(selector.xpath('//table[@class="detail_table"]/tr/th[2]/text()'))
# for i in selector.xpath('//table[@class="detail_table"]/tr/th[2]/text()'):
a = selector.xpath('//table[@class="detail_table"]/tr/descendant::text()')
# a=list(filter(lambda x:))
a = [re.sub(r'[\r\t\n\xa0| ]', '', i) for i in a]
a = list(filter(lambda x: len(x) > 1, a))
a = ''.join(a)
print(a.split('：'))
# for i in selector.xpath('//table[@class="detail_table"]/tr/th[position()=2 or position()=4 or position()=6]/text()|//table[@class="detail_table"]/tr/td/text()'):
#     print(i)
for a, b in zip(
        selector.xpath('//table[@class="detail_table"]/tr[1]/th[position()=2 or position()=4 or position()=6]/text()'),
        selector.xpath('//table[@class="detail_table"]/tr[1]/td/text()')):
    print(a, b)
for a, b in zip_longest(
        selector.xpath('//table[@class="detail_table"]/tr[2]/th[position()=2 or position()=4 or position()=6]/text()'),
        selector.xpath('//table[@class="detail_table"]/tr[2]/td/text()')):
    print(a, b)
for i in selector.xpath('//table[@class="detail_table2"]/tr'):
    # a=i.xpath('th/text()')
    # b=i.xpath('td/text()')
    a = re.sub(r'[\r\t\n\xa0 ]', '', i.xpath('th/text()')[0])
    b = re.sub(r'[\r\t\n\xa0 ]', '', ''.join(str(i).strip() for i in i.xpath('td/descendant::text()')))
    # print(a, b)

for i in selector.xpath('//div[@class="detail_right"]/div[@class="business"]/div[@class="top"]/ul/li'):
    a = i.xpath('text()')
    a=re.sub(r'[\xa0 ]','',a[0]).split('：')
    print(a)