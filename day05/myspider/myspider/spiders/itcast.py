# -*- coding: utf-8 -*-
import scrapy

from myspider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['www.itcast.cn']
    # 修改其实的url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 获取所有老师信息的节点
        node_list = response.xpath('//div[@class="li_txt"]')
        # 遍历所有的教师节点
        data_list = []
        for node in node_list:
            # 创建存储数据的容器
            item = MyspiderItem()
            # 抽取数据，保存到item中
            item['name'] = node.xpath('./h3/text()').extract()[0]
            item['title'] = node.xpath('./h4/text()').extract()[0]
            item['desc'] = node.xpath('./p/text()').extract()[0]

            # 使用yield返回数据
            yield item
            # data_list.append(item)

        # return data_list


