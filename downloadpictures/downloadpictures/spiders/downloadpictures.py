import scrapy
from ..items import DownloadpicturesItem


class DownloadPicturesSpiders(scrapy.Spider):
    name = 'pictures'
    start_urls = ['https://stocksnap.io/']

    # start_urls = ['https://stocksnap.io/api/load-photos/date/desc/2']

    def parse(self, response):
        image = DownloadpicturesItem()
        print(response)
        sel = scrapy.Selector(response)
        img_urls = []
        for i in sel.xpath('//div[@id="main"]/a/img/@src').extract():
            # print(i)
            # image['image_urls'] = [i]
            image['image_urls'] = [i]
            yield image
        #     img_urls.append(i)
        # image['image_urls'] = img_urls
        # yield image