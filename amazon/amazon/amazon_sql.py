import pymysql
#
# def amazon_sql():
#
#     connnection = pymysql.connect(host='localhost', user='root', password='1234', db='employee', charset='utf8mb4')
#     with connnection.cursor() as cursor:
#         sql = 'select * from scrapy_amazon'
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         for i, row in enumerate(results, 1):
#             print(i, row)
#
# if __name__ == '__main__':
#     amazon_sql()


class Amazon_sql():

    def __init__(self):
        self.connect = pymysql.connect(host='localhost', user='root', password='1234', db='employee', charset='utf8mb4')
        self.cursor = self.connect.cursor()

    def process_item(self):
        sql = 'select * from scrapy_amazon'
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for i, row in enumerate(results, 1):
            # item = (i, row)
            # return item
            print(i, row)

if __name__=='__main__':
    sql = Amazon_sql()
    sql.process_item()
    # print(sql.process_item())