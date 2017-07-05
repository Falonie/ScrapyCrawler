# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Unit5Item(scrapy.Item):
    book_name = scrapy.Field()
    ratings = scrapy.Field()
    price = scrapy.Field()
    publishing_date = scrapy.Field()