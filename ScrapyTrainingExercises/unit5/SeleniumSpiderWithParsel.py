import parsel
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def scrape():
    driver = webdriver.PhantomJS(executable_path=r'G:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get('https://www.amazon.cn/s/ref=nb_sb_noss_1/457-9456003-0676269?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Dbooks&field-keywords=python&sprefix=python%2Caps%2CNaN&crid=2NW36ZVI3BPCN')
    while True:
        sel = parsel.Selector(text=driver.page_source)
        for i in sel.xpath('//div[@class="a-row a-spacing-none"]/a/h2/text()').extract():
            # yield {'book name': i}
            print({'book name': i})

        try:
            driver.find_element_by_id('pagnNextString').click()
        except NoSuchElementException:
            break

if __name__ == '__main__':
    scrape()