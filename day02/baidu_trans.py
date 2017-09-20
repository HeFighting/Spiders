#coding=utf-8
import requests
import json
import sys


class Baidu_trans(object):
    def __init__(self, word):
        self.word = word
        self.url = 'http://fanyi.baidu.com/v2transapi'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        self.post_data = {
            "from": "zh",
            "to": "en",
            "query": word,
            "transtype": "translang",
            "simple_means_flag": 3
        }

    def get_data(self):
        response = requests.get(self.url, headers=self.headers, data=self.post_data)
        return response.content.decode()

    def parse_data(self, data):
        result = json.loads(data)
        english_data = result['trans_result']['data'][0]['dst']
        print(self.word+"-------->"+english_data)

    def run(self):
        # url
        # 构建请求头
        # 构建post的数据
        # 发送请求获得响应
        data = self.get_data()
        self.parse_data(data)


if __name__ == '__main__':
    baidu = Baidu_trans(sys.argv[1])
    baidu.run()
