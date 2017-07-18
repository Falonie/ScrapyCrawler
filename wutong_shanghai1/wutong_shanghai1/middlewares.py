# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.conf import settings
import random, json


class WutongShanghai1SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleware(object):
    # IP_list = settings['IP_LIST']

    # def __init__(self):
    # pool = []
    # pool2 = []
    # with open('ip3.txt', 'r') as f:
    #     for i in f.readlines():
    #         lines = json.loads(i)
    #         line = lines['RESULT']
    #         for l in line:
    #             ip = ':'.join((l.get('ip'), l.get('port')))
    #             # print(l, type(l), l.get('ip'), l.get('port'))
    #             pool.append(l.get('ip'))
    #             pool2.append(ip)
    #             return pool2

    with open('E:\ip6.txt', 'r') as f:
        # for line in f.readlines():
        #     print(line.strip())
        lines = ['http://' + l.strip() for l in f.readlines()]

    def process_request(self, request, spider):
        ip = random.choice(self.lines)
        request.meta['proxy'] = ip

# class UAMiddleware(object):
#     UA_list = settings['User_Agent_List']
#
#     def process_request(self, request, spider):
#         ua = random.choice(self.UA_list)
#         request.headers['User-Agent'] = ua