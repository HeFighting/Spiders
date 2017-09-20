# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Douban.items import DoubanItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 获取所有电影节点
        node_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]')
        print('------', len(node_list))
        # 遍历节点列表
        for node in node_list:
            # 创建item对象
            item = DoubanItem()
            # 从节点中获取数据保存到item中
            item['name'] = node.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['score'] = node.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['info'] = ''.join([i.strip() for i in node.xpath('./div[2]/p[1]/text()').extract()]).replace('\xa0', '')
            item['desc'] = node.xpath('./div[2]/p[2]/span/text()').extract_first()

        # 返回数据
        yield item















