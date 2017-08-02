import requests,re
from lxml import html

url='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=%E5%A4%96%E8%B4%B8%E7%94%B5%E5%95%86&isadv=0&sg=5c6fce89e325407a84e8d43aca6804cc&p=1'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
cookies={'Cookie':'dywez=95841923.1501233653.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; LastCity=%e4%b8%8a%e6%b5%b7; LastCity%5Fid=538; JSSearchModel=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1501233653; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1501551680; BLACKSTRIP=yes; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c%e9%a4%90%e8%a1%a5%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e5%8c%85%e4%bd%8f%7c%e5%8c%85%e5%90%83%7c%e6%88%bf%e8%a1%a5%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4; LastSearchHistory=%7b%22Id%22%3a%226ef7e3f0-954d-4d56-9bf2-a9625193f1d1%22%2c%22Name%22%3a%22%e5%a4%96%e8%b4%b8%e7%94%b5%e5%95%86+%2b+%e4%b8%8a%e6%b5%b7%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e4%25b8%258a%25e6%25b5%25b7%26kw%3d%25e5%25a4%2596%25e8%25b4%25b8%25e7%2594%25b5%25e5%2595%2586%26isadv%3d0%26sg%3d5c6fce89e325407a84e8d43aca6804cc%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1501552485016%2b0800)%5c%2f%22%7d; dywea=95841923.765757106191005700.1501233653.1501233653.1501551268.2; dywec=95841923; __utma=269921210.1653021763.1501233653.1501233653.1501551270.2; __utmc=269921210; __utmz=269921210.1501233653.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0'}
response=requests.get(url=url,headers=headers,cookies=cookies).text
sel=html.fromstring(response)
# item=sel.xpath('//div[@class="newlist_wrap fl"]/div[@class="newlist_list"]/div[@class="newlist_list_content"]/table[position()>1]/tbody/tr[1]')
# for i in item:
#     position = i.xpath('td[1]/div/a/text()')
    # print(position)
# for j in sel.xpath('//div[@class="newlist_list_content"]/table[position()>1]/tbody/tr[1]/td[@class="zwmc"]/div/a/text()'):
#     print(j)

# for m in sel.xpath('//div[@class="newlist_wrap fl和热风"]/div[@class="newlist_list"]/div[@class="newlist_list_content"]/table[@class="newlist"]/tbody/tr[1]/td[1]/div/a/text()'):
#     print(m)

# for m in sel.xpath('//div[@id="newlist_list_content_table"]/table[position()>1]/tbody[1]/tr[1]/td[1]/div[1]/a[1]/text()'):
#     print(m)

# for i in sel.xpath('//div[@id="newlist_list_content_table"]/table[position()>1]/tbody[1]/tr[1]/td[@class="gxsj"]/span/text()'):
# for i in sel.xpath('//div[@class="newlist_wrap fl"]/div[@id="newlist_list_div"]/div[@id="newlist_list_content_table"]/table[@class="newlist"]/tbody[1]/tr[1]/td[@class="gxsj"]/span/text()'):
#     print(i)

# for n in re.findall('target="_blank">(.*?)</a>',response):
#     print(n)
# '//*[@id="newlist_list_content_table"]/table[2]/tbody/tr[1]/td[1]/div/a'

pattern=re.compile(r'<a style=.*?target="_blank">(.*?)</a>')
pattern2=re.compile(r'<td class="gsmc"><a.*?target="_blank">(.*?)</a> ')
pattern3=re.compile(r'<td class="gxsj"><span>(.*?)</span><')
pattern4=re.compile(r' <td class="zwyx">(.*?)</td>')
pattern5=re.compile(r'<a style="font-weight:.*?href="http://(.*?)" target="_blank">')
job=pattern.findall(response)
for i,m in enumerate(pattern5.findall(response),1):
    position = re.sub(r'[</b>]', '', m)
    # print(i,position)
# print(job.__len__())
#print(type(response))
#print(response)

url1='http://jobs.zhaopin.com/597974523250007.htm'
selector=html.fromstring(requests.get(url=url1,headers=headers,cookies=cookies).text)
item=selector.xpath('//div[@class="terminalpage-left"]/ul[@class="terminal-ul clearfix"]/li')
for i in item:
    s=i.xpath('strong/text()|strong/a/text()|strong/span/text()')
    s1=i.xpath('span/text()')
    # print(s1,s)
print(type(requests.get(url=url,headers=headers,cookies=cookies).text))

url3='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E&kw=%E4%BA%9A%E9%A9%AC%E9%80%8A%E8%BF%90%E8%90%A5&sm=0&p=1'
selector=html.fromstring(requests.get(url=url3,headers=headers,cookies=cookies).text)
for i in selector.xpath('//div[@class="pagesDown"]/ul/li[@class="pagesDown-pos"]/a/@href'):
    print(i)