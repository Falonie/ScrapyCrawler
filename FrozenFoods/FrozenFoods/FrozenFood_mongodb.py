import pymongo

collection = pymongo.MongoClient(host='127.0.0.1', port=27017)['Falonie']['frozenfood']
for i, j in enumerate(collection.find(), 1):
    print(i, j)
# collection.rename(new_name='frozenfood')