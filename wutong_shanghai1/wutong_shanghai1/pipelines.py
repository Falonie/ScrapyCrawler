# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql, pymongo, csv
from .items import WutongShanghai1Item
from scrapy.conf import settings


class WutongShanghai1Pipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port='27017')
        self.db = self.client['empolyee']
        self.collection = self.db['wutong_shanghai1']

    def process_item(self, item, spider):

        # connection = pymysql.connect(host='localhost', user='root', password='1234', db='employee', charset='utf8mb4')
        # with connection.cursor() as cursor:
        #     sql = "INSERT INTO wutong_shenzhen1 (COMPANY,BRIEF) values('{}','{}')"
        #     cursor.execute(sql.format(item['company'], item['brief']))
        #     connection.commit()

        try:
            self.collection.insert(dict(item))
        except Exception as e:
            print(e)

        try:
            with open('wutong_shenzhen_logistics_companies_test2.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow((item['company'], item['brief']))
        except Exception as e:
            print(e)
        return item