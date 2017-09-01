import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['employee']
collection_shanghai = db['China_Manufacture_shanghai']
collection_hangzhou = db['China_Manufacture_hangzhou']
collection_shenzhen = db['China_Manufacture_shenzhen_new']

for i, j in enumerate(collection_hangzhou.find({}), 1):
    print(i, j)
# db['amazon'].drop()