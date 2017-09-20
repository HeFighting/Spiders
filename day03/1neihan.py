#coding=utf-8
import re
from day03.api import get_page

'''
<a target="_blank" class="image share_url" href=".*?".*?<p>.*?</p>
'''


class Neihan(object):
    def __init__(self):
        self.url = 'http://neihanshequ.com/'
        self.pattern = re.compile(r'<a target="_blank" class="image share_url" href="(.*?)".*?<p>(.*?)</p>', re.S)

    def parse_data(self, str_data):
        return self.pattern.findall(str_data)
        # 结果为[ (,), (,), (,)... ]

    def save_data(self, data_list):
        with open('neihan.txt','w') as f:
            for data in data_list:
                f.write(data[0]+'\n')
                f.write(data[1]+'\n')

    def run(self):
        str_data = get_page(self.url)
        data_list = self.parse_data(str_data)
        self.save_data(data_list)

if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()

















