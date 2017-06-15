# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,csv
from scrapy.conf import settings
from .items import ItjuzispiderItem

class ItjuzispiderPipeline(object):

    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='1234', db='employee',
                                          charset='utf8mb4')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):

        sql='insert into itjuzi (PRODUCT,COMPANY_NAME,TIME,ROUND,FINANCIAL_AMOUNT,INDUSTRY,INVESTORS,SCALE,LOCATION,LEADERSHIP,HOMEPAGE) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, (item['product'], item['company_name'], item['time'], item['rounds'], item['financial amount'],
                                  item['industry'],item['investor'], item['scale'], item['location'], item['leadership'], item['homepage']))
        self.connection.commit()

        try:
            with open('itjuzi.csv','a+',newline='') as f:
                writer = csv.writer(f)
                writer.writerow((item['company_name'],item['product'],item['time'],item['rounds'],item['financial amount'],item['investor'],
                                 item['industry'],item['scale'],item['location'],item['leadership'],item['homepage']))
        except Exception as e:
            pass
        return item
