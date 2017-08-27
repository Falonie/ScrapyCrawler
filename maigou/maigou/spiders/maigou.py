import scrapy, re
from ..items import MaigouItem


class MaigouSpider(scrapy.Spider):
    name = 'maigou'
    start_urls = ['http://10.maigoo.com/search/?catid=3054&areaid=2769&action=ajax&getac=brand&page={page}']

    def start_requests(self):
        for i in range(1, 15):
            url = self.start_urls[0].format(page=i)
            yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        # print(response)
        # print(type(response), type(response.body), type(response.body.decode('utf-8')))
        r = response.body.decode('utf-8')
        r1 = response.body
        pattern = re.compile(r'<a class="dhidden" href="(.*?)" target="_blank">')
        # for i in pattern.findall(str(r1)):
        for href in pattern.findall(r):
            item = {'href': href}
            yield scrapy.Request(url=href, meta={'item': item},dont_filter=True, callback=self.page_details)

    def page_details(self, response):
        selector = scrapy.Selector(response)
        maigou = MaigouItem()
        maigou = response.meta.get('item', '')
        name = selector.xpath('//ul[@class="info fr"]/li[@class="name"]/text()').extract_first(default='N/A')
        maigou['company'] = name
        for item in selector.xpath('//ul[@class="info col3 noweixin"]/li[position()<6]'):
            n = item.xpath('text()|b/font/text()|a/text()').extract()
            try:
                a, b = ''.join(str(i).strip().replace('\n', '') for i in n).split('：')
            except Exception as e:
                a = ''.join(str(i).strip().replace('\n', '') for i in n).split('：')[0]
                b = 'N/A'
            finally:
                maigou[a] = b
        for item in selector.xpath('//ul[@class="info fr"]/li[position()>1]'):
            a, b = ''.join(str(i).strip() for i in item.xpath('text()|a/text()').extract()).split('：')
            # name = selector.xpath('//ul[@class="info fr"]/li[@class="name"]/text()').extract_first('N/A')
            # print(a, b)
            maigou[a] = b
            # maigou['company'] = name
        for item in selector.xpath('//ul[@class="license"]/li'):
            try:
                a, b = ''.join(str(i).strip() for i in item.xpath('text()|a/text()').extract()).split('：')
            except Exception as e:
                a, b = ''.join(str(i).strip() for i in item.xpath('text()|a/text()').extract()).split('：')[0], 'N/A'
            finally:
                maigou[a] = b
        brief = selector.xpath('//div[@class="introduce"]/div[@class="desc"]/p/text()').extract()
        maigou['brief'] = re.sub(r'[\n\r ]', '', ''.join(str(i) for i in brief))
        yield maigou