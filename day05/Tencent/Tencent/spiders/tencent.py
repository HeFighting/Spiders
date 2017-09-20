# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # 修改起始的url，可以有多个起始的url，直接在下面的列表中添加即可
    start_urls = ['http://hr.tencent.com/position.php']
    host = 'http://hr.tencent.com/'

    def parse(self, response):
        # 获取职位节点列表
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # 遍历所有的节点
        for node in node_list:
            # 创建一个摸版类的实例
            item = TencentItem()
            # 从每个节点中抽取数据，并放到item中
            item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['link'] = self.host + node.xpath('./td[1]/a/@href').extract()[0]
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['time'] = node.xpath('./td[5]/text()').extract()[0]
            # 将数据返回给引擎
            yield item

        # 翻页
        next_url = self.host + node.xpath('//*[@id="next"]/@href').extract()[0]
        # 使用url构建请求,下面的函数可以参考scrapy源码
        yield scrapy.Request(next_url, callback=self.parse)

