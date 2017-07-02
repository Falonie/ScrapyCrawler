from pymongo import MongoClient
from pprint import pprint

client=MongoClient()
db=client['employee']
amazon=db['amazon']
# amazon_2=db['amazon_2']

for i,item in enumerate(amazon.find(),1):
    print(i,item)

# print('\n')
# print(amazon.find_one({'books':'Python Machine Learning'}))

# db.amazon.copyTo('amazon2')
# db.amazon.drop()
# db.amazon_2.remove()
# db.amazon2.drop()
