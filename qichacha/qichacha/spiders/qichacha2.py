import scrapy, re
from scrapy.http import Request
from ..items import QichachaItem
from selenium import webdriver


class QichachaSpider(scrapy.Spider):
    name = 'qichacha2'
    # start_urls=['http://www.qichacha.com/company_getinfos?unique=39b2704ef21426edc8b38e47fec017a0&companyname=%E5%B9%BF%E4%B8%9C%E5%BE%B7%E5%B0%94%E9%A1%BF%E7%A3%81%E8%83%BD%E7%83%AD%E6%B0%B4%E5%99%A8%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&tab=base']
    start_urls = [
        'http://www.qichacha.com/search?key=%E5%B9%BF%E4%B8%9C%E5%BE%B7%E5%B0%94%E9%A1%BF%E7%A3%81%E8%83%BD%E7%83%AD%E6%B0%B4%E5%99%A8%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8']

    # def __init__(self, *args, **kwargs):
    #     self.driver = webdriver.PhantomJS(executable_path=r'E:\files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    #     super(QichachaSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        sel = scrapy.Selector(response)
        company_name = sel.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/em/em/text()').extract_first()
        href = sel.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/@href').extract_first()
        unique_key = re.split(r'[_.]', href)[1]
        a = {'company_name': company_name, 'href': href, 'unique_key': unique_key}
        print(company_name, href, unique_key)


"""
    def parse(self, response):
        # print(type(response), type(str(response)), type(response.body.decode('utf-8')))
        sel = scrapy.Selector(response)
        # base_url = 'http://www.qichacha.com/company_getinfos?unique=a78fe9bc4e3cb16f98f769e2ba0695c7&companyname={}&tab=base'
        base_url='http://www.qichacha.com/company_getinfos?unique=39b2704ef21426edc8b38e47fec017a0&companyname={}&tab=base'
        company_name = sel.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/em/em/text()').extract()
        href = sel.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/@href').extract()
        # print(company_name,href)
        for c, h in zip(company_name, href):
            # print(c, h)
            a = {'company_name': c}
            yield scrapy.Request(url=base_url.format(c), meta={'item': a}, callback=self.parse_content)

    def parse_content(self, response):
        qichacha = QichachaItem()
        # print(type(response.body), type(response), type(response.body.decode('utf-8')))
        # print(response.body.decode('utf-8'))
        # self.driver.get(response.url)
        # print(self.driver.page_source)
        qichacha = response.meta.get('item', '')
        sel = scrapy.Selector(response)
        r = response.body.decode('utf-8')
        # title = sel.xpath('//table[@class="m_changeList"]/tr/td[@class="ma_bluebg ma_left"]/text()').extract()
        # info = sel.xpath('//table[@class="m_changeList"]/tr/td[2]/text()|//table[@class="m_changeList"]/tr/td[4]/text()').extract()
        pattern = re.compile(r'<td class="ma_bluebg ma_left".*?>\s*(.*?)\s*</td> ')
        title = pattern.findall(r)
        pattern2 = re.compile(r'td class="ma_left".*?>\s*(.*?)\s*<')
        info = pattern2.findall(r)
        # print(len(title),title)
        # print(len(info),info)
        for i, t in zip(title, info):
            i = str(i).strip()
            qichacha[i] = t
        yield qichacha
"""