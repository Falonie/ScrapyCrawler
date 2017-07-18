import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client['employee']
#amazon=db['amazon_python_books']

# for i,item in enumerate(db.amazon_python_books.find({}),1):
#     print(i,item)
#
# # db['amazon_python_books'].rename('amazon_python_books_old')
# print(db['amazon_python_books_old'].full_name)
# print(db['amazon_python_books'].count())
# # db['amazon_python_books_old'].rename('amazon_python_books_cn')
# print(db['amazon_python_books'].name)
# db['amazon_python_books'].copyTo('amazon_1')
db['amazon_python_books'].remove()