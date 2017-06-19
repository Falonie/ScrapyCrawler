# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,csv
from .items import FreightTransportItem
from scrapy.conf import settings

class FreightTransportPipeline(object):

    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='1234', db='employee',
                                          charset='utf8mb4')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):

        try:
            sql = 'insert into freight_transport (COMPANY,CONTACT,TELEPHONE,TELEGRAPH,' \
                  'MOBILE,LOCATION,REGISTER_DATE,BRIEF) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (item['company'], item['contact'], item['telephone'], item['telegraph'],
                                      item['mobile'], item['location'],item['register_data'], item['brief']))
            self.connection.commit()
        except Exception as e:
            pass

        try:
            with open('freight_transport.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow((item['company'], item['contact'], item['telephone'], item['telegraph'],
                                      item['mobile'], item['location'],item['register_data'], item['brief']))
        except Exception as e:
            pass
        return item
