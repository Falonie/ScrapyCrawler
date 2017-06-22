import scrapy
from ..items import Unit2Item

class BookCrawler(scrapy.Spider):

    name = 'book-crawler'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for href in response.xpath('//article/h3/a/@href').extract():
            yield scrapy.Request(url=response.urljoin(href),callback=self.book_details)
        # for href in response.xpath('//li[@class="next"]/a/@href').extract():
        #     yield {'href':href}
        # print(response)

        next_page=response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(url=response.urljoin(next_page),callback=self.parse)

    def book_details(self,response):
        book = Unit2Item()
        for books in response.xpath('//div[@class="col-sm-6 product_main"]'):
            book['book_name'] = books.xpath('h1/text()').extract_first()
            book['book_price'] = books.xpath('p[@class="price_color"]/text()').extract_first()
            book['book_stock'] = books.xpath('p[@class="instock availability"]/text()').extract()[1].strip()
            yield book
            # yield {'book':book.xpath('h1/text()').extract()}