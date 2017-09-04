import pymongo

collection = pymongo.MongoClient(host='localhost', port=27017)['employee']['qichacha2']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)

# collection.drop()