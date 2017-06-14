# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    books = scrapy.Field()
    ratings = scrapy.Field()
    price = scrapy.Field()
    publishing_date = scrapy.Field()
    # pass
