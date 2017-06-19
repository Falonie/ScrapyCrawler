import scrapy
from ..items import FreightTransportItem

class FreightTransport(scrapy.Spider):
    name = 'freighttransport'
    # start_urls = ['http://sh.zghy.com/Page/index.aspx?page=1']
    start_urls = ['http://sh.zghy.com/Page/index.aspx?page={}']

    def start_requests(self):
        for i in range(1, 2052):
            url = self.start_urls[0].format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.xpath('//div[@class="List_ItemList"]/ul/li[@class="Title"]/p/a/@href').extract():
            # yield {'href':href}
            yield scrapy.Request(url=response.urljoin(href), callback=self.freight_company)

    def freight_company(self,response):
        freight = FreightTransportItem()
        # freight['item'] = response.xpath('//tr/td/span/text()').extract()
        try:
            freight['register_data'] = str(response.xpath('//tr/td/span/text()').extract()[1]).split('：')[1]
        except Exception as e:
            freight['register_data'] = 'N/A'

        try:
            freight['company'] = response.xpath('//tr/td/span/text()').extract()[4]
        except Exception as e:
            freight['contact'] = response.xpath('//tr/td/span/text()').extract()[2]

        try:
            freight['contact'] = response.xpath('//tr/td/span/text()').extract()[5]
        except Exception as e:
            freight['contact'] = 'N/A'

        try:
            freight['telephone'] = response.xpath('//tr/td/span/text()').extract()[6]
        except Exception as e:
            freight['telephone'] = 'N/A'

        try:
            freight['telegraph'] = response.xpath('//tr/td/span/text()').extract()[7]
        except Exception as e:
            freight['telegraph'] = 'N/A'

        try:
            freight['mobile'] = response.xpath('//tr/td/span/text()').extract()[8]
        except Exception as e:
            freight['mobile'] = 'N/A'

        try:
            freight['location'] = response.xpath('//tr/td/span/text()').extract()[9]
        except Exception as e:
            freight['location'] = 'N/A'

        try:
            brief = response.xpath('//span[@id="ctl00_ContentPlaceHolder1_lbIntro"]/text()').extract_first()
            freight['brief'] = ''.join([str(i).strip() for i in brief])
        except Exception as e:
            freight['brief'] = 'N/A'

        yield freight