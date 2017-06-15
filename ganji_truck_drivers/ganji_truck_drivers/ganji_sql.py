import pymysql

def ganji_sql():

    # config = {'host': 'localhost', 'user': 'root', 'password': '1234', 'db': 'employee', 'charset': 'utf8mb4'}
    # connnection = pymysql.connect(**config)
    connnection = pymysql.connect(host='localhost', user='root', password='1234', db='employee', charset='utf8mb4')
    with connnection.cursor() as  cursor:
        sql = 'select * from ganji_truck_drivers'
        cursor.execute(sql)
        results = cursor.fetchall()
        for i, row in enumerate(results, 1):
            print(i, row)

if __name__ == '__main__':
    ganji_sql()