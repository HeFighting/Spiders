# coding=utf-8
import redis
from pymongo import MongoClient
import json


# 链接redis
redis_cli = redis.Redis(host='192.168.71.50', port=6379, db=0)


# 链接mongodb
handle = MongoClient('127.0.0.1', 27017)
db = handle['Tianqi']
col = db['tianqi']

# 循环读取写入操作
while True:
    # 从redis中使用key获取数据，返回能够获取数据的key及对应的数据
    source, data = redis_cli.blpop(['tianqi:items'])
    # print(type(data))
    # 将数据转换成python字典
    result = json.loads(data.decode())
    print('---------', result)
    col.insert(result)


















