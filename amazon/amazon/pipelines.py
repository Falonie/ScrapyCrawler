# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings
from .items import AmazonItem

class AmazonPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self):
        config = {'host': 'localhost', 'user': 'root', 'password': '1234', 'db': 'employee', 'charset': 'utf8mb4'}
        self.connect = pymysql.connect(**config)
        # self.connect = pymysql.connect(host='localhost', user='root', password='1234', db='employee', charset='utf8mb4')
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        sql = 'insert into scrapy_amazon (BOOK_NAME,RATINGS,PRICE,PUBLISHING_DATE) VALUES(%s,%s,%s,%s)'
        self.cursor.execute(sql, (item['books'], item['ratings'], item['price'], item['publishing_date']))
        self.connect.commit()
        return item
