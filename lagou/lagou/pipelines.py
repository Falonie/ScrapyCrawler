# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class LagouPipeline(object):
    # def open_spider(self,spider):
    #     with sqlite3.connect('lagou.db') as self.conn:
    #         self.c = self.conn.cursor()
            # self.c.execute('create table lagou(salary varchar(512),company_name varchar(128),block varchar(128))')

    def process_item(self, item, spider):
        print(spider.name,'pipelines')
        # insert_sql = "insert into lagou (salary,company_name,block) values('{}','{}','{}')".format(item['salary'],
        #                                                                                            item['company_name'],
        #                                                                                            item['block'])
        # self.c.execute(insert_sql)
        # self.conn.commit()
        return item
