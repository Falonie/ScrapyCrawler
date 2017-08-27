import scrapy
from ..items import AppdownloadItem
from selenium import webdriver


class APPdownload(scrapy.Spider):
    name = 'APPdownload'
    start_urls = ['http://www.wandoujia.com/search?key={}&source=']

    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS(executable_path=r'E:\files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        super(APPdownload, self).__init__(*args, **kwargs)

    def start_requests(self):
        with open('E:\约克法修\APP2.txt', 'r') as f:
            base_url = 'http://www.wandoujia.com/search?key={}&source='
            for line in f.readlines():
                url = self.start_urls[0].format(line.strip())
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.driver.get(response.url)
        sel = scrapy.Selector(text=self.driver.page_source)
        product = AppdownloadItem()
        for item in sel.xpath('//li[@class="search-item search-searchitems"][1]/div[@class="app-desc"]'):
            product_names = item.xpath('h2/a/text()').extract_first(default='N/A')
            download = item.xpath('div[@class="meta"]/span/text()').extract_first(default='N/A')
            # yield {'product name': product_names, 'download': download}
            product['brand'] = product_names
            product['download'] = download
            yield product