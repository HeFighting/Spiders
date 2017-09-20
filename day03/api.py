# coding=utf-8
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# 获取url对应的响应
def _get_page(url):
    # 私有函数，能内部调用，但不能被from api import * 导入
    response = requests.get(url, headers=headers)
    # print(response.content.decode())
    return response.content.decode()


def get_page(url):
    try:
        str_data = _get_page(url)
    except Exception as e:
        print(e)
        str_data = None

    return str_data





