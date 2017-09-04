import scrapy, re
from ..items import ChinaManufactureItem


class ChinaManufactureSpider(scrapy.Spider):
    name = 'china_manufacture'
    start_urls = [
        'http://cn.made-in-china.com/companysearch.do?propertyValues=&action=hunt&senior=0&certFlag=0&order=0&style=b&page={page}&comProvince=Zhejiang&comCity=Zhejiang_Hangzhou&size=30&viewType=&word=%CD%E2%C3%B3&from=hunt&comServiceType=&chooseUniqfield=0']
    # start_urls = [
    #     'http://cn.made-in-china.com/companysearch.do?propertyValues=&action=hunt&senior=0&certFlag=0&order=0&style=b&page={page}&comProvince=Guangdong&comCity=Guangdong_Shenzhen&size=30&viewType=&word=%CD%E2%C3%B3&from=hunt&comServiceType=&chooseUniqfield=0']
    # start_urls = [
    #     'http://cn.made-in-china.com/companysearch.do?propertyValues=&action=hunt&senior=0&certFlag=0&order=0&style=b&page={page}&comProvince=Shanghai&comCity=&size=30&viewType=&word=%CD%E2%C3%B3&from=hunt&comServiceType=&chooseUniqfield=0']

    def start_requests(self):
        for i in range(1, 45):
            url = self.start_urls[0].format(page=i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response=response)
        for item in sel.xpath('//li[@class="co-item"]'):
            company = item.xpath('div[1]/label[@class="co-name"]/a/@title').extract_first(default='N/A')
            link = item.xpath('div[1]/label[@class="co-name"]/a/@href').extract_first(default='N/A')
            product = ''.join(i for i in item.xpath('div[2]/div[1]/ul[1]/li[1]/a/text()').extract())
            mode = str(item.xpath('div[2]/div[1]/ul[1]/li[2]/a/text()').extract_first()).strip()
            supplying_products = item.xpath('div[2]/div[1]/ul[1]/li[3]/a/text()').extract_first(default='N/A')
            address = item.xpath('div[2]/div[1]/ul[1]/li[4]/a/text()').extract_first(default='N/A')
            p = {'company': company, 'product': product, 'mode': mode, 'supplying products': supplying_products,
                 'address': address, 'link': link}
            baseurl = 'http://cn.made-in-china.com'
            yield scrapy.Request(url=baseurl + link, meta={'item': p}, callback=self.company_details, dont_filter=True)

    # def company(self, response):
    #     # china_manufacture = ChinaManufactureItem()
    #     item = response.meta.get('item', {})
    #     href = response.xpath('//div[@class="boxCont boxText"]/p[@class="companyInf"]/a/@href').extract_first()
    #     # yield {"href": href}
    #     if href:
    #         yield scrapy.Request(url=href, meta={'item1': item}, callback=self.company_details)
    #     else:
    #         pass

    def company_details(self, response):
        china_manufacture = ChinaManufactureItem()
        pattern = re.compile(r'[\u3000\r\n\t\xa0 ]')
        selector = scrapy.Selector(response)
        china_manufacture = response.meta.get('item', '')
        # brief = response.xpath('//div[@class="boxCont company-blk"]/div[1]/p/text()').extract()
        brief = selector.xpath('//div[@class="boxCont boxText"]/p[@class="companyInf"]/text()').extract()
        brief1 = pattern.sub('', ''.join(str(i).strip() for i in brief))
        china_manufacture['brief'] = pattern.sub('', ''.join(str(i).strip() for i in brief))
        for i in selector.xpath('//div[@class="boxCont boxText contactCard"]/ul[@class="contactInfo"]'):
            contact = i.xpath('li[1]/text()|li[1]/strong/text()').extract()
            contact1 = pattern.sub('', ''.join(str(i).strip() for i in contact))
            mobile1 = i.xpath('li[2]/strong[@class="contact-bd org"]/text()').extract_first(default='N/A')
            china_manufacture['contact'] = pattern.sub('', ''.join(str(i).strip() for i in contact))
            china_manufacture['mobile'] = i.xpath('li[2]/strong[@class="contact-bd org"]/text()').extract_first(default='N/A')
        details = selector.xpath('//div[@class="box"]/div/table/tr/th/text()|//div[@class="box"]/div/table/tr/td/text()|//div[@class="box"]/div/table/tr/td/label/text()').extract()
        china_manufacture['details'] = ''.join(str(i).strip() for i in details)
        for j in selector.xpath('//div[@class="box"]/div/table/tr'):
            a = j.xpath('th/text()').extract()
            b = j.xpath('td/text()|td/label/text()').extract()
            a1 = str(a[0]).strip().replace('：', '')
            b1 = ''.join(str(i).strip() for i in b)
            detail = a1 + b1
            china_manufacture[a1] = b1
        yield china_manufacture