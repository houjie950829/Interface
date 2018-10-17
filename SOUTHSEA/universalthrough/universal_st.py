import unittest
import random
from models import mytest
from datetime import datetime
from SOUTHSEA.universalthrough.public import *


class universal_universalthrough(mytest):
    # 百事通
    # @unittest.skip('暂时跳过')
    def test_do_add_ann(self):
        # 百事通——添加
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        self.data[1]['title'] = '测试标题{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
        self.data[1]['content'] = '这是自动化测试哒内容{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()

    # @unittest.skip('暂时跳过')
    def test_announce_list(self):
        # 百事通——列表(权限)
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
        r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
        self.result = r.json()

    # @unittest.skip('暂时跳过')
    def test_lower_frame_Ann(self):
        # 百事通——下架
        y = get_universal_through_list()
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
        if y[0] is not False:
            for i in range(len(y)):
                self.data[1][1]["announce_id"] = y[i]
                r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
                if r.json().get('code') is 0:
                    self.result = r.json()
                elif r.json().get('msg') == '百事通已经下架':
                    id = self.data[1][1]["announce_id"]
                    y_id = del_universal_through(id)
                    if y_id is True:
                        return self.test_lower_frame_Ann()
                    else:
                        self.result = y_id
                if i is 2:
                    break
        else:
            self.result = y[1]

    # @unittest.skip('暂时跳过')
    def test_do_del_ann(self):
        #百事通——删除
        y = get_universal_through_list()
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0] # 删除的url
        if y[0] is not False:
            for i in range(len(y)):
                self.data[1][1]["announce_id"] = y[i]
                r=requests.post(url,headers=self.headers,data=self.data[1][1],stream=True)
                self.result=r.json()
                if i is 2:
                    break
        else:
            self.result = y[1]

    # @unittest.skip('暂时跳过')
    def test_announce_sort(self):
        # 百事通——排序(个人排序)
        y = self_list_id()
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
        if y[0] is not False:
            n = ''.join(str(y)[1:-1])
            m = random.sample(range(1,len(y) + 1),len(y))
            self.data[1][1]["announce_ids"] = n
            self.data[1][1]["sorts"] = str(m)[1:-1]
            r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
            self.result = r.json()
        else:
            self.result = y[1]

    # @unittest.skip('暂时跳过')
    def test_publish(self):
        #百事通——发布
        url=MyYaml('SOUTHSEA').baseUrl+self.data[1][0]
        y = self_list_id()
        if y[0] is not False:
            for i in range(len(y)):
                self.data[1][1]["announce_id"] = y[i]
                r=requests.post(url,headers=self.headers,data=self.data[1][1],stream=True)
                self.result=r.json()
                if i == 2:
                    break
        else:
            self.result = y[1]

    # @unittest.skip('暂时跳过')
    def test_manageAnnounce(self):
        # 百事通——列表(后台)
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
        r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
        self.result = r.json()

    # @unittest.skip('暂时跳过')
    def test_logList(self):
        # 百事通——操作记录
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
        y = self_list_id()
        if y[0] is not False:
            for i in range(len(y)):
                self.data[1][1]["announce_id"] = y[i]
                r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
                self.result = r.json()
                if i == 2:
                    break
        else:
            self.result = y[1]

    # @unittest.skip('暂时跳过')
    def test_do_edit_ann(self):
        # 百事通——编辑
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
        y = self_list_id()
        if y[0] is not False:
            for i in range(len(y)):
                self.data[1][1]["announce_id"] = y[i]
                self.data[1][1]['title'] = '测试编辑标题{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
                self.data[1][1]['content'] = '这是自动化测试哒内容哒编辑哒内容{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
                r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
                self.result = r.json()
                if i is 1:
                    break
        else:
            self.result = y[1]

    # @unittest.skip('暂时跳过')
    def test_details(self):
        #百事通——详情
        url=MyYaml('SOUTHSEA').baseUrl+self.data[1][0]
        y = self_list_id()
        if y[0] is not False:
            for i in range(len(y)):
                self.data[1][1]["announce_id"] = y[i]
                r=requests.post(url,headers=self.headers,data=self.data[1][1],stream=True)
                self.result=r.json()
                if i is 2:
                    break
        else:
            self.result = y[1]


if __name__ == '__main__':
    unittest.main()


