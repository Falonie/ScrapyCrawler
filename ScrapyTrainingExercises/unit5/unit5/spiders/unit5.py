import scrapy
from selenium import webdriver

class Spider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.cn/s/ref=nb_sb_ss_c_2_6?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Dbooks&field-keywords=python&sprefix=python%2Caps%2C154&crid=71XLL8KCV31R']

    def __init__(self,*args,**kwargs):
        self.driver = webdriver.PhantomJS(executable_path=r'E:\files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        # self.driver = webdriver.PhantomJS(executable_path=r'G:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        super(Spider, self).__init__(*args, **kwargs)

    def parse(self, response):
        self.driver.get(response.url)
        sel = scrapy.Selector(text=self.driver.page_source)
        for i in sel.xpath('//div[@class="a-row a-spacing-none"]/a/h2/text()').extract():
            yield {'book name': i}

        next_page = sel.xpath('//span[@class="pagnRA"]/a[@class="pagnNext"]/@href').extract_first()
        base_url = 'https://www.amazon.cn'
        if next_page:
            yield scrapy.Request(base_url + next_page, callback=self.parse)