# -*- coding: utf-8 -*-
import scrapy, re
from ..items import RecruitAmazonItem


class Recruit2Spider(scrapy.Spider):
    name = 'recruit2'
    # start_urls = [
    #     'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=%E5%A4%96%E8%B4%B8%E7%94%B5%E5%95%86&isadv=0&sg=5c6fce89e325407a84e8d43aca6804cc&p={}']
    start_urls = [
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E9%94%80%E5%94%AE&isadv=0&sg=d1adcdbd993b45148ae48fe7e01806e0&p={}']

    def start_requests(self):
        for i in range(1, 91):
            url = self.start_urls[0].format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response)
        r = response.body.decode('utf-8')
        # print(response.body.decode('utf-8'))
        # item = sel.xpath('//div[@id="newlist_list_content_table"]/table[position()>1]/tbody/tr[1]')
        # position = item.xpath('td[1]/div/a/text()').extract()
        pattern = re.compile(r'<a style=.*?target="_blank">(.*?)</a>')
        pattern2 = re.compile(r'<td class="gsmc"><a.*?target="_blank">(.*?)</a> ')
        pattern3 = re.compile(r'<td class="gxsj"><span>(.*?)</span><')
        pattern4 = re.compile(r' <td class="zwyx">(.*?)</td>')
        pattern5 = re.compile(r'<a style="font-weight:.*?href="(.*?)" target="_blank">')
        position = pattern.findall(r)
        company = pattern2.findall(r)
        release_time = pattern3.findall(r)
        salary = pattern4.findall(r)
        href = pattern5.findall(r)
        next_page = sel.xpath('//div[@class="pagesDown"]/ul/li[@class="pagesDown-pos"]/a/@href').extract_first(default='N/A')
        for p, c, r, s, h in zip(position, company, release_time, salary, href):
            p = re.sub(r'[</b>]', '', p)
            item = {'position': p, 'company': c, 'release time': r, 'salary': s, 'next_page': next_page}
            # yield item
            yield scrapy.Request(url=h, meta={'item': item}, dont_filter=True, callback=self.page_details)

        # next_page = sel.xpath('//div[@class="pagesDown"]/ul/li[@class="pagesDown-pos"]/a/@href').extract_first()
        # if next_page:
        #     yield scrapy.Request(url=next_page, dont_filter=True, callback=self.parse)

    def page_details(self, response):
        recruit = RecruitAmazonItem()
        selector = scrapy.Selector(response)
        recruit = response.meta.get('item', '')
        for _ in selector.xpath('//div[@class="terminalpage-main clearfix"]/div[@class="tab-cont-box"]'):
            job_description = _.xpath('div[1]/descendant::text()').extract()
            job_description = re.sub(r'[\xa0\n\r\t ]','',''.join(str(i).strip() for i in job_description))
            company_description_ = _.xpath('div[2]/descendant::text()').extract()
            company_description = re.sub(r'[\xa0\n\r\t ]','',''.join(str(i).strip() for i in company_description_))
            recruit['job_description'] = job_description
            recruit['company_description'] = company_description
        for _ in selector.xpath('//div[@class="company-box"]/ul/li'):
            a = _.xpath('span/text()').extract_first(default='N/A')
            b = _.xpath('strong/descendant::text()').extract()
            b = ''.join(str(i).strip() for i in b)
            recruit[a] = b
        company_name = selector.xpath('//p[@class="company-name-t"]/a/text()').extract_first(default='N/A')
        recruit['company_name'] = company_name
        yield recruit