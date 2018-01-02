import pymongo

collection = pymongo.MongoClient(host='localhost', port=27017)['Falonie']['物通临沂3']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)
# print(15*29)
# collection.drop()