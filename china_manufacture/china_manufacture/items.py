# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaManufactureItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    product = scrapy.Field()
    mode = scrapy.Field()
    supplying_products = scrapy.Field()
    address = scrapy.Field()
    brief = scrapy.Field()
    contact = scrapy.Field()
    mobile = scrapy.Field()
    a1 = scrapy.Field()
    details = scrapy.Field()
