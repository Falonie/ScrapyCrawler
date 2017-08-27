import requests, re
from lxml import html

url = 'http://www.zhongchoujia.com/platform/?prid=20&fa=-1&pni=-1&dt=-1&pt=-1&pname=&rank=-1'
url1 = 'http://www.zhongchoujia.com/platform/yunchou/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
cookies = {
    'Cookie': 'ASP.NET_SessionId=cxttlti10wa4wmulcllgizo4; UM_distinctid=15e0b4001e11b1-04686fd598c7c1-474f0820-13c680-15e0b4001e2375; Qs_lvt_44311=1503427299; CNZZDATA1254120327=1447214523-1503455331-%7C1503455331; Qs_pv_44311=2362235615177559600%2C2108800966084530400%2C2976757068144369000; Hm_lvt_a20e495a4331ceb1d7ebf363198d7a48=1503427300; Hm_lpvt_a20e495a4331ceb1d7ebf363198d7a48=1503427311'}
session = requests.session()
response = session.get(url=url, headers=headers, cookies=cookies).text
selector = html.fromstring(response)
# print(response)
for href in selector.xpath('//ul[@class="platformlist"]/li[@class="platformItem pbox"]/div[1]/div[1]/a/@href'):
    # print(href)
    pass
# print(selector.xpath('//div[@class="m-t-20 paging page"]/pre/a[last()-1]/@href'))

sel = html.fromstring(session.get(url=url1, headers=headers, cookies=cookies).text)
for item in sel.xpath('//div[@class="basic-right"]/ul[@class="basic-detailul"]/li'):
    # name=re.sub(r'[\r\n ],'',''.join(str(i).strip().replace(' ','') for i in item.xpath('span[2]/descendant::text()')))
    name = ''.join(str(i).strip().replace(' ', '') for i in item.xpath('span[2]/descendant::text()'))
    a1, a2 = re.sub(r'[\r\n-]', '', name).split('：')
    # print(a1, a2)
    # print(name)

brief = sel.xpath('//div[@class="basic-right"]/div[@class="basic-Content"]/text()')
# print(re.sub(r'[\r\n ]', '', ''.join(str(i) for i in brief)))

for item in sel.xpath('//div[@class="pfd-archives pfd-item "]/div[1]/div[@class="archivesinfo"]/p'):
    # j = ''.join(str(i) for i in item.xpath('text()'))
    # j = re.sub(r'[\r\n ]', '', j)
    # print(j)
    pass

# for introduction in sel.xpath('//div[@class="pfd-archives pfd-item "]/div[2]/div/p/descendant::text()'):
#     print(introduction)
introduction = sel.xpath('//div[@class="pfd-archives pfd-item "]/div[2]/div/p/descendant::text()')
# print(''.join(str(i).strip() for i in introduction))

r = session.get(
    url='http://www.zhongchoujia.com/platform/default.aspx?pi=1&prid=20&fa=-1&pni=-1&dt=-1&pt=-1&pname=&rank=-1',
    headers=headers, cookies=cookies).text
sel1 = html.fromstring(r)
# for title in sel1.xpath('//ul[@class="platformlist"]/li[@class="platformItem pbox"]/div[1]/div[1]/a/text()'):
for i in sel1.xpath('//div[@class="title"]/a'):
    title = i.xpath('text()')[0]
    href = i.xpath('@href')[0]
    print(href, title)