#coding=utf-8
'''
<script>var props=({"activeInvestors|investor".*?"}}})</script>
'''
from day03.api import get_page
import re
import json


class Ker36(object):
    def __init__(self):
        self.url = 'http://36kr.com/'
        # self.pattern = re.compile(r'<script>var props=({"activeInvestors|investor".*?"}}})</script>')

    def parse_data(self, str_data):
        # result = self.pattern.findall(str_data)[0]
        # 因为是一个元组，故取第一个
        result = re.findall(r'<script>var props=({"activeInvestors\|investor".*?"}}})</script>', str_data)[0]
        result = re.sub(',locationnal={.*', '', result)
        my_dict = json.loads(result)['feedPostsLatest|post']
        return my_dict

    def save_data(self, data_dict):
        with open('36.json', 'w') as f:
            for data in data_dict:
                f.write(json.dumps(data, ensure_ascii=False)+',\n')

    def run(self):
        str_data = get_page(self.url)
        print(type(str_data))
        data_dict = self.parse_data(str_data)
        self.save_data(data_dict)


if __name__ == '__main__':
    ker36 = Ker36()
    ker36.run()

















