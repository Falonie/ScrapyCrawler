import requests, re, pymongo, time
from lxml import html

url = 'https://www.itjuzi.com/company?fund_status=15&page=2'
url2 = 'https://www.itjuzi.com/company/32373471'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Mobile Safari/537.36'}
collection=pymongo.MongoClient(host='localhost',port=27017)['Falonie']['itjuzi']



d={"ERRORCODE":"0","RESULT":{"wanIp":"125.121.118.219","proxyport":"37828"}}
ip=d.get('RESULT')
ip_address='http://'+ip.get('wanIp')+':'+ip.get('proxyport')
proxy={'https':ip_address}
def page_url():
    base_url = 'https://www.itjuzi.com/company?fund_status=16&page={}'
    for _ in range(1, 1000):
        url = base_url.format(_)
        print(proxy)
        yield url


def parse_page(url):
    session = requests.session()
    r = session.get(url=url, headers=headers, cookies=cookies,proxies=proxy).text
    selector = html.fromstring(r)
    url_list = []
    for _ in selector.xpath('//ul[@class="list-main-icnset company-list-ul"]/li'):
        href = _.xpath('div[@class="cell maincell"]/div[@class="title"]/a/@href')[0]
        url_list.append(href)
        product = _.xpath('div[@class="cell maincell"]/div[@class="title"]/a/span[1]/text()')
        location = _.xpath('i[@class="cell place"]/text()')
        location = ''.join(str(i).strip() for i in location)
    return url_list


def page_details(url2):
    session = requests.session()
    r = session.get(url2, headers=headers, cookies=cookies,proxies=proxy).text
    selector = html.fromstring(r)
    item = {}
    for _ in selector.xpath('//div[@class="picinfo"]'):
        short_name = _.xpath('div[@class="line-title"]/span[@class="title"]/h1/@data-name')
        short_name = ''.join(str(i).strip() for i in short_name)
        full_name = _.xpath('div[@class="line-title"]/span[@class="title"]/h1/@data-fullname')
        full_name = ''.join(str(i).strip() for i in full_name)
        slogan = _.xpath('div[2]/h2/text()')
        slogan = ''.join(str(i).strip() for i in slogan)
        link = _.xpath('div[@class="link-line"]/a/@href')
        link = ''.join(str(i) for i in link)
        # print(short_name, full_name, slogan)
        item.update({'short_name': short_name, 'full_name': full_name, 'slogan': slogan, 'link': link})
    # name=selector.xpath('//div[@class="line-title"]/span[@class="title"]/h1')
    for _ in selector.xpath('//div[@class="block-inc-info on-edit-hide"]'):
        brief_intro = _.xpath(
            'div[@class="block" and position()=1]/div/descendant::text()|div[@class="block"]/div[@class="summary"]/text()')
        brief_intro = ''.join(str(i).strip() for i in brief_intro)
        establish_time = _.xpath(
            'div[@class="block" and position()=2]/div/h3[1]/descendant::text()|div[@class="block"]/div/h3[1]/descendant::text()')
        establish_time = ''.join(str(i).strip() for i in establish_time)
        scale = _.xpath('div[@class="block"]/div/h3[2]/descendant::text()')
        scale = ''.join(str(i).strip() for i in scale)
        # print(brief_intro, establish_time, scale)
        item.update({'brief_intro': brief_intro, 'establish_time': establish_time, 'scale': scale})
    for _ in selector.xpath('//ul[@class="contact-list limited-itemnum"]/li/ul'):
        phone = _.xpath('li[contains(i/@class,"fa icon icon-phone-o")]/span/text()')
        phone = ''.join(str(i) for i in phone)
        mail = _.xpath('li[contains(i/@class,"fa icon icon-email-o")]/span/text()')
        mail = ''.join(str(i) for i in mail)
        location = _.xpath('li[contains(i/@class,"fa icon icon-address-o")]/span/text()')
        location = ''.join(str(i) for i in location)
        # print({'phone': phone, 'mail': mail, 'location': location})
        item.update({'phone': phone, 'mail': mail, 'location': location})
    for _ in selector.xpath('//table[@class="list-round-v2"]/tbody/tr'):
        ficancing_time = _.xpath('td[1]/span/text()')
        ficancing_time = ''.join(str(i).strip() for i in ficancing_time)
        rounds = _.xpath('td[2]/span/a/text()')
        rounds = ''.join(str(i).strip() for i in rounds)
        leadership = selector.xpath('//li[@class="feedback-btn-parent first-letter-box-4js"]/div/descendant::text()')
        leadership = ''.join(str(i).strip() for i in leadership)
        # print(ficancing_time, rounds, leadership)
        item.update({'financing_time': ficancing_time, 'rounds': rounds, 'leadership': leadership})
    collection.insert(item)
    return item


if __name__ == '__main__':
    # print(parse_page(url))
    # print(page_details('https://www.itjuzi.com/company/32373471'))
    for _ in page_url():
        print(_)
        for i in parse_page(url):
            print(page_details(i))
            time.sleep(5)
        time.sleep(7)
    pass

# print(selector.xpath('//div[@class="block-inc-info on-edit-hide"]/div[@class="block" and position()=1]/div/descendant::text()'))
# print(selector.xpath('//div[@class="block-inc-info on-edit-hide"]/div[@class="block"]/div[@class="summary"]/text()'))
