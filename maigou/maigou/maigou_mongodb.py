import pymongo

collection = pymongo.MongoClient(host='127.0.0.1', port=27017)['employee']['maigou']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)

# collection.rename('maigou')