import scrapy,sys,io
from ..items import GanjiTruckDriversItem

class GanjiTruckDrivers(scrapy.Spider):

    name = 'ganji_truck_drivers'
    start_urls = ['http://sh.ganji.com/zphuoyunsiji/']
    # start_urls = ['http://sh.ganji.com/zphuoyunsiji/o{}/']

    # def start_requests(self):
    #     for i in range(1,5):
    #         url = self.start_urls[0].format(i)
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # for item in response.xpath('//dl'):
        #     yield {'href':item.xpath('dt/a/@href').extract_first(),
        #            'title':item.xpath('dt/a/text()').extract_first()}
        for href in response.xpath('//dl/dt/a/@href').extract():
            yield scrapy.Request(url=href, callback=self.drivers_details)
            # yield {'href':href}

        # next_page = response.xpath('//ul[@class="pageLink clearfix"]/li[last()]/a/@href').extract_first()
        # if next_page:
        #     yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def drivers_details(self, response):
        driver = GanjiTruckDriversItem()
        # response.encoding = 'charset=utf-8'
        driver['title'] = response.xpath('//div[@class="d-c-left-hear"]/h1/text()').extract()[0]
        driver['position'] = response.xpath('//ul[@class="clearfix pos-relat"]/li[1]/em/a/text()').extract_first()
        driver['company'] = response.xpath('//div[@class="ad-firm-logo"]/span/a/text()').extract_first().strip()
        driver['recruit'] = response.xpath('//ul[@class="clearfix pos-relat"]/li[6]/em/text()').extract_first()
        location = response.xpath('//ul[@class="clearfix pos-relat"]/li[last()]/em/a/text()').extract()
        location2 = response.xpath('//ul[@class="clearfix pos-relat"]/li[last()]/em/text()').extract_first().strip()
        location.append(location2)
        driver['location'] = ''.join([str(i) for i in location])
        driver['scale'] = response.xpath('//div[@class="ad-firm-logo"]/div/div[last()]/span/text()').extract_first()
        driver['nature'] = response.xpath(
            '//div[@class="ad-firm-logo"]/div/div[last()-1]/span/a/text()').extract_first()
        driver['industry'] = response.xpath('//div[@class="ad-firm-logo"]/div/div[last()-2]/span/a/text()').extract_first()
        driver['authentication'] = response.xpath(
            '//div[@class="ad-firm-logo"]/div/div[last()-3]/span/text()').extract_first()
        driver['credit_ranking'] = response.xpath('//div[@class="ad-firm-logo"]/div/div[last()-4]/div/@class').extract_first()
        driver['job_description'] = ''.join([str(i).strip() for i in response.xpath(
            '//div[@class="js-tab-show d-l-account fc4b"]/div[1]/text()').extract()])
        driver['company_description'] = ''.join(
            [str(i).strip() for i in response.xpath('//div[@class="js-tab-show d-com-intr fc4b"]/p/text()').extract()])
        yield driver