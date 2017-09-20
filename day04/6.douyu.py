#coding=utf-8
import json

from selenium import webdriver


class DouYu(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.douyu.com/directory/all')

    def parse_data(self):
        # 获取所有房间节点
        node_list = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li/a')

        # 遍历节点列表,获取数据
        data_list = []
        for node in node_list:
            temp = {}
            temp['owner'] = node.find_element_by_xpath('./div/p/span[1]').text
            temp['title'] = node.find_element_by_xpath('./div/div/h3').text3
            temp['category'] = node.find_element_by_xpath('./div/div/span').text
            temp['num'] = node.find_element_by_xpath('./div/p/span[2]').text
            temp['cover'] = node.find_element_by_xpath('./span/img').get_attribute('src')
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        with open('douyu.json', 'a') as f:
            for data in data_list:
                result = json.dumps(data, ensure_ascii=False) + ',\n'
                f.write(result)

    def __del__(self):
        self.driver.close()

    def run(self):
        while True:
            data_list = self.parse_data()
            self.save_data(data_list)
            # 定位到下一页节点,模拟点击,如果捕获错误则表明到达最后一页
            '''
            斗鱼直播的url是动态加载的,点击下一页后,页面上的url地址不会发生改变,故需要本例采取的这种方法获取数据
            '''
            try:
                el_next = self.driver.find_element_by_xpath('//a[class="shark-pager-next"]')
                el_next.click()
            except:
                break


if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()







