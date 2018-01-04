import requests, re
from lxml import html

url = 'http://company.jctrans.com/Company/List/0-0-%E6%B7%84%E5%8D%9A---0/1.html'
cookies = {
    'Cookie': 'LiveWSLHF61175281=1505179258324498117366; LiveWSLHF61175281sessionid=1505179258324498117366; NLHF61175281fistvisitetime=1505179258537; NLHF61175281visitecounts=1; Hm_lvt_c5bb7feca9c1ba5a1d9aac9844e94118=1505179260; Hm_lpvt_c5bb7feca9c1ba5a1d9aac9844e94118=1505179260; Hm_lvt_19c3fd26632e830e7d7906b26665d0ae=1505179260; Hm_lpvt_19c3fd26632e830e7d7906b26665d0ae=1505179260; __utmt=1; __utma=152505899.245658831.1505179260.1505179260.1505179260.1; __utmb=152505899.1.10.1505179260; __utmc=152505899; __utmz=152505899.1505179260.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); safedog-flow-item=7367D5CFCE961636CA28C48E150A5416; NLHF61175281lastvisitetime=1505179278270; NLHF61175281visitepages=2; NLHF61175281lastinvite=1505179519702'}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
response = requests.get(url=url, headers=headers, cookies=cookies).text
# print(response)
sel = html.fromstring(response)
# print(sel.xpath('//div[@class="table_cont"]/ul/li[2]/div/a/@title'))
# print(sel.xpath('//*[@id="company_list"]/div[3]/div[3]/ul[5]/li[2]/div/a/@title'))
# print(sel.xpath('//div[@class="com_name"]/a/@title'))
for i in sel.xpath('//div[@class="com_name"]'):
    company = i.xpath('a/@title')
    href = i.xpath('a/@href')
    c = i.xpath('p[@class="link_person"]/descendant::text()')
    contact = ''.join(str(i).strip().replace('联系人：', '') for i in c)
    # print(company,href,contact)
url = 'http://shop.jctrans.com/C935AC19-8836-4E77-BB68-17570A68EDDA.html'
r = requests.get(url=url, headers=headers, cookies=cookies).text
# print(r)
selector = html.etree.HTML(r)
for i in selector.xpath('//ul[@class="fei"]/li'):
    a = i.xpath('span[@class="name"]/text()')
    b = i.xpath('b/text()|span[2]/text()|text()')
    print(a, b)
print(''.join(str(i).strip() for i in selector.xpath('//div[@class="contxt"]/text()')))