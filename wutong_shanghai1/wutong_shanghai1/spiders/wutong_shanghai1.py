import scrapy,re
from ..items import WutongShanghai1Item
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider

class WutongShanghaiSpider(scrapy.Spider):
# class WutongShanghaiSpider(RedisSpider):
    name = 'wutong_shanghai1'
    # name = 'wutong_shanghai1_redis'
    start_urls = ['http://www.chinawutong.com/223/p1937c1961l1n-1/']

    def parse(self, response):
        selector = scrapy.Selector(response)
        for item in selector.xpath('//div[@class="companyl"]|//div[@class="company"]'):
            company = item.xpath('div[1]/div[2]/p[1]/a/text()').extract_first()
            href = item.xpath('div[1]/div[2]/p[1]/a/@href').extract_first()
            # next_page = selector.xpath('//div[@class="fy_zwp"]/a[last()]/@href').extract_first()
            a = {'company': company}
            # yield {'company': company, 'href': href,'next_page':next_page}
            yield scrapy.Request(url=href, meta={'item': a}, callback=self.brief)

        # next_page = selector.xpath('//div[@class="fy_zwp"]/a[last()]/@href').extract_first()
        # if next_page:
        #     yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def brief(self, response):
        sel = scrapy.Selector(response)
        pattern = re.compile(r'[\u3000\xa0\u2003\xae\u2022\u200b\u200c\x81\u20e3\ufe0f\xad\u202a\u200d\r\n\t ]')
        wutong_shanghai = WutongShanghai1Item()
        wutong_shanghai = response.meta.get('item', '')
        brief = sel.xpath('//div[@class="jianjie-content"]/p/text()').extract()
        wutong_shanghai['brief'] = pattern.sub('',''.join([str(i).strip() for i in brief]))
        yield wutong_shanghai