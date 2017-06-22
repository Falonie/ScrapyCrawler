import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author_details'
    start_urls = ['http://quotes.toscrape.com/',]

    def parse(self, response):
        # for href in response.css('div.quote span.text::text').extract():
        # for href in response.css('div.quote'):
        #     yield {'next_page':href.css('li.next a::attr(href)').extract()}

        # for href in response.xpath('//li[@class="next"]/a/@href').extract():
        for href in response.xpath('//div[@class="quote"]/span[2]/a/@href').extract():
            yield scrapy.Request(response.urljoin(href),callback=self.author_details)
            # yield {'href':href}
        #     return href
        #     print(href)
            # yield scrapy.Request(response.urljoin(href),callback=self.author_details)

        # next_page = response.xpath('//li[@class="next"]/a/@href').extract()[0]
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def author_details(self,response):
        yield {'name':response.xpath('//div[@class="author-details"]/h3/text()').extract()[0].strip(),
               'born_date':response.xpath('//div[@class="author-details"]/p/span[@class="author-born-date"]/text()').extract_first(),
               'born_location':response.xpath('//div[@class="author-details"]/p/span[@class="author-born-location"]/text()').extract_first()}

        # for href in response.css('div.quotes span.a::attr(href)').extract():
        #     print(href)

        # for page in response.css('li.next a::attr(href)').extract():
        #     yield {'next_page':page}

        # next_page = response.css('li.next a::attr(href)').extract()
        # if next_page is not None:
        #     url = response.urljoin(next_page)
        #     yield scrapy.Request(url, callback=self.parse)
        # for next_page in response.css('li.next a::attr(href)').extract():
        #     #yield {'next_page':next_page}
        #     print(next_page)