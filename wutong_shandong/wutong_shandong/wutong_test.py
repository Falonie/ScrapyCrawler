import requests
from lxml import html

url='http://www.chinawutong.com/224/1305183.html'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
cookies={'Cookie':'IESESSION=alive; wtluck=201710-16%2C0; pgv_pvi=3043430400; pgv_si=s1742296064; tencentSig=9230836736; ASP.NET_SessionId=gpju5wyw3ixcwx55lgved455; SESSION_COOKIE=2; 629110=cishu=0&time=2017/10/16 9:54:29; 1926847=cishu=0&time=2017/10/16 9:54:36; _qddamta_4000105656=3-0; Hm_lvt_b056f6db54a055cf5bfde997b9ed913f=1508118868; Hm_lpvt_b056f6db54a055cf5bfde997b9ed913f=1508123557; _qddaz=QD.g556zd.png5n3.j8tj1abu; _qdda=3-1.1; _qddab=3-6ggr9.j8tldnb4'}
response=requests.get(url=url,headers=headers,cookies=cookies).text
sel=html.fromstring(response)
# print(response)
print(sel.xpath('//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div[2]/table/tbody/tr/td/ul[1]/li[2]/span[2]/text()'))
print(sel.xpath('//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div[2]/table/tbody/tr/td/h2/a/@href')[0])
print(sel.xpath('//*[@id="aspnetForm"]/div[10]/div/div[1]/div[3]/div[2]/img/@src'))

url2='http://13953395876.chinawutong.com/'
s=html.fromstring(requests.get(url=url2,headers=headers,cookies=cookies).text)
print(s.xpath('//*[@id="aspnetForm"]/div[10]/div[2]/div[1]/div[2]/table/tr/td/ul[2]/li[2]/img/text()'))
'//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div/table/tbody/tr/td/ul[1]/li/span[2]'
'//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div/table/tbody/tr/td/ul[1]/li/span[2]'
print(s.xpath('//ul[@class="wxtlx"]/li[2]/img/@src'))
print(s.xpath('//ul[@class="wxtlx"]/li[3]/img/@src'))
url3='http://www.chinawutong.com/224/393768.html'
s3=html.fromstring(requests.get(url=url3,headers=headers,cookies=cookies).text)
print(s3.xpath('//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div/table/tbody/tr/td/ul[1]/li/span[2]/text()'))

url4='http://www.chinawutong.com/224/1468863.html'
s=html.fromstring(requests.get(url=url4,headers=headers,cookies=cookies).text)
print(s.xpath('//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div[2]/table/tbody/tr/td/h2/a/@href'))
'//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div[2]/table/tbody/tr/td/h2/a/@href'
'//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div[2]/table/tbody/tr/td/h2/a/@href'