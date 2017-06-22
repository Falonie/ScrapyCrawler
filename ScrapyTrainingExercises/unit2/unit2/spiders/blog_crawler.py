import scrapy

class ScrapingSpider(scrapy.Spider):
    name = 'blog_crawler'
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        # for href in response.xpath('//div[@class="nav-links"]/div/div[2]/a/@href').extract():
        for href in response.xpath('//article/header[@class="entry-header"]/h2/a/@href').extract():
            yield {'href':href}

        next_page=response.xpath('//div[@class="nav-links"]/div/div[2]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)

    def blog_details(self,response):
        yield {''}