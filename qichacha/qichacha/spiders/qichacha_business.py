import scrapy, re
from scrapy.http import Request
from ..items import QichachaItem
from selenium import webdriver


class QichachaSpider(scrapy.Spider):
    name = 'qichacha3'
    # start_urls = [
    #     'http://www.qichacha.com/search?key=%E5%B9%BF%E4%B8%9C%E5%BE%B7%E5%B0%94%E9%A1%BF%E7%A3%81%E8%83%BD%E7%83%AD%E6%B0%B4%E5%99%A8%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8']
    start_urls = [
        'http://www.qichacha.com/search?key=%E5%B9%BF%E5%B7%9E%E5%B8%82%E8%81%94%E4%B8%8A%E7%82%89%E5%85%B7%E8%B4%B8%E6%98%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8']

    # def __init__(self, *args, **kwargs):
    #     self.driver = webdriver.PhantomJS(executable_path=r'E:\files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    #     super(QichachaSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # print(type(response), type(str(response)), type(response.body.decode('utf-8')))
        sel = scrapy.Selector(response)
        basic_url = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=base'
        business = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=run'
        company_name = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/a/descendant::text()').extract()
        company_name = ''.join(str(i).strip() for i in company_name)
        email = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[2]/span/text()').extract_first('N/A')
        legal_representative = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[1]/a/text()').extract_first('N/A')
        telephone = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[2]/text()').extract_first('N/A')
        telephone = ''.join(str(i).strip() for i in telephone)
        href = sel.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/@href').extract_first()
        unique_key = re.split(r'[_.]', href)[1]
        a = {'company_name': company_name, 'legal_representative': legal_representative, 'email': email,
             'telephone': telephone}
        # print(company_name, href, unique_key)
        yield scrapy.Request(url=business.format(unique_key, company_name), meta={'item': a},
                             callback=self.parse_business)

    def parse_business(self, response):
        qichacha = QichachaItem()
        qichacha = response.meta.get('item', '')
        sel = scrapy.Selector(response)
        r = response.body.decode('utf-8')
        for j, i in enumerate(sel.xpath('//*[@id="joblist"]/table/tbody/tr[position()>1]'), 1):
            joblist = i.xpath('td/text()').extract()
            # print('recruit{}'.format(j), ''.join(str(i).strip() for i in joblist))
            a = 'recruit_member{}'.format(j)
            b = ''.join(str(i).strip() for i in joblist)
            qichacha[a] = b
        for i in sel.xpath('//*[@id="V3_cwzl"]/table/tr'):
            title = i.xpath('td[position()=1 or position()=3]/text()').extract()
            content = i.xpath('td[position()=2 or position()=4]/text()').extract()
            # print(title,content)
            for t, c in zip(title, content):
                a = str(t).strip().replace('：', '')
                b = str(c).strip()
                # print(a, b)
                qichacha[a] = b
        yield qichacha