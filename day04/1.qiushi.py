#coding=utf-8
import requests
from lxml import etree
import json


class Qiubai(object):
    def __init__(self):
        self.url = "https://www.qiushibaike.com/hot/page/{}/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        self.host = "https://www.qiushibaike.com"

    # 生成url列表
    def generate_list(self):
        print('生成url列表')
        url_list = [self.url.format(i) for i in range(1, 14)]
        return url_list

    # 获取url对应的响应
    def get_page(self, url):
        print('开始获取%s的响应'%url)
        try:
            response = requests.get(url, headers=self.headers)
            return response.content.decode()
        except:
            return None

    # 提取数据
    def parse_data(self, str_data):
        print('开始解析数据')
        # 将html字符串转换为element对象
        html = etree.HTML(str_data)
        # 获取节点列表
        node_list = html.xpath('//div[@id="content-left"]/div')
        # 创建一个储存字典数据的容器
        data_list = []

        for node in node_list:
            temp = {}
            # 从每一个节点中抽取数据
            try:
                temp['user'] = node.xpath('./div[1]/a[2]/h2/text()')[0].strip()
                temp['zone_link'] = self.host + node.xpath('./div[1]/a[2]/@href')[0]
                temp['age'] = node.xpath('./div[1]/div/text()')[0]
                temp['gender'] = node.xpath('./div[1]/div/@class')[0]
            except:
                temp['user'] = '匿名用户'
                temp['zone_link'] = None
                temp['age'] = None
                temp['gender'] = None
            if temp['gender'] == None:
                pass
            elif 'women' in temp['gender']:
                temp['gender'] = 'women'
            else:
                temp['gender'] = 'man'

            temp['content'] = node.xpath('./a[1]/div/span/text()')[0].strip()
            temp['url'] = self.host + node.xpath('./a[1]/@href')[0]
            data_list.append(temp)

        return data_list

    def save_data(self, data_list):
        print('开始存储文件')
        with open('qiushi.json','a') as f:  # a表示追加内容
            for data in data_list:
                result = json.dumps(data, ensure_ascii=False) + ',\n'  # 将json数据转换为字符串
                f.write(result)

    def run(self):
        # 1.生成url列表
        url_list = self.generate_list()
        # 2.遍历列表
        for url in url_list:
            str_data = self.get_page(url)
            data_list = self.parse_data(str_data)
            self.save_data(data_list)


if __name__ == '__main__':
    qiubai = Qiubai()
    qiubai.run()















