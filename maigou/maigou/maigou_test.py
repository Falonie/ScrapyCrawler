import requests, re
from lxml import html

url = 'http://www.maigoo.com/maigoocms/special/ztjiaju/064deweier.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
cookies = {
    'Cookie': 'PHPSESSID=euemij4ogb5s875tpkbh99jvv6; uip=52c0cca45e1aca890eb4fbef2e69e90a; f=brand; mgtoken=mg_40129765'}
session = requests.session()
response = session.get(url=url, headers=headers, cookies=cookies).text
# print(response)
selector = html.fromstring(response)
# for i, item in enumerate(selector.xpath('//div[@class="bottminfo_weixin"]/ul[@class="info col3"]/li'), 1):
#     name = item.xpath('text()|b/text()|a/text()|b/font/text()')
# print(name)
# print(selector.xpath('//div[@class="bottminfo_weixin"]/ul[@class="info col3"]/li[5]/script/text()'))

r = session.get(
    # url='http://10.maigoo.com/search/?catid=3054&areaid=2769&action=ajax&getac=brand&page=2',
    url='http://10.maigoo.com/search/?catid=3054&areaid=2769&action=ajax&getac=brand&page=2',
    headers=headers, cookies=cookies).text
# print(r)
# sel = html.fromstring(r)
# for i in sel.xpath('//div[@class="b-brand-nlist hoverdetail"]/ul/li/div[2]/div[1]/a/@href'):
#     # print(i)
#     pass
# print(r)
pattern = re.compile('<a class="dhidden" href="(.*?)" target="_blank">(.*?)</a>(.*?)<span')
for i in pattern.findall(r):
    print(i)
    pass

pattern2 = re.compile(r'<div class="dhidden">(.*?)')
for i in pattern2.findall(r):
    # print(i)
    pass
pattern3 = re.compile(r'')
# for i in sel.xpath('//div[@class="b-brand-nlist hoverdetail"]/ul/li/div[@class="detail"]/div[@class="td3"]/div/div[1]/text()'):
#     # print(i)
#     pass

r1 = session.get(url='http://www.maigoo.com/brand/7869.html', headers=headers, cookies=cookies).text
sel1 = html.fromstring(r1)
# # print(r1)
# for item in sel1.xpath('//ul[@class="info col3 noweixin"]/li[position()<6]'):
#     n = item.xpath('text()|b/font/text()|a/text()')
#     a, b = ''.join(str(i).strip().replace('\n', '') for i in n).split('：')
#     # h=re.findall(r'get=\\"_blank\\">(.*?)</a>',n)
#     # m = item.xpath('descendant::text()')
#     # print(a, b)
#
# # for a in sel1.xpath('//*[@id="leftlayout"]/div[3]/div[1]/div[1]/div[3]/ul/li[5]/a/@href'):
# #     print(a)

for item in sel1.xpath('//ul[@class="info fr"]/li[position()>1]'):
    a, b = ''.join(str(i).strip() for i in item.xpath('text()|a/text()')).split('：')
    # print(a, b)
    pass

# for item in sel1.xpath('//ul[@class="license"]/li'):
#     # a,b=''.join(str(i).strip() for i in item.xpath('text()|a/text()')).split('：')
#     # print(a,b)
#     pass
#
brief = sel1.xpath('//div[@class="introduce"]/div[@class="desc"]/p/text()')
# a = item.xpath('text()|a/text()')
brief = re.sub(r'[\n\r ]', '', ''.join(str(i).strip().replace('\n', '') for i in brief))
print(brief)
# pass

for item in sel1.xpath('//ul[@class="info fr"]/li[@class="name"]'):
    # print(item.xpath('text()'))
    pass