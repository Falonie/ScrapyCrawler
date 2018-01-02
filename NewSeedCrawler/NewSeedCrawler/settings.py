# -*- coding: utf-8 -*-

# Scrapy settings for NewSeedCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'NewSeedCrawler'

SPIDER_MODULES = ['NewSeedCrawler.spiders']
NEWSPIDER_MODULE = 'NewSeedCrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'NewSeedCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Cookie':'__uid=7708072285; ASP.NET_SessionId=l3ey4acdym3sk2mjtjmxn5rd; ARRAffinity=197ae5372184c64aeca47f780a2e053f3a50366e2bda392cd4bfa3b38e39a929; __utmt=1; pedaily.cn=uid=201531&username=18516630543&password=9724D8CA473B50D9B007DAE52181AFD7&email=&mobile=18516630543&oauth_token=&oauth_token_secret=&unionid=&hiname=%E6%96%B0%E8%8A%BD%E7%BD%91%E5%8F%8B721531&photo=&blogurl=&usertype=0&companyid=0&logintype=12&roletype=0&ismobilevalidated=True&isemailvalidated=False&isverified=False&isok=False; zg_did=%7B%22did%22%3A%20%2216077ad63fc158-017288883860d9-464a0129-e1000-16077ad63fd5b%22%7D; zg_2804ec8ba91741c0853e364274858816=%7B%22sid%22%3A%201514039159533%2C%22updated%22%3A%201514039301129%2C%22info%22%3A%201513836340233%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22201531%22%7D; __utma=117171865.1601227618.1513836341.1513844920.1514039160.4; __utmb=117171865.6.10.1514039160; __utmc=117171865; __utmz=117171865.1513836341.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_155833ecab8e70af6f2498f897bd8616=1513836341; Hm_lpvt_155833ecab8e70af6f2498f897bd8616=1514039301; Hm_lvt_25919c38fb62b67cfb40d17ce3348508=1513836341; Hm_lpvt_25919c38fb62b67cfb40d17ce3348508=1514039301; jiathis_rdc=%7B%22http%3A//www.newseed.cn/project/62156%22%3A2011253638%2C%22http%3A//www.newseed.cn/project/60542%22%3A2011257378%2C%22http%3A//www.newseed.cn/project/62125%22%3A2011682665%2C%22http%3A//www.newseed.cn/project/60764%22%3A2012244764%2C%22http%3A//www.newseed.cn/project/62166%22%3A0%7C1513840746846%2C%22http%3A//www.newseed.cn/project/19595%22%3A%220%7C1514039301420%22%7D'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'NewSeedCrawler.middlewares.NewseedcrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'NewSeedCrawler.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'NewSeedCrawler.pipelines.NewseedcrawlerPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
