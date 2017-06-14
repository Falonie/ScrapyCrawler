# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,csv,xlwt
from scrapy.conf import settings
from .items import GanjiTruckDriversItem

class GanjiTruckDriversPipeline(object):

    def __init__(self):
    #     self.connection = pymysql.connect(host='localhost', user='root', password='1234', db='employee',
    #                                       charset='utf8mb4')
    #     self.cursor = self.connection.cursor()

        self.book = xlwt.Workbook()
        self.sheet = self.book.add_sheet('sheet', cell_overwrite_ok=True)


    #
    def process_item(self, item, spider):

    #     sql='insert into ganji_truck_drivers (TITLE,POSITION,RECRUIT,LOCATION,COMPANY,INDUSTRY,NATURE,SCALE' \
    #         ',AUTHENTICATION,CREDIT_RANKING,JOB_DESCRIPTION,COMPANY_DESCRIPTION) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    #     self.cursor.execute(sql, (
    #     item['title'], item['position'], item['recruit'], item['location'], item['company'], item['industry'],
    #     item['nature'], item['scale'], item['authentication'], item['credit_ranking'], item['job_description'],
    #     item['company_description']))
    #     self.connection.commit()
    #
        # with open('ganji3.csv', 'a+', newline='',encoding='utf-8') as f:
        #     writer = csv.writer(f)
        #     writer.writerow((item['title'], item['position'], item['recruit'], item['location'], item['company'],
        #                      item['industry'], item['nature'], item['scale'], item['authentication'],
        #                      item['credit_ranking'], item['job_description'], item['company_description']))
    #
    #     with open('ganji2.csv', 'a+', newline='') as f2:
    #         writer = csv.writer(f2)
    #         writer.writerow((item['title'], item['position'], item['recruit'], item['location'], item['company'],
    #                          item['industry'], item['nature'], item['scale'], item['authentication'],
    #                          item['credit_ranking']))

        self.sheet.write((item['title'], item['position'], item['recruit'], item['location'], item['company'],item['industry'], item['nature'],
                          item['scale'], item['authentication'], item['credit_ranking'],item['job_description'], item['company_description']))

        self.book.save('ganji_xlwt.xls')
        #
        return item