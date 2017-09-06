import scrapy, re
from scrapy.http import Request
from ..items import QichachaItem
from selenium import webdriver


class QichachaSpider(scrapy.Spider):
    name = 'qichacha_all2'
    # start_urls = [
    #     'http://www.qichacha.com/search?key=%E5%B9%BF%E4%B8%9C%E5%BE%B7%E5%B0%94%E9%A1%BF%E7%A3%81%E8%83%BD%E7%83%AD%E6%B0%B4%E5%99%A8%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8']
    # start_urls = [
    #     'http://www.qichacha.com/search?key=%E5%B9%BF%E5%B7%9E%E5%B8%82%E8%81%94%E4%B8%8A%E7%82%89%E5%85%B7%E8%B4%B8%E6%98%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8']
    start_urls = ['http://www.qichacha.com/search?key=奥特朗电器（广州）有限公司']

    # def __init__(self, *args, **kwargs):
    #     self.driver = webdriver.PhantomJS(executable_path=r'E:\files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    #     super(QichachaSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # print(type(response), type(str(response)), type(response.body.decode('utf-8')))
        sel = scrapy.Selector(response)
        basic_url = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=base'
        business = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=run'
        financial_report = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=report'
        company_name = sel.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/em/em/text()').extract_first()
        href = sel.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/@href').extract_first()
        unique_key = re.split(r'[_.]', href)[1]
        a = {'company_name': company_name}
        # print(unique_key)
        # print(company_name, href, unique_key)
        self.new_basic_url = basic_url.format(unique_key, company_name)
        self.new_business_url = business.format(unique_key, company_name)
        self.new_financial_report_url = financial_report.format(unique_key, company_name)
        yield scrapy.Request(url=basic_url.format(unique_key, company_name), meta={'item': a},
                             callback=self.parse_basic)
        # yield scrapy.Request(url=business.format(unique_key, company_name), meta={'item': a},
        #                      callback=self.parse_business)
        # yield scrapy.Request(url=financial_report.format(unique_key, company_name), meta={'item': a},
        #                      callback=self.parse_financial_report)

    def parse_basic(self, response):
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
            i = str(i).strip().replace('：', '')
            qichacha[i] = t
        for j, i in enumerate(sel.xpath('//*[@id="Sockinfo"]/table[@class="m_changeList"]/tr[position()>1]'), 1):
            s = i.xpath('td/text()|td/div/a[1]/text()').extract()
            a = 'shareholder{}'.format(j)
            b = ''.join(str(i).strip() for i in s)
            # print('shareholder{}'.format(j), ''.join(str(i).strip() for i in s))
            qichacha[a] = b
        for i, j in enumerate(sel.xpath('//*[@id="Mainmember"]/table[@class="m_changeList"]/tr[position()>1]'), 1):
            staff = j.xpath('td/text()|td/div/a/text()').extract()
            c = 'staff{}'.format(i)
            d = ''.join(str(i).strip() for i in staff)
            # print('staff{}'.format(i), ''.join(str(i).strip() for i in staff))
            qichacha[c] = d
        introduction = sel.xpath('//section[@id="Comintroduce"]/div[2]/div/p/text()').extract()
        qichacha['introduction'] = ''.join(str(i).strip() for i in introduction)
        # item={a:b,c:d}
        yield scrapy.Request(url=self.new_business_url, callback=self.parse_business)
        # yield qichacha

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


"""
    def parse_financial_report(self, response):
        qichacha = QichachaItem()
        # print(type(response.body), type(response), type(response.body.decode('utf-8')))
        # print(response.body.decode('utf-8'))
        # self.driver.get(response.url)
        # print(self.driver.page_source)
        qichacha = response.meta.get('item', '')
        sel = scrapy.Selector(response)
        r = response.body.decode('utf-8')
        for i in sel.xpath('//div[@class="tab-pane fade in active"]/table[@class="table table-bordered"]/tbody/tr|//div[@class="tab-pane fade in active"]/table[@class="table table-bordered"]/tr'):
            title = i.xpath('td[position()=1 or position()=3]/text()').extract()
            content = i.xpath('td[position()=2 or position()=4]/text()').extract()
            # print(a,b)
            for a, b in zip(title, content):
                a = str(a).strip().replace('：','')
                b = str(b).strip()
                # print(a, b)
                qichacha[a] = b
        for i in sel.xpath('//div[@class="tab-pane fade in active"]/table[2]/tbody'):
            title = i.xpath('tr[1]/td/text()').extract()
            # print(title)
            content = i.xpath('tr[2]/td/text()|tr[2]/td/a/text()').extract()
            content = list(filter(lambda x: len(x) > 1, content))
            # print(content)
            for t, c in zip(title, content):
                t = str(t).strip().replace('：','')
                c = str(c).strip()
                # print(t, c)
                qichacha[t] = c
        yield qichacha
"""