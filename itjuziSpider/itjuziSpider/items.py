# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuzispiderItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    product_name = scrapy.Field()
    homepage = scrapy.Field()
    industry = scrapy.Field()
    scale = scrapy.Field()
    location = scrapy.Field()
    times = scrapy.Field()
    rounds = scrapy.Field()
    amount = scrapy.Field()
    investors = scrapy.Field()
    leadership = scrapy.Field()
    # pass
