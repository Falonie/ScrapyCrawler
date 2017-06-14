# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,csv
from scrapy.conf import settings
from .items import ItjuzispiderItem

class ItjuzispiderPipeline(object):

    # def __init__(self):
    #     self.connection = pymysql.connect(host='localhost', user='root', password='1234', db='employee',
    #                                       charset='utf8mbt')
    #     self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        return item
