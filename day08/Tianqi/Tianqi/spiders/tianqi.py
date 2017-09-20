# -*- coding: utf-8 -*-
import scrapy
import time

from Tianqi.items import TianqiItem

# ----1导入scrapy_redis爬虫类
from scrapy_redis.spiders import RedisSpider


# ----2修改类的继承
# class TianqiSpider(scrapy.Spider):
class TianqiSpider(RedisSpider):
    name = 'tianqi'
    # ----3注销允许的域以及起始的url
    # allowed_domains = ['lishi.tianqi.com']
    # start_urls = ['http://lishi.tianqi.com/']

    # ----4动态获取允许的域名
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(TianqiSpider, self).__init__(*args, **kwargs)

    # －－－－5设置redis_key
    redis_key = 'tianqi:start_urls'

    def parse(self, response):
        # print(response.body)
        # 解析起始的url对应的响应
        # 获取所有地区节点列表
        node_list = response.xpath('//*[@id="tool_site"]/div[2]/ul/li/a')
        # print(len(node_list))
        # 遍历节点列表
        for node in node_list:
            url = node.xpath('./@href').extract_first()
            area = node.xpath('./text()').extract_first()
            # print(area, url)
            # 过滤错误的url
            if url != '#':
                # 正确的url，则拿来发送请求
                yield scrapy.Request(url, callback=self.parse_area, meta={'meta_1': area})

    def parse_area(self, response):
        # 解析地区页面获取数据，发起请求
        # 获取meta传参
        area = response.meta['meta_1']
        # 获取详细页面链接列表
        url_list = response.xpath('//*[@id="tool_site"]/div[2]/ul/li/a/@href').extract()
        # print('=======', len(url_list), response.url)
        # 遍历url列表
        for url in url_list:
            # 发起详情页面请求
            yield scrapy.Request(url, callback=self.parse_data, meta={'meta_2': area})

    def parse_data(self, response):
        # 解析详情页面
        # 获取meta传参
        area = response.meta['meta_2']
        # 获取url
        url = response.url
        # 获取采集时间
        timestamp = time.time()
        # 获取数据节点列表
        node_list = response.xpath('//*[@id="tool_site"]/div[@class="tqtongji2"]/ul')
        # print('===========', len(node_list))
        # 遍历列表
        for node in node_list[1:]:  # 因为第一个节点不需要
            # 创建item对象，存储数据
            item = TianqiItem()
            # 抽取数据
            item['area'] = area
            item['url'] = url
            item['timestamp'] = timestamp
            # 日期
            try:
                item['datetime'] = node.xpath('./li[1]/a/text()').extract()[0]
            except:
                item['datetime'] = node.xpath('./li[1]/text()').extract_first()
            # 最高气温
            item['max_t'] = node.xpath('./li[2]/text()').extract_first()
            # 最低气温
            item['max_t'] = node.xpath('./li[3]/text()').extract_first()
            # 天气
            item['weather'] = node.xpath('./li[4]/text()').extract_first()
            # 风向
            item['wind_direction'] = node.xpath('./li[5]/text()').extract_first()
            # 风力
            item['wind_power'] = node.xpath('./li[6]/text()').extract_first()

            print(item)
            # 返回数据
            yield item
















