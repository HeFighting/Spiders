#coding=utf-8

import requests
from lxml import etree
import os,sys
import json


class Tieba(object):
    def __init__(self, name):
        self.name = name
        self.url = 'https://tieba.baidu.com/f?kw=%s' %self.name
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0 '
        }

    # 获取url对应的响应
    def get_page(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            return response.content.decode()
        except:
            return None

    # 从列表页面解析出详情页面的连接和标题以及下一页的url
    def parse_datail_list(self, str_data):
        # 将html字符串转换为element对象
        html = etree.HTML(str_data)

        # 获取所有帖子的节点列表
        node_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')

        # 创建一个数据列表
        detail_list = []

        # 遍历节点列表
        for node in node_list:
            temp = {}
            temp['title'] = node.xpath('./text()')[0]
            temp['url'] = 'https://tieba.baidu.com/' + node.xpath('./@href')[0]
            detail_list.append(temp)

        try:
            next_url = html.xpath('//*[@id="frs_list_pager"]a[last()-1]/@href')
        except:
            next_url = None
        print(detail_list,next_url)

        return detail_list, next_url

    def parse_image(self, detail_data):
        html = etree.HTML(detail_data)
        # 获取所有图片链接
        image_list = html.xpath('//cc/div/img/@src')
        # print(image_list)

        return image_list

    def download(self, image_list):
        if not os.path.exists('images'):
            os.makedirs('images')
        for url in image_list:
            response = requests.get(url, self.headers)
            filename = 'images' + os.sep + url.split('/')[-1]
            with open(filename, 'wb') as f:
                f.write(response.content)

    def save_data(self, data):
        with open('tieba_p', 'a') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '.\n')

    def run(self):
        # url
        next_url = self.url
        while next_url:
            # 2.发送请求获取响应
            str_data = self.get_page(next_url)
            # 3.从响应中获取详细页面的链接和标题，下一页的url
            detail_list, next_url = self.parse_datail_list(str_data)

            # 4.遍历链接和标题列表
            for detail in detail_list:
                # 4.1发送请求，获取详细页面的响应
                url = detail['url']
                detail_data = self.get_page(url)
                # 4.2从响应中抽取数据（图片列表）
                image_list = self.parse_image(detail_data)
                detail['images'] = image_list
                # 4.3下载图片
                self.download(image_list)
                # 4.4保存数据
                self.save_data(detail)


if __name__ == '__main__':
    tieba = Tieba('美女')
    # tieba = Tieba(sys.argv[1])
    tieba.run()

