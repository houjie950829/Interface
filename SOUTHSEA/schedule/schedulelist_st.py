# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from datetime import date,timedelta

class schedulelist_schedule(mytest):

    # 获取日程列表
    # @unittest.skip('暂时跳过')

    def test_schedulelist(self):
        # 获取日程列表
        startdata = date.today()
        enddata = date.today() + timedelta(days=+6)
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        del self.data[1]["start_time"],self.data[1]["end_time"]
        self.data[1]["start_time"] = str(startdata)
        self.data[1]["end_time"] = str(enddata)
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()

        

if __name__ == '__main__':
    unittest.main()