# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/']

    def parse(self, response):
        with open('renren.html','wb') as f:
            f.write(response.body)
