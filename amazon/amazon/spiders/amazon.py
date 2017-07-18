import scrapy
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy_redis.spiders import RedisSpider
from ..items import AmazonItem

class Amazon(RedisSpider):
    name = "amazon"
    redis_key = 'Amazon:start_urls'
    start_urls = [
        'https://www.amazon.com/s/ref=sr_pg_{page}?rh=n%3A283155%2Ck%3Apython&page={page}&d=1&keywords=python&ie=UTF8&qid=1498837060&spIA=1786468522,B01MS6NN02,B071G3652S,178646439X']

    def start_requests(self):
        # header = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        # cookie = {
        #     'Cookie': 'session-token=f8xAgLueBhn9NCL0gpB048RXVzNkWuDnR+Qya6Wu7Zkz6Y831ogI4ftVSnvSVkAWH5ngYgVppgpvPg3Fjin203H4h6UpLBvwYbwuzf6SZGnYAXO51P2TtArNy/zMZr0FdSwm7nQIDnSjhsbpC2V8MVXlSHcbQ4/023HJZDIbsREo7KEd942p6j4l3Igv/oTJ; x-wl-uid=1GYh/oY10ZWNjqqmYG7mrEkboksY1LoZD0y/RpHmhZ8M/jFyqksWg0JOSBro6U+xTnVg4cxiLkzg=; skin=noskin; JSESSIONID=27E42C46E14D9A6166A39323CB256E92; session-id-time=2082787201l; session-id=159-4015366-6650112; ubid-main=160-7552422-4139833; csm-hit=ZFMXG7B4A0MYJWN39E1J+sa-ZFMXG7B4A0MYJWN39E1J-KG72V5XKQ5RZ241J79XQ|1492441072302'}

        for i in range(1, 5):
            url = self.start_urls[0].format(page=i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        amazon = AmazonItem()
        books = response.xpath('//h2[@data-attribute]/text()').extract()
        rating = response.xpath('//div[@class="a-row a-spacing-mini"]/a/text()').extract()
        price = response.xpath('//div[@class="a-column a-span7"]/div[@class="a-row a-spacing-none"][2]/a/span/@aria-label').extract()
        publishing_date = response.xpath(
            '//div[@class="a-row a-spacing-small"]/div[@class="a-row a-spacing-none"][1]/span[@class="a-size-small a-color-secondary"]/text()').extract()

        for b, r, p, pd in zip(books, rating, price, publishing_date):
            amazon['books'] = b
            amazon['ratings'] = r
            amazon['price'] = p
            amazon['publishing_date'] = pd
            yield amazon
            # print(b, r, p, pd)