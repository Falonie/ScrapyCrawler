import scrapy, re
from ..items import ZhongchouItem


class ZhongchouSpider(scrapy.Spider):
    name = 'zhongchou'
    start_urls = [
        'http://www.zhongchoujia.com/platform/default.aspx?pi={page}&prid=20&fa=-1&pni=-1&dt=-1&pt=-1&pname=&rank=-1']

    def start_requests(self):
        for i in range(1, 11):
            url = self.start_urls[0].format(page=i)
            yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        selector = scrapy.Selector(response)
        # print(type(response),type(response.body),type(response.body.decode('utf-8')))
        # for item in selector.xpath('//ul[@class="platformlist"]/li[@class="platformItem pbox"]/div[1]/div[1]/a'):
        for item in selector.xpath('//div[@class="title"]/a'):
            title = item.xpath('text()').extract_first()
            href = item.xpath('@href').extract_first()
            item = {'item': title}
            # yield {'href':href,'title':title}
            yield scrapy.Request(url='http://www.zhongchoujia.com{}'.format(href), meta={'item': item},
                                 dont_filter=True, callback=self.page_details)

        # next_page = selector.xpath('//div[@class="m-t-20 paging page"]/pre/a[last()-1]/@href').extract_first()
        # if next_page:
        #     scrapy.Request(url='http://www.zhongchoujia.com{}'.format(next_page), dont_filter=True, callback=self.parse)

    def page_details(self, response):
        selector = scrapy.Selector(response)
        zhongchou = ZhongchouItem()
        zhongchou = response.meta.get('item', '')
        for i in selector.xpath('//div[@class="basic-right"]'):
            name = i.xpath('div[@class="basic-Title Titlefont"]/h1').extract_first(default='N/A')
            brief = i.xpath('div[@class="basic-Content"]/text()').extract_first(default='N/A')
            zhongchou['name'] = re.sub(r'[\r\n<h1>/ ]', '', name)
            zhongchou['brief'] = re.sub(pattern=r'[\r\n/ ]', repl='', string=''.join(str(i).strip() for i in brief))
        for item in selector.xpath('//div[@class="basic-right"]/ul[@class="basic-detailul"]/li'):
            title = ''.join(str(i).strip().replace(' ', '') for i in item.xpath('span[2]/text()|span[2]/a/text()').extract())
            key = re.sub(pattern=r'[\r\n- ]', repl='', string=title).split('：')[0]
            value = re.sub(pattern=r'[\r\n- ]', repl='', string=title).split('：')[1]
            zhongchou[key] = value
        for i in selector.xpath('//div[@class="pfd-archives pfd-item "]/div[1]/div[@class="archivesinfo"]/p'):
            a, b = ''.join(str(i).replace('\r\n ', '').strip() for i in i.xpath('text()').extract()).split('：')
            zhongchou[a] = b
        introduction = selector.xpath('//div[@class="pfd-archives pfd-item "]/div[2]/div/p/descendant::text()').extract()
        zhongchou['introduction'] = ''.join(str(i).strip().replace(' ', '') for i in introduction)
        yield zhongchou
