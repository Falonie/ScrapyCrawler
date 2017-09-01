import requests, csv, re
from lxml import html

url = 'http://cn.made-in-china.com/showroom/15919915597-companyinfo.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url=url, headers=headers).text
selector = html.fromstring(response)
# print(response)
# brief=selector.xpath('//div[@class="boxCont company-blk"]/div[1]/p/text()')
# print(brief)
# for j in selector.xpath('//div[@class="box"]/div/table/tr/th/text()'):
#     print(str(j).strip())
for i in selector.xpath('//div[@class="box"]/div/table/tr'):
    a = i.xpath('th/text()')
    b = i.xpath('td/text()|td/label/text()')
    a1 = str(a[0]).strip()
    b1 = ''.join(str(i).strip() for i in b)
    c = i.xpath('th/text()|td/text()|td/label/text()')
    c1 = ''.join(str(i).strip() for i in c)
    # print(c1)
    # with open('file.csv','a+',newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(c1)
    # writer.writerow((a1, b1))

item = selector.xpath(
    '//div[@class="box"]/div/table/tr/th/text()|//div[@class="box"]/div/table/tr/td/text()|//div[@class="box"]/div/table/tr/td/label/text()')
# print(''.join(str(i).strip() for i in item))

url1 = 'http://cn.made-in-china.com/showroom/guijiaoshuiping'
r = requests.get(url=url1, headers=headers).text
sel = html.fromstring(r)
brief = sel.xpath('//div[@class="boxCont boxText"]/p[@class="companyInf"]/text()')
brief1 = re.sub(r'[\u3000\r\t\n ]', '', ''.join(str(i).strip() for i in brief))
brief2 = brief[-2]
print(brief1)