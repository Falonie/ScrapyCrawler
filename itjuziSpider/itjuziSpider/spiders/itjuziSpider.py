# -*- coding: utf-8 -*-
import scrapy


class ItjuzispiderSpider(scrapy.Spider):
    name = 'itjuziSpider'
    # allowed_domains = ['basic']
    start_urls = ['https://www.itjuzi.com/company?page=1']

    # def start_requests(self):
    #     for i in range(1, 1000):
    #         url = self.start_urls[0].format(i)
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('@@@@@')
        selector = scrapy.Selector(response)
        print(response.xpath('//ul[contains(@class,"company-list")]/li'))
        for _ in selector.xpath('//ul[@class="list-main-icnset company-list-ul"]/li'):
            href = _.xpath('div[@class="cell maincell"]/div[@class="title"]/a/@href').extract_first()
            product = _.xpath('div[@class="cell maincell"]/div[@class="title"]/a/span[1]/text()').extract_first()
            location = _.xpath('i[@class="cell place"]/text()').extract()
            location = ''.join(str(i).strip() for i in location)
            item = {'href': href, 'product': product, 'location': location}
            print(item)
            yield scrapy.Request(url=href, meta={'item': item}, callback=self.parse_page)

    def parse_page(self, response):
        selector = scrapy.Selector(response)
        juzi=response.meta.get('item','')
        for _ in selector.xpath('//div[@class="picinfo"]'):
            short_name = _.xpath('div[@class="line-title"]/span[@class="title"]/h1/@data-name').extract()
            juzi['short_name'] = ''.join(str(i).strip() for i in short_name)
            full_name = _.xpath('div[@class="line-title"]/span[@class="title"]/h1/@data-fullname').extract()
            juzi['full_name'] = ''.join(str(i).strip() for i in full_name)
            slogan = _.xpath('div[2]/h2/text()').extract()
            juzi['slogan'] = ''.join(str(i).strip() for i in slogan)
            # print(short_name, full_name, slogan)
        # name=selector.xpath('//div[@class="line-title"]/span[@class="title"]/h1')
        for _ in selector.xpath('//div[@class="block-inc-info on-edit-hide"]'):
            brief_intro = _.xpath('div[@class="block" and position()=1]/div/descendant::text()|'
                                  'div[@class="block"]/div[@class="summary"]/text()').extract()
            juzi['brief_intro'] = ''.join(str(i).strip() for i in brief_intro)
            establish_time = _.xpath('div[@class="block" and position()=2]/div/h3[1]/descendant::text()|'
                                     'div[@class="block"]/div/h3[1]/descendant::text()').extract()
            juzi['establish_time'] = ''.join(str(i).strip() for i in establish_time)
            scale = _.xpath('div[@class="block"]/div/h3[2]/descendant::text()').extract()
            juzi['scale'] = ''.join(str(i).strip() for i in scale)
            # print(brief_intro, establish_time, scale)
        for _ in selector.xpath('//table[@class="list-round-v2"]/tbody/tr'):
            ficancing_time = _.xpath('td[1]/span/text()').extract()
            juzi['ficancing_time'] = ''.join(str(i).strip() for i in ficancing_time)
            rounds = _.xpath('td[2]/span/a/text()').extract()
            juzi['rounds'] = ''.join(str(i).strip() for i in rounds)
            leadership = selector.xpath('//li[@class="feedback-btn-parent first-letter-box-4js"]/div/descendant::text()').extract()
            juzi['leadership'] = ''.join(str(i).strip() for i in leadership)
            # print(ficancing_time, rounds, leadership)
        yield juzi