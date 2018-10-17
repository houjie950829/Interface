# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml


class meetingtpl_meeting(mytest):

    # 获取会议表单模板
    # @unittest.skip('暂时跳过')
    def test_meetingtpl(self):

        # 获取会议表单模板

        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()
        

if __name__ == '__main__':
    unittest.main()