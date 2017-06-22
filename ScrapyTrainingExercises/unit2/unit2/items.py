# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Unit2Item(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_price = scrapy.Field()
    book_stock = scrapy.Field()
    # pass
