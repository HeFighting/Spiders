#coding-utf-8

import requests
import sys


class Tieba(object):
    '''
    贴吧类
    '''
    def __init__(self, tieba_name, pn):
        self.tieba_name = tieba_name
        self.url = 'http://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(tieba_name)
        self.url_list = [self.url + str(i*50) for i in range(pn)]
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def get_page(self, url):
        '''
        获取URL对应的响应
        '''
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_data(self, data, number):
        filename = self.tieba_name + "_" + str(number+1) + '.html'
        with open(filename, 'w') as f:
            f.write(data)

    def run(self):
        for url in self.url_list:
            data = self.get_page(url)
            number = self.url_list.index(url)
            self.save_data(data, number)


if __name__ == '__main__':
    # name = sys.argv[1]
    # pn = sys.argv[2]

    tieba = Tieba('长城', int(10))
    tieba.run()
