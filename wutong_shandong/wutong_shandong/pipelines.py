# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class WutongShandongPipeline(object):
    def __init__(self):
        self.collection = pymongo.MongoClient(host='localhost', port=27017)['Falonie']['物通临沂3']

    def process_item(self, item, spider):
        try:
            self.collection.insert(dict(item))
        except Exception as e:
            print(e)
        return item