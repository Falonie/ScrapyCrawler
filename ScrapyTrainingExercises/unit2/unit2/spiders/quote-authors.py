import scrapy

class QuoteAuthor(scrapy.Spider):
    name = 'quote-authors'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            item = {'text': quote.xpath('span[@class="text"]/text()').extract()[0],
                    'tags': quote.xpath('div[@class="tags"]/a/text()').extract()}
        # yield {'herf':response.xpath('//li[@class="next"]/a/@href').extract_first()}
            author_url = quote.xpath('span[2]/a/@href').extract()[0]
            # yield {'author_url':author_url}
            yield scrapy.Request(response.urljoin(author_url), meta={'item':item}, dont_filter=True,
                                 callback=self.author_details)

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def author_details(self, response):
        item = response.meta.get('item', {})
        item['author'] = {
            'author-title': response.xpath('//div[@class="author-details"]/h3[@class="author-title"]/text()').extract()[0].strip(),
            'author-born-date':response.xpath('//div[@class="author-details"]/p[1]/span[@class="author-born-date"]/text()').extract()[0]}
        yield item
