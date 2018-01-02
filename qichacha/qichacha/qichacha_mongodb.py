import pymongo

collection = pymongo.MongoClient(host='localhost', port=27017)['employee']['qichacha']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)

# collection.drop()

with open('/media/salesmind/Other/OTMS/qichacha_all_dimensions_test.txt', 'r') as f:
    for i, line in enumerate(f.readlines(), 1):
        print(i, line.strip())

"""
with open('/media/salesmind/Other/MongoDB_files/招聘-e签宝-result-01.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        # print(row[0], str(row[1]).split(','))
        # for i in str(row[1]).split(','):
        # print(str(row[1]).split(','))
        with open('/media/salesmind/Other/MongoDB_files/招聘-e签宝-result-01_1.csv', 'a+') as f2:
            writer = csv.writer(f2)
            writer.writerow((str(row[0]),str(row[1]).split(',')))
"""

"""
with open("/media/salesmind/Other/others/repository_address.txt", 'r') as f:
    for i, line in enumerate(f.readlines(), 1):
        print(line.strip())
        # print(list(line.strip()))
        # keywords = 'XXX '
        with open('/media/salesmind/Other/others/repository_address.csv', 'a+',newline='') as f2:
            writer = csv.writer(f2)
            writer.writerow((line.strip(),))
            # valuess = spider.search(line.strip())
"""
