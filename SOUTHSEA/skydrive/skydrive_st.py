# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml


class skydrive_skydrive(mytest):
    # 网盘
    # @unittest.skip('暂时跳过')
    def test_net_disk_list(self):
        # 网盘列表
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data=self.data[3], stream=True)
        self.usetime = '%.2f' % r.elapsed.total_seconds ()
        self.result = r.json()
    # @unittest.skip('暂时跳过')
    def test_search_list(self):
        # 网盘搜索
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][1]
        r = requests.post(url, headers=self.headers, data=self.data[1][2], stream=True)
        self.usetime = '%.2f' % r.elapsed.total_seconds ()
        self.result = r.json()

if __name__ == '__main__':
    unittest.main()

