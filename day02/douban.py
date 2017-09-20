#coding=utf-8

import requests
import json

class Douban(object):
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=50"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode()

    def parse_data(self, data):
        result = json.loads(data)
        movie_dict = result['subject_collection_items']

        data_list = []
        # 遍历电影列表，从每一个电影信息中拿到数据
        for movie in movie_dict:
            temp = {}
            temp['url'] = movie['url']
            temp['title'] = movie['title']
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        with open('douban.json', 'w') as f:
            for data in data_list:
                result = json.dumps(data, ensure_ascii=False) + ',\n'
                # ensure_ascii表示转码
                f.write(result)

    def run(self):
        data = self.get_data()
        data_list = self.parse_data(data)
        self.save_data(data_list)

if __name__ == '__main__':
    douban = Douban()
    douban.run()













