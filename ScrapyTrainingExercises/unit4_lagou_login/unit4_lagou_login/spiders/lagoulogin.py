import scrapy

class LagouLogin(scrapy.Spider):
    name = 'lagoulogin'
    # start_urls = ['https://passport.lagou.com/login/login.html?ts=1498399747484&serviceId=lagou&service=https%253A%252F%252Fwww.lagou.com%252F&action=login&signature=9F7B78139D980C22EE7205FEB0CA65E8']
    start_urls = ['https://passport.36kr.com/pages/?ok_url=http%3A%2F%2F36kr.com%2F#/login?pos=header']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response,
                                               formdata={'username': '2014650646@qq.com', 'password': '413154831'},
                                               callback=self.homepage)

    def homepage(self, response):
        selector = scrapy.Selector(response)
        # yield {'job_title': selector.xpath('//div[@class="menu_box"]/div[1]/a/text()').extract()}
        print(response)