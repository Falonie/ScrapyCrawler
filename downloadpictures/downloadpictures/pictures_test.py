import requests
from lxml import html

url = 'https://stocksnap.io/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
cookies = {
    'cookie': '__cfduid=d4fee6dd956d72919cb6b75a296ff72b41502855146; _csrf=FjmMOj5e1Qchip_odUiKjt_i; _ga=GA1.2.1798702046.1502855151; _gid=GA1.2.1583145762.1502855151; _gat=1; _omappvp=true; _omappvs=true'}
response = requests.get(url=url, headers=headers, cookies=cookies).text
sel = html.fromstring(response)
# print(response)
for i in sel.xpath('//div[@id="main"]/a/img/@src'):
    print(i)