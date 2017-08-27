import pymongo

collection = pymongo.MongoClient(host='localhost', port=27017)['employee']['zhongchou']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)

# collection.rename('zhongchou')