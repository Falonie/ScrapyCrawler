import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.spiders import CrawlSpider
from ..items import Unit5Item
from selenium import webdriver


class Spider(scrapy.Spider):
    name = 'amazon'
    # start_urls = ['https://www.amazon.cn/s/ref=nb_sb_ss_c_2_6?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Dbooks&field-keywords=python&sprefix=python%2Caps%2C154&crid=71XLL8KCV31R']
    start_urls = [
        'https://www.amazon.com/s/ref=nb_sb_ss_c_2_6/147-1679858-5856244?url=search-alias%3Dstripbooks&field-keywords=python&sprefix=python%2Caps%2C1257&crid=MWKPASGP50J4']

    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS(executable_path=r'E:\files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        # self.driver = webdriver.PhantomJS(executable_path=r'G:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        super(Spider, self).__init__(*args, **kwargs)

    def parse(self, response):
        self.logger.info('Parse function called on {}'.format(response.url))
        amazon = Unit5Item()
        self.driver.get(response.url)
        sel = scrapy.Selector(text=self.driver.page_source)
        books = sel.xpath('//h2[@data-attribute]/text()').extract()
        rating = sel.xpath('//div[@class="a-row a-spacing-mini"]/a/text()').extract()
        price = sel.xpath('//div[@class="a-column a-span7"]/div[@class="a-row a-spacing-none"][2]/a/span/@aria-label').extract()
        publishing_date = sel.xpath(
            '//div[@class="a-row a-spacing-small"]/div[@class="a-row a-spacing-none"][1]/span[@class="a-size-small a-color-secondary"]/text()').extract()
        # for i in sel.xpath('//div[@class="a-row a-spacing-none"]/a/h2/text()').extract():
        #     # yield {'book name': i}
        #     book['book_name'] = i
        for b, r, p, pd in zip(books, rating, price, publishing_date):
            amazon['book_name'] = b
            amazon['ratings'] = r
            amazon['price'] = p
            amazon['publishing_date'] = pd
            yield amazon

        # next_page = sel.xpath('//span[@class="pagnRA"]/a[@class="pagnNext"]/@href').extract_first()
        # base_url = 'https://www.amazon.cn'
        # if next_page:
        #     yield scrapy.Request(response.urljoin(next_page), dont_filter=True, callback=self.parse)