import scrapy

class Baixing_Truck_Drivers(scrapy.Spider):

    name = 'baixing_truck_drivers'
    start_urls=['http://shanghai.baixing.com/siji/m37286/?page=2']

    def parse(self, response):
        for href in response.xpath('//div[@class="preview-hover"]/a[@class="ad-title"]').extract():
            print(href)