# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyspiderPipeline(object):
    def open_spider(self, spider):
        # 创建存储数据的文件
        self.file = open('itcast.json', 'w')

    def process_item(self, item, spider):
        # 将item实例转化成字典，将字典转化成字符串
        result = json.dumps(dict(item), ensure_ascii=False) + '.\n'
        # 写入文件
        self.file.write(result)
        return item

    def close_spider(self, spider):
        # 关闭存储数据的容器
        self.file.close()
