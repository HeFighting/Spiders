#coding=utf-8
import json

import requests
import sys


class Baidu_Trans(object):
    def __init__(self, word):
        self.word = word
        self.url = 'http://fanyi.baidu.com/v2transapi'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        self.post_data = {
            'from': 'zh',
            'to': 'en',
            'query': word,
            'transtype': 'translang',
            'simple_means_flag': 3
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.post_data)
        return response.content.decode()

    def parse_data(self, data):
        result = json.loads(data)
        English_data = result['trans_result']['data'][0]['dst']
        print(self.word+'----->'+English_data)

    def run(self):
        data = self.get_data()
        self.parse_data(data)

if __name__ == '__main__':
    # baidu = Baidu_Trans(sys.argv[1])
    baidu = Baidu_Trans('中国')
    baidu.run()

























