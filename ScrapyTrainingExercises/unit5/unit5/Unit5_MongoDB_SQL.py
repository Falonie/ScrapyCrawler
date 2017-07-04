import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client['employee']
#amazon=db['amazon_python_books']

for i,item in enumerate(db.amazon_python_books.find({}),1):
    print(i,item)