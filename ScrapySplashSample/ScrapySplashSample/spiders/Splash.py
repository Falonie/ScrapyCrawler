# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from ..items import ScrapysplashsampleItem


class SplashSpider(scrapy.Spider):
    name = 'Splash'

    def start_requests(self):
        urls = ['http://stock.qq.com/l/stock/ywq/list20150423143546.htm']
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 0.5})

    def parse(self, response):
        sel = scrapy.Selector(response)
        links = sel.xpath('//div[@class="qq_main"]/ul/li/div[@class="info"]/h3/a/@href').extract()
        # print(links)
        for link in links:
            item = {'item': link}
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse_article)

    def parse_article(self, response):
        selector = scrapy.Selector(response)
        # article = Splash1Item()
        article = response.meta.get('item', '')
        article['title'] = selector.xpath('//div[@class="qq_article"]/div[@class="hd"]/h1/text()').extract_first(
            default='N/A')
        article['source'] = selector.xpath('//span[@class="a_source"]/descendant::text()').extract_first(default='N/A')
        article['report_date'] = selector.xpath('//span[@class="a_time"]/descendant::text()').extract_first(
            default='N/A')
        yield article