# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiTruckDriversItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    position = scrapy.Field()
    recruit = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    scale = scrapy.Field()
    nature = scrapy.Field()
    industry = scrapy.Field()
    authentication = scrapy.Field()
    credit_ranking = scrapy.Field()
    job_description = scrapy.Field()
    company_description = scrapy.Field()