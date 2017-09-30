import scrapy, re
from scrapy.http import Request, FormRequest
from ..items import FrozenfoodsItem
from itertools import zip_longest


class FrozenFoodSpider(scrapy.Spider):
    name = 'frozenfood'
    start_urls = ['http://www.maidongpin.com/pc/list/supplylistPage']

    def start_requests(self):
        for i in range(1, 3):
            # data = {'page': str(i), 'rows': str(20)}
            yield scrapy.FormRequest(url=self.start_urls[0], formdata={'page': str(i), 'rows': str(50)}, callback=self.parse)
            # yield Request(url=self.start_urls[0], method='POST', body=json.dumps(data), callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response=response)
        # print(type(response))
        for i in sel.xpath('//div[@class="grid_1200"]/ul[@class="list_prd"]/li'):
            href = i.xpath('div[1]/a/@href').extract_first(default='N/A')
            name = i.xpath('div[2]/span[1]/text()').extract_first(default='N/A')
            # print(name, href)
            item = {'name': name}
            yield Request(url=href, meta={'item': item}, callback=self.page)

        # next_page = sel.xpath('//div[@class="float_right"]/ul[@class="page_bd"]/li[last()-1]/@title').extract_first()
        # n = 1
        # if next_page == '下一页':
        #     yield scrapy.FormRequest(url=self.start_urls[0], formdata={'page': str(n)}, callback=self.parse)
        #     n += 1

    def page(self, response):
        frozenfood = response.meta.get('item', '')
        selector = scrapy.Selector(response=response)
        a = selector.xpath('//table[@class="detail_table"]/tr/descendant::text()').extract()
        a = [re.sub(r'[\r\t\n\xa0| ]', '', i) for i in a]
        a = list(filter(lambda x: len(x) > 1, a))
        a = ''.join(a)
        # print(a.split('：'))
        key = selector.xpath(
            '//table[@class="detail_table"]/tr[1]/th[position()=2 or position()=4 or position()=6]/text()').extract()
        value = selector.xpath('//table[@class="detail_table"]/tr[1]/td/text()').extract()
        for a, b in zip(key, value):
            frozenfood[a] = b
        key2 = selector.xpath(
            '//table[@class="detail_table"]/tr[2]/th[position()=2 or position()=4 or position()=6]/text()').extract()
        key2 = [re.sub(r'[\r\t\n\xa0 ]', '', i) for i in key2]
        value2 = selector.xpath('//table[@class="detail_table"]/tr[2]/td/text()').extract()
        for a, b in zip_longest(key2, value2):
            frozenfood[a] = b
        for i in selector.xpath('//table[@class="detail_table2"]/tr'):
            a = ''.join(str(i).strip() for i in i.xpath('th/text()').extract())
            a = re.sub(r'[\r\t\n\xa0 ]', '', a)
            b = ''.join(str(i).strip() for i in i.xpath('td/descendant::text()').extract())
            b = re.sub(r'[\r\t\n\xa0 ]', '', b)
            frozenfood[a] = b
        for i in selector.xpath('//div[@class="detail_right"]/div[@class="business"]/div[@class="top"]/ul/li'):
            text = i.xpath('text()').extract_first(default='N/A')
            a, b = re.sub(r'[\xa0 ]', '', text).split('：')
            frozenfood[a] = b
            # print(a,b)
        yield frozenfood