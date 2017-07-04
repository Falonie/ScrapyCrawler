# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql, pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy.log import logger
from .items import AmazonItem


class AmazonPipeline(object):
    def __init__(self):
        config = {'host': 'localhost', 'user': 'root', 'password': '1234', 'db': 'employee', 'charset': 'utf8mb4'}
        self.connect = pymysql.connect(**config)
        # self.connect = pymysql.connect(host='localhost', user='root', password='1234', db='employee', charset='utf8mb4')
        self.cursor = self.connect.cursor()

        connection = pymongo.MongoClient(host=settings['MONGODB_SERVER'], port=settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        sql = 'insert into scrapy_amazon2 (BOOK_NAME,RATINGS,PRICE,PUBLISHING_DATE) VALUES(%s,%s,%s,%s)'
        self.cursor.execute(sql, (item['books'], item['ratings'], item['price'], item['publishing_date']))
        self.connect.commit()

        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing {}!'.format(data))
        if valid:
            self.collection.insert(dict(item))
            # logger.log("Question added to MongoDB database!")
        return item