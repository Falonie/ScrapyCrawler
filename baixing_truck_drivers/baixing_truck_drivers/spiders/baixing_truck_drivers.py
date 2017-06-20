import scrapy
from ..items import BaixingTruckDriversItem

class Baixing_Truck_Drivers(scrapy.Spider):

    name = 'baixing_truck_drivers'
    start_urls=['http://shanghai.baixing.com/siji/m37286/?page=2']

    def parse(self, response):
        for href in response.xpath('//div[@class="preview-hover"]/a[@class="ad-title"]/@href').extract():
            # yield {'href': href}
            yield scrapy.Request(url=href, callback=self.truck_driver)

    def truck_driver(self, response):
        driver = BaixingTruckDriversItem()
        driver['title'] = response.xpath('//div[@class="viewad-header"]/div[@class="viewad-title "]/h1/text()').extract_first()
        driver['company'] = response.xpath('//div[@class="viewad-meta-item company"]/span/text()').extract_first()
        driver['category'] = response.xpath('//div[@class="viewad-meta"]/div[@class="viewad-meta-item"][1]/span/a/text()').extract_first()
        driver['recruit'] = response.xpath('//div[@class="viewad-meta"]/div[@class="viewad-meta-item"][2]/span/text()').extract_first()
        driver['location'] = response.xpath('//div[@class="viewad-meta2"]/div[@class="viewad-meta2-item"][1]/span/text()').extract_first()
        driver['contact'] = response.xpath('//div[@class="viewad-meta2"]/div[@class="viewad-meta2-item "][2]/label[2]/text()').extract()
        yield driver