import scrapy
from ..items import WubaTruckDriversItem

class WubaTruckDrivers(scrapy.Spider):

    name = 'wuba_truck_drivers'
    start_urls = ['http://sh.58.com/sonhuosiji/?PGTID=0d302517-0000-2d1c-ff44-d938cbcf6a78&ClickID=2']

    # def start_requests(self):
    #     for i in range(1, 9):
    #         url = self.start_urls[0].format(page=i)
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # for item in response.xpath('//div[@id="infolist"]/dl/dt'):
        #     yield {'title':item.xpath('a/text()').extract_first(),
        #            'href':item.xpath('a/@href').extract_first()}
        for href in response.xpath('//div[@id="infolist"]/dl/dt/a/@href').extract():
            # yield {'href':href}
            yield scrapy.Request(url=href, callback=self.driver_details)

        next_page = response.xpath('//div[@class="pager"]/a[@class="next"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def driver_details(self, response):
        driver = WubaTruckDriversItem()
        for item in response.xpath('//div[@class="item_con pos_info"]'):
            driver['title'] = item.xpath('div[@class="pos_base_info"]/span[1]/text()').extract_first()
            driver['position'] = item.xpath('span/text()').extract_first()
            driver['recruit'] = item.xpath(
                'div[@class="pos_base_condition"]/span[@class="item_condition pad_left_none"]/text()').extract_first()
            driver['location'] = ''.join([str(i).strip() for i in item.xpath('div[@class="pos-area"]/span/a/text()').extract()])
            driver['company'] = response.xpath(
                '//div[@class="comp_baseInfo_title"]/div[@class="baseInfo_link"]/a/text()').extract_first()
            # driver['scale']=item.xpath('')
            driver['industry'] = response.xpath('//p[@class="comp_baseInfo_belong"]/a/text()').extract_first()
            driver['scale'] = response.xpath('//p[@class="comp_baseInfo_scale"]/text()').extract_first()
            driver['job_description'] = ''.join([str(i).strip() for i in response.xpath(
                '//div[@class="item_con"]/div[1]/div[@class="posDes"]/div[@class="des"]/text()').extract()])
            driver['company_description'] = ''.join([str(i).strip() for i in response.xpath('//div[@class="intro"]/div/p/text()').extract()])
        yield driver