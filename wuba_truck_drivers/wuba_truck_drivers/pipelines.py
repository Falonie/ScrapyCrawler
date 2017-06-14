# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,csv
from scrapy.conf import settings
from .items import WubaTruckDriversItem

class WubaTruckDriversPipeline(object):

    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='1234', db='employee',
                                          charset='utf8mb4')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        sql = 'insert into wuba_truck_drivers (TITLE,POSITION,RECRUIT,LOCATION,COMPANY,' \
              'INDUSTRY,SCALE,JOB_DESCRIPTION,COMPANY_DESCRIPTION) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql,(item['title'],item['position'],item['recruit'],item['location'],item['company'],
                            item['industry'],item['scale'],item['job_description'],item['company_description']))
        self.connection.commit()

        with open('wuba_truck_drivers.csv', 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow((item['title'], item['position'], item['recruit'], item['location'], item['company'],
                             item['industry'], item['scale']))

        with open('wuba_truck_drivers2.csv', 'a+', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerow((item['title'], item['position'], item['recruit'], item['location'], item['company'],
                             item['industry'], item['scale'],item['job_description'],item['company_description']))
        return item