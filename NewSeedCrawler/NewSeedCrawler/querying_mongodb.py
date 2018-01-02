import pymongo,os

collection = pymongo.MongoClient(host='localhost', port=27017)['Falonie']['newseed_IPO上市及以后_scrapy2']
# collection = pymongo.MongoClient(host='localhost', port=27017)['Falonie']['物通烟台3']
for i, j in enumerate(collection.find({}), 1):
    print(i, j)
print(os.path.abspath('.'))
# collection.rename('newseed_种子_scrapy')
# collection.drop()