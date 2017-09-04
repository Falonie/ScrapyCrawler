import requests, re
from lxml import html

url = 'http://www.qichacha.com/firm_bd92b34e390f8f79b2b66e01b3cd011e.html'
main_url = 'http://www.qichacha.com/search?key=%E5%B9%BF%E4%B8%9C%E5%BE%B7%E5%B0%94%E9%A1%BF%E7%A3%81%E8%83%BD%E7%83%AD%E6%B0%B4%E5%99%A8%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'
mail_url2 = 'http://www.qichacha.com/search?key=%E5%A5%A5%E7%89%B9%E6%9C%97%E7%94%B5%E5%99%A8%EF%BC%88%E5%B9%BF%E5%B7%9E%EF%BC%89%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
cookies = {
    'Cookie': 'acw_tc=AQAAAPerD2dCPA4AoPycy6JDPEBIZosg; UM_distinctid=15e4b0324083dd-08767f64a8da92-3976045e-13c680-15e4b032409954; hasShow=1; _uab_collina=150449705636401992300154; _umdata=0823A424438F76ABFA06070C74C0BA6B29AEC944C4ABFA8C9298B5BBB334427F3DFBD6DC0FCA2DD4CD43AD3E795C914C1C86FC023D04F74A85CA12831DC25A62; PHPSESSID=c0g7usjik1ea9rmp327vjfjud4; zg_did=%7B%22did%22%3A%20%2215e4b0325ba5b-018c65b33a103c-3976045e-13c680-15e4b0325bb713%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201504504840830%2C%22updated%22%3A%201504504840838%2C%22info%22%3A%201504497051072%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22eec241ef4431df98337f2759c6cd7538%22%7D; CNZZDATA1254842228=569286993-1504492656-%7C1504503456'}
response = requests.get(url=main_url, headers=headers, cookies=cookies).text
# print(response)
selector = html.fromstring(response)
# for i in selector.xpath('//*[@id="Cominfo"]/table/tbody/tr[1]/td[1]/text()'):
#     print(i)
href = selector.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/@href')[0]
print(href)
match_obj = re.match('.*?([\w]{10,})', href)
# if match_obj:
#     print(match_obj.group())
# if re.match('^_[]]')
pattern = re.compile(r'[\w]+')
# a=pattern.match(href,6,50)
# if a:
#     print(a.group())
# b=re.match('[\w]+',href)
# if b:
#     print(b.group())
a = re.split(r'[_.]', href)
print(a)

selector2 = html.fromstring(requests.get(url=mail_url2, headers=headers, cookies=cookies).text)
href2 = selector2.xpath('//*[@id="searchlist"]/table[1]/tbody/tr[1]/td[2]/a/@href')[0]
print(href2)
print(re.split(r'[_.]', href2)[1])

with open('/media/salesmind/Other/OTMS/qichacha_all_dimensions_test.txt', 'r') as f:
    for i, line in enumerate(f.readlines(), 1):
        print(i, line.strip())