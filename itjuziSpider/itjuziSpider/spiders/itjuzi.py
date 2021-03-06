import scrapy
from ..items import ItjuzispiderItem


class ItjuziSpider(scrapy.Spider):
    name = 'itjuzi'
    # start_urls = ['https://www.itjuzi.com/investevents?page=1']
    start_urls = ['https://www.itjuzi.com/investevents?page={}']

    def start_requests(self):
        for i in range(1, 2463):
            url = self.start_urls[0].format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.xpath('//p[@class="title"]/a[@target="_blank"]/span/text()').extract()
        links = response.xpath('//p[@class="title"]/a[@target="_blank"]/@href').extract()
        financial_amount = response.xpath('//i[@class="cell money"]/text()').extract()[1::]
        # investors = response.xpath('//div[@class="investorset"]/a[@target="_blank"]/descendant::text()').extract()
        rounds = response.xpath('//i[@class="cell round"]/a/span/text()').extract()
        times = response.xpath('//i[@class="cell date"]/span/text()').extract()
        # for product in products:
        #     yield {'product':product}
        for product, link, amount, r, t in zip(products, links, financial_amount, rounds, times):
            # yield {'product': product, 'link': link, 'amount': amount}
            # p = {'product': product, 'financial amount': amount, 'investor': investor, 'rounds': r, 'time': t}
            p = {'product': product, 'financial amount': amount, 'rounds': r, 'time': t}
            yield scrapy.Request(url=link, meta={'item': p}, dont_filter=True, callback=self.page)
        # for href in response.xpath('//div[@class="ui-pagechange for-sec-bottom"]/a[last()-1]/text()').extract():
        #     yield {'product':product,'links':link}

        # next_page = response.xpath('//div[@class="ui-pagechange for-sec-bottom"]/a[last()-1]/text()').extract()
        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse)

    def page(self, response):
        juzi = ItjuzispiderItem()
        juzi = response.meta.get('item', {})
        company = response.xpath('//div[@class="des-more"]/div[1]/h2/text()').extract()
        juzi['company_name'] = str(company[0]).split('：')[1]
        try:
            homepage = response.xpath('//div[@class="picinfo"]/div[@class="link-line"]/a[@class="weblink"]/@href').extract()
            juzi['homepage'] = ''.join([str(i).strip() for i in homepage])
        except Exception as e:
            juzi['homepage'] = 'N/A'
        industry = [str(i) for i in response.xpath('//div[@class="picinfo"]/div[3]/span[1]/a/text()').extract()]
        juzi['industry'] = ''.join(industry)
        juzi['scale'] = str(response.xpath('//div[@class="des-more"]/div[2]/h2[2]/text()').extract()[0]).strip().split('：')[1]
        locaiton = [str(i) for i in response.xpath('//div[@class="picinfo"]/div[3]/span[2]/a/text()').extract()]
        juzi['location'] = ''.join(locaiton)
        leadership = [str(i) for i in response.xpath('//h4[@class="person-name"]/a[@class="title"]/b/span/text()').extract()]
        juzi['leadership'] = ''.join(leadership)
        yield juzi