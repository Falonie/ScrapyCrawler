# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhongchouItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    brief = scrapy.Field()
    a = scrapy.Field()
    # introduction = scrapy.Field()
    key = scrapy.Field()