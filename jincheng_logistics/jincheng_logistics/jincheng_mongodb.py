import pymongo

collection = pymongo.MongoClient(host='127.0.0.1', port=27017)['Falonie']['jincheng_logistics_福州']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)

# collection.drop()
# collection.rename('jincheng_logistics_yantai')