import scrapy, re, logging, xlrd
from ..items import QichachaItem
from selenium import webdriver


class QichachaSpider(scrapy.Spider):
    name = 'qichacha_all'
    start_urls = ['http://www.qichacha.com/search?key={}']

    # def __init__(self, *args, **kwargs):
    #     self.driver = webdriver.PhantomJS(executable_path=r'E:\files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    #     super(QichachaSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        with open('/media/salesmind/0002C1F9000B55A8/Ctrip/库-365 (2).txt', 'r') as f:
            for i, line in enumerate(f.readlines(), 1):
                # print(i, line.strip())
                url = self.start_urls[0].format(line.strip())
                yield scrapy.Request(url=url, callback=self.parse)

    # def start_requests(self):
    #     with xlrd.open_workbook('/media/salesmind/Other/Ctrip/快租365-分支.xlsx') as data:
    #         table = data.sheets()[0]
    #         for rownum in range(1, table.nrows):
    #             row = table.row_values(rownum)
    #             url = self.start_urls[0].format(str(row[0]).strip())
    #             yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # print(type(response), type(str(response)), type(response.body.decode('utf-8')))
        sel = scrapy.Selector(response)
        basic_url = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=base'
        business = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=run'
        financial_report = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=report'
        company_name = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/a/descendant::text()').extract()
        company_name = ''.join(str(i).strip() for i in company_name)
        email = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[2]/span/text()').extract_first('N/A')
        legal_representative = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[1]/a/text()').extract_first('N/A')
        telephone = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[2]/text()').extract_first('N/A')
        telephone = ''.join(str(i).strip() for i in telephone)
        href = sel.xpath('//*[@id="searchlist"]/table[1]/tbody/tr/td[2]/a/@href').extract_first('N/A')
        unique_key = re.split(r'[_.]', href)[1]
        a = {'company_name': company_name, 'legal_representative': legal_representative, 'email': email,
             'telephone': telephone}
        # print(company_name, href, unique_key)
        # print(type(href))
        yield scrapy.Request(url=basic_url.format(unique_key, company_name), meta={'item': a},
                             callback=self.parse_basic)
        yield scrapy.Request(url=business.format(unique_key, company_name), meta={'item': a},
                             callback=self.parse_business)
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
        pattern = re.compile(r'class="ma_bluebg ma_left".*?>\s*(.*?)\s*</td> ')
        title = pattern.findall(r)[2::]
        pattern2 = re.compile(r'class="ma_left".*?>\s*(.*?)\s*<')
        info = pattern2.findall(r)
        qichacha.update({str(i).strip().replace('：', ''): t for i, t in zip(title, info)})
        for j, i in enumerate(sel.xpath('//*[@id="Sockinfo"]/table[@class="m_changeList"]/tr[position()>1]'), 1):
            shareholders = i.xpath('td/text()|td/div/a[1]/text()').extract()
            a = 'shareholder{}'.format(j)
            b = ''.join(str(i).strip() for i in shareholders)
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
        qichacha['分支机构'] = sel.xpath('//*[@id="Subcom"]/div[1]/span[2]/text()').extract_first(default='N/A')
        yield qichacha

    def parse_business(self, response):
        # qichacha = QichachaItem()
        qichacha = response.meta.get('item', '')
        sel = scrapy.Selector(response)
        r = response.body.decode('utf-8')
        for j, i in enumerate(sel.xpath('//*[@id="joblist"]/table/tbody/tr[position()>1]'), 1):
            joblist = i.xpath('td/text()').extract()
            # print('recruit{}'.format(j), ''.join(str(i).strip() for i in joblist))
            a = 'recruit_member{}'.format(j)
            b = ''.join(str(i).strip() for i in joblist)
            qichacha[a] = b
        jobs_amout = sel.xpath('//section[@id="joblist"]/div[1]/span/text()').extract()
        qichacha['jobs_amout']=''.join(str(i) for i in jobs_amout)
        job_release_lates_date = sel.xpath('//section[@id="joblist"]/table[@class="m_changeList"]/'
                                           'tbody/tr[2]/td/descendant::text()').extract()
        qichacha['latest_job'] = ','.join(str(i).strip() for i in job_release_lates_date)
        for i in sel.xpath('//*[@id="V3_cwzl"]/table/tr'):
            title = i.xpath('td[position()=1 or position()=3]/text()').extract()
            content = i.xpath('td[position()=2 or position()=4]/text()').extract()
            qichacha.update({str(t).strip().replace('：', ''): str(c).strip() for t, c in zip(title, content)})
        for i in sel.xpath('//section[@id="financingList"]/table[@class="m_changeList"]'):
            head = i.xpath('thead/th/text()').extract()
            item = i.xpath('tbody/tr[1]/td/descendant::text()').extract()
            financing_content = [str(i).strip() for i in item]
            financing_content = list(filter(lambda x: len(x) > 1, financing_content))
            qichacha.update({k: v for k, v in zip(head, financing_content)})
        # yield qichacha

    def parse_financial_report(self, response):
        # qichacha = QichachaItem()
        qichacha = response.meta.get('item', '')
        sel = scrapy.Selector(response)
        r = response.body.decode('utf-8')
        for i in sel.xpath('//div[@class="tab-pane fade in active"]/table[@class="table table-bordered"]/tbody/tr|'
                           '//div[@class="tab-pane fade in active"]/table[@class="table table-bordered"]/tr'):
            title = i.xpath('td[position()=1 or position()=3]/text()').extract()
            content = i.xpath('td[position()=2 or position()=4]/text()').extract()
            qichacha.update({str(k).strip().replace('：', ''):str(v).strip() for k,v in zip(title,content)})
        for i in sel.xpath('//div[@class="tab-pane fade in active"]/table[2]/tbody'):
            title = i.xpath('tr[1]/td/text()').extract()
            content = i.xpath('tr[2]/td/text()|tr[2]/td/a/text()').extract()
            content = list(filter(lambda x: len(x) > 1, content))
            qichacha.update({str(t).strip().replace('：', ''): str(c).strip() for t, c in zip(title, content)})
        # yield qichacha