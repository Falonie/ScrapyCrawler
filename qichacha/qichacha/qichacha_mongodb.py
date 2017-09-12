import pymongo

collection = pymongo.MongoClient(host='localhost', port=27017)['employee']['qichacha']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)

# collection.drop()

with open('/media/salesmind/Other/OTMS/qichacha_all_dimensions_test.txt', 'r') as f:
    for i, line in enumerate(f.readlines(), 1):
        print(i, line.strip())