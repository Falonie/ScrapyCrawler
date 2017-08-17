import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['employee']
collection = db['Recruit_shenzhen_kuajingdianshang_crossbordertransanction']
collection2 = db['Recruit_shenzhen_oversea_haiwaituiguang']
collection3 = db['Recruit_shenzhen_waimaodianshang']
collection4 = db['Recruit_Shanghai']
collection5 = db['Recruit_Hangzhou_test']
collection6 = db['Recruit_Hangzhou_test2']

for i, j in enumerate(collection5.find({}), 1):
    print(i, j)
# collection5.drop()