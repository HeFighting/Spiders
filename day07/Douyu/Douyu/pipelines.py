# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline  # 导入图片管道
from scrapy.utils.project import get_project_settings  # 第三中获取文件配置参数的方法
import scrapy
import os


class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item


class Images(ImagesPipeline):
    # 从setting文件中获取图片存放路径
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    # 发起需要下载的媒体文件请求
    def get_media_requests(self, item, info):
        # return [Request(x) for x in item.get(self.images_urls_field, [])]
        # print('=============', item['image_link'])
        yield scrapy.Request(item['image_link'])

    # 获取需要下载媒体文件的信息
    def item_completed(self, results, item, info):
        # if isinstance(item, dict) or self.images_result_field in item.fields:
        #     item[self.images_result_field] = [x for ok, x in results if ok]
        # return item
        # print('----', results)
        images = [data['path'] for ok,data in results]

        old_name = self.IMAGES_STORE + images[0]
        new_name = self.IMAGES + images[0].split(os.sep)[0] + os.sep + item['name'] + '.jpg'

        # 改名
        os.renames(old_name, new_name)

        return item










