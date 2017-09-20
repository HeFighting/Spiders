# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['fs.com
']
    start_urls = ['http://fs.com
/']

    def parse(self, response):
        pass
