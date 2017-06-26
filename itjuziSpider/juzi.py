import requests,csv
from lxml import html

url='https://www.itjuzi.com/investevents?page=1'
header={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
cookie={'Cookie':'acw_tc=AQAAAEgfMhnaDA0AqfCh07JcaN85U78a; gr_user_id=2cbe1d8f-24a9-4515-aa6b-506b42f20bb6; MEIQIA_EXTRA_TRACK_ID=ca987278550011e78faf067fd4f49ede; identity=2014650646%40qq.com; remember_code=i1boX8JOtO; acw_sc=59493e3871e316dbb2235d29c20506b33220beab; session=c94244802898cb35ba68bc64a63a9be6225f1403; gr_session_id_eee5a46c52000d401f969f4535bdaa78=2c44fe5d-3cfd-4fce-aa49-e352fe0c1380; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1497884693; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1497972568; _ga=GA1.2.436743832.1497884693; _gid=GA1.2.554176371.1497884693; _gat=1'}
session=requests.session()
response=session.get(url=url,headers=header,cookies=cookie).text
selector=html.fromstring(response)
investors=selector.xpath('//div[@class="investorset"]/descendant::text()')
print([str(i).strip() for i in investors])