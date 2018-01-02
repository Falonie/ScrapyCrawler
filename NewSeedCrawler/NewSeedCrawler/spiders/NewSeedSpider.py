# -*- coding: utf-8 -*-
# __author__ = 'Falonie'
import scrapy, re


class NewseedspiderSpider(scrapy.Spider):
    name = 'NewSeedSpider'
    # allowed_domains = ['basic']
    start_urls = ['http://www.newseed.cn/project/r113-p{}']

    def start_requests(self):
        for i in range(1, 40):
            url = self.start_urls[0].format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = scrapy.Selector(response)
        for _ in selector.xpath('//div[@class="project-list"]/table[@class="table-list"]/tbody/tr[position()>1]'):
            href = _.xpath('td[1]/a/@href').extract_first(default='N/A')
            rounds = _.xpath('td[4]/descendant::text()').extract()
            rounds = ','.join(str(i).strip() for i in rounds)
            item = {'round': rounds}
            # print(href,rounds)
            yield scrapy.Request(url=href, meta={'item': item}, callback=self.parse_page)

    def parse_page(self, response):
        NewSeed = response.meta.get('item', '')
        selector = scrapy.Selector(response)
        for _ in selector.xpath('//div[@class="info-box"]/div[@class="info"]'):
            product = _.xpath('h1/text()').extract()
            NewSeed['product'] = ''.join(str(i).strip() for i in product)
            field = _.xpath('ul[@class="subinfo"]/li[@class="l"]/p[1]/a/text()').extract()
            NewSeed['field'] = ''.join(str(i).strip() for i in field)
            platform = _.xpath('ul[@class="subinfo"]/li[@class="l"]/p[2]/span[1]/text()').extract()
            NewSeed['platform'] = ''.join(str(i).strip() for i in platform)
            location = _.xpath('ul[@class="subinfo"]/li[@class="l"]/p[2]/span[2]/text()').extract()
            NewSeed['location'] = ''.join(str(i).strip() for i in location)
            homepage = _.xpath('ul[@class="subinfo"]/li[@class="l"]/p[3]/span[1]/descendant::text()').extract()
            NewSeed['homepage'] = ''.join(str(i).strip() for i in homepage)
            establish_time = _.xpath('ul[@class="subinfo"]/li[@class="r box-fix-r"]/p[1]/text()').extract()
            NewSeed['establish_time'] = ''.join(str(i).strip() for i in establish_time)
            status = _.xpath('ul[@class="subinfo"]/li[@class="r box-fix-r"]/p[2]/text()').extract()
            NewSeed['status'] = ''.join(str(i).strip() for i in status)
            tags = selector.xpath('//div[@class="project-top"]/div[@class="txt"]/div[1]/a/text()').extract()
            NewSeed['tags'] = ''.join(str(i).strip() for i in tags)
            description = selector.xpath('//div[@class="box-plate"]/div[@class="desc"]/text()').extract()
            NewSeed['description'] = re.sub(r'[\n\r ]', '', ''.join(str(i).strip() for i in description))
            contact = _.xpath(
                '//div[@class="project-status"]/div[@class="people-list"]/h4[@class="title"]/a/text()').extract()
            NewSeed['contact'] = ''.join(str(i).strip() for i in contact)
            NewSeed['project_status'] = _.xpath('//div[@class="project-status"]/a/text()').extract_first(default='N/A')
            leadership = selector.xpath(
                '//div[@class="item-list people-list"]/ul/li/div[2]/descendant::text()').extract()
            leadership = list(filter(lambda x: len(x) > 1, [str(_).strip() for _ in leadership]))
            NewSeed['leadership'] = ''.join(str(i).strip() for i in leadership)
            logo_url = selector.xpath('//div[@class="img"]/span[@class="img-middle"]/img/@src').extract()
            NewSeed['company_name'] = selector.xpath('//div[@class="company-box"]/dl[1]/p/a/text()').extract_first(
                default='N/A')
            brief_intro = selector.xpath('//div[@class="company-box"]/dl[1]/dd//text()').extract()
            NewSeed['brief_intro'] = re.sub('r[\n\r ]','',''.join(str(i).strip() for i in brief_intro))
            NewSeed['logo_url'] = ''.join(str(i).strip() for i in logo_url)
            NewSeed['url'] = response.url
            yield NewSeed