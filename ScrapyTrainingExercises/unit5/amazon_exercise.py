import scrapy
from selenium import webdriver

base_url = 'https://www.amazon.cn'
# driver=webdriver.PhantomJS(executable_path=r'E:\files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://www.amazon.cn/s/ref=nb_sb_noss_1/457-9456003-0676269?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Dbooks&field-keywords=python&sprefix=python%2Caps%2CNaN&crid=2NW36ZVI3BPCN')
sel = scrapy.Selector(text=driver.page_source)
# print(sel.xpath('//div[@class="a-row a-spacing-none"]/a/h2/text()').extract())
for i in sel.xpath('//div[@class="a-row a-spacing-none"]/a/h2/text()').extract():
    print(i)
# print([i for i in sel.xpath('//div[@class="a-row a-spacing-none"]/a/h2/text()').extract()])
next_page_href = sel.xpath('//a[@class="pagnNext"]/@href').extract_first()
next_page = base_url + next_page_href
print(next_page)

# next_page_btn=driver.find_element_by_id('pagnNextString')
# next_page_btn.click()

search_bar = driver.find_element_by_id('twotabsearchtextbox')
search_bar.clear()
search_bar.send_keys('java')
driver.find_element_by_xpath('//div[@class="nav-search-submit nav-sprite"]/input').click()