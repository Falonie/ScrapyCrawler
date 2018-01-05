import scrapy, re
from ..items import JinchengLogisticsItem


class JinchengLogisticsSpider(scrapy.Spider):
    name = 'jincheng'
    start_urls = ['http://company.jctrans.com/Company/List/0-0--13-111-0/{}.html']

    def start_requests(self):
        # 更改页码
        for i in range(1, 81):
            url = self.start_urls[0].format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response=response)
        for i in sel.xpath('//div[@class="com_name"]'):
            company = i.xpath('a/@title').extract_first()
            href = i.xpath('a/@href').extract_first()
            contact = i.xpath('p[@class="link_person"]/descendant::text()').extract()
            contact = ''.join(str(i).strip().replace('联系人：', '') for i in contact)
            # print(company, href, contact)
            item = {'company': company, 'contact': contact}
            yield scrapy.Request(url=href, meta={'item': item}, callback=self.parse_page)

    def parse_page(self, response):
        selector = scrapy.Selector(response=response)
        jincheng = JinchengLogisticsItem()
        jincheng = response.meta.get('item', '')
        for i in selector.xpath('//ul[@class="fei"]/li'):
            a = i.xpath('span[@class="name"]/text()').extract_first()
            pattern = re.compile(r'[\u3000\r\n ]')
            a = re.sub(r'[\u3000]', '', a)
            b = i.xpath('b/text()|span[2]/text()|text()').extract_first()
            b = ''.join(str(i).strip() for i in b)
            jincheng[a] = b
            brief_introduction = selector.xpath('//div[@class="contxt"]/text()').extract()
            jincheng['brief-introduction'] = pattern.sub('', ''.join(
                str(i).strip().replace(' ', '') for i in brief_introduction))
            # print(a, b)
        yield jincheng