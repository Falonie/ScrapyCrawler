# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql, pymongo, csv
from .items import ChinaManufactureItem
from scrapy.conf import settings


class ChinaManufacturePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client['employee']
        self.collection = self.db['China_Manufacture_hangzhou']

    def process_item(self, item, spider):
        try:
            self.collection.insert(dict(item))
        except Exception as e:
            print(e)

        # try:
        #     with open('ChinaManufacture_shanghai_new.csv', 'a+', newline='') as f:
        #         writer = csv.writer(f)
        #         writer.writerow((item['company'], item['product'], item['mode'],
        #                          # item['supplying_products']
        #                          item['address']
        #                          , item['brief'], item['contact'], item['mobile'],item['details']
        #                          ))
        #         # writer.writerow((item['company'], item['product'], item['mode'], item['supplying_products'],
        #         #                  item['address'], item['brief'], item['contact'], item['mobile']))
        # except Exception as e:
        #     pass
        return item