# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from random import randint
class areaupdate_meetingroom(mytest):

    # 添加/更新区域
    # @unittest.skip('暂时跳过')

    def test_areaupdate(self):

        # 添加/更新区域
        actual_area_name = "区域名称" + str(randint(0,9999))
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        del self.data[1]['actual_area_name']
        self.data[1]['actual_area_name'] = actual_area_name
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()

if __name__ == '__main__':
    unittest.main()