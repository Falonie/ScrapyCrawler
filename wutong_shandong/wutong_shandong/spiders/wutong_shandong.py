import scrapy, re, requests, os
from ..items import WutongShandongItem

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


class WutongShandongSpider(scrapy.Spider):
    name = 'wutong_shandong'
    start_urls = ['http://www.chinawutong.com/223/p1354c1459l-1n-1/page{}']

    def start_requests(self):
        for i in range(1, 69):
            url = self.start_urls[0].format(i)
            yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response)
        for i in sel.xpath('//div[@class="companyl"]'):
            company_name = i.xpath('div[1]/div[2]/p[1]/a/text()').extract_first().strip()
            href = i.xpath('div[1]/div[2]/p[1]/a/@href').extract_first()
            l = i.xpath('div[@class="coifo fl"]/div[@class="wxtfio"]/p[@class="coare"]/text()').extract_first(
                default='N/A')
            location = ''.join(str(i).strip() for i in l)
            c = i.xpath('ul[@class="companyul"]/li[@class="zhishu"]/p[position()>2]/span/text()').extract_first(
                default='N/A')
            contact = ''.join(str(i).strip() for i in c)
            item = {'company_name': company_name, 'location': location, 'contact': contact}
            # print(company_name, href, location, contact)
            yield scrapy.Request(url=href, meta={'item': item}, dont_filter=True, callback=self.brief)

            # next_page = sel.xpath('//div[@class="fy_zwp"]/a[last()]/@href').extract_first()
            # if next_page:
            #     yield scrapy.Request(url=response.urljoin(next_page),callback=self.parse)

    def brief(self, response):
        sel = scrapy.Selector(response)
        pattern = re.compile(r'[\u3000\xa0\u2003\xae\u2022\u200b\u200c\x81\u20e3\ufe0f\xad\u202a\u200d\r\n\t ]')
        wutong_shandong = WutongShandongItem()
        wutong_shandong = response.meta.get('item', {})
        brief = sel.xpath('//div[@class="jianjie-content"]/p/text()').extract()
        brief2 = pattern.sub('', ''.join(str(i).strip() for i in brief))
        wutong_shandong['brief'] = brief2
        authentication = sel.xpath(
            '//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div[2]/table/tbody/tr/td/ul[1]/li[2]/span[2]/text()|//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div/table/tbody/tr/td/ul[1]/li/span[2]/text()').extract_first(
            default='N/A')
        wutong_shandong['authentication'] = authentication
        href = sel.xpath(
            '//*[@id="aspnetForm"]/div[10]/div/div[2]/div[1]/div[2]/table/tbody/tr/td/h2/a/@href').extract_first(
            default='N/A')
        # wutong_shandong['href2'] = href
        # item2 = {'brief': brief2, 'authentication': authentication}
        # item2.update(response.meta.get('item', {}))
        # yield scrapy.Request(url=href, meta={'item2': item2}, callback=self.page_details)
        picture = sel.xpath('//*[@id="aspnetForm"]/div[10]/div/div[1]/div[3]/div[2]/img/@src').extract_first()
        path = '/media/salesmind/Other/Shell/临沂3'
        if not os.path.exists(path):
            os.mkdir(path)
        file = path + '/' + '{}.jpg'.format(response.meta.get('item', {}).get('company_name'))
        with open(file, 'wb') as f:
            f.write(requests.get(url=picture, headers=headers).content)
        yield wutong_shandong


        # def page_details(self, response):
        #     sel = scrapy.Selector(response)
        #     wutong_shandong = response.meta.get('item2', {})
        #     try:
        #         wutong_shandong['telephone'] = sel.xpath('//ul[@class="wxtlx"]/li[2]/img/@src').extract_first(default='N/A')
        #     except Exception as e:
        #         wutong_shandong['telephone'] = 'N/A'
        #     wutong_shandong['mobile'] = sel.xpath('//ul[@class="wxtlx"]/li[3]/img/@src').extract_first(default='N/A')
        #     yield wutong_shandong