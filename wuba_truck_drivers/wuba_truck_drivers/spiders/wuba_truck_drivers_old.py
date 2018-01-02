import scrapy,re
from ..items import WubaTruckDriversItem

class WubaTruckDrivers(scrapy.Spider):

    name = 'wuba_truck_drivers_old'
    # start_urls = ['http://sh.58.com/sonhuosiji/?PGTID=0d302517-0000-2d1c-ff44-d938cbcf6a78&ClickID=2']
    start_urls = ['http://fz.58.com/job/pn{}/?key=%E5%8F%B8%E6%9C%BA&final=1&jump=1']

    def start_requests(self):
        for i in range(1, 3):
            url = self.start_urls[0].format(page=i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        selector=scrapy.Selector(response)
        # for item in response.xpath('//div[@id="infolist"]/dl/dt'):
        #     yield {'title':item.xpath('a/text()').extract_first(),
        #            'href':item.xpath('a/@href').extract_first()}
        for href in response.xpath('//div[@id="infolist"]/dl/dt/a/@href').extract():
                # yield {'href':href}
            yield scrapy.Request(url=href, callback=self.driver_details)

        # next_page = response.xpath('//div[@class="pager"]/a[@class="next"]/@href').extract_first()
        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse)

    def driver_details(self, response):
        driver = WubaTruckDriversItem()
        pattern = re.compile(r'[\u3000\xa0\u2003\xae\u2022\u200b\u200c\x81\u20e3\ufe0f\xad\u202a\u200d\u2212 ]')
        for item in response.xpath('//div[@class="item_con pos_info"]'):
            title = item.xpath('div[@class="pos_base_info"]/span/text()').extract()
            driver['title'] = ''.join([str(i) for i in title])
            driver['position'] = ''.join([str(i) for i in item.xpath('span/text()').extract()])
            recruit = item.xpath('div[@class="pos_base_condition"]/span[@class="item_condition pad_left_none"]/text()').extract()
            driver['recruit'] = ''.join([str(i) for i in recruit])
            location = item.xpath('div[@class="pos-area"]/span/descendant::text()').extract()
            driver['location'] = ''.join([str(i).strip().replace('查看地图', '') for i in location])
            company = response.xpath('//div[@class="comp_baseInfo_title"]/div[@class="baseInfo_link"]/a/text()').extract()
            driver['company'] = ''.join([str(i) for i in company])
            industry = response.xpath('//p[@class="comp_baseInfo_belong"]/a/text()').extract()
            driver['industry'] = ''.join([str(i) for i in industry])
            scale = response.xpath('//p[@class="comp_baseInfo_scale"]/text()').extract()
            driver['scale'] = ''.join([str(i) for i in scale])
            job_description = response.xpath('//div[@class="item_con"]/div[1]/div[@class="posDes"]/div[@class="des"]/text()').extract()
            driver['job_description'] = pattern.sub('', ''.join([str(i).strip() for i in job_description]))
            company_description = response.xpath('//div[@class="intro"]/div/p/text()').extract()
            driver['company_description'] = pattern.sub('', ''.join([str(i).strip() for i in company_description]))
        yield driver