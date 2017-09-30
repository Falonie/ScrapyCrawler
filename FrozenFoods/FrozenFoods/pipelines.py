# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class FrozenfoodsPipeline(object):
    def __init__(self):
        self.collection = pymongo.MongoClient(host='127.0.0.1', port=27017)['Falonie']['frozenfood']

    def process_item(self, item, spider):
        try:
            self.collection.insert(dict(item))
        except Exception as e:
            print(e)
        return item