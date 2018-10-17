# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from random import choice
from .public import Addmeeting,Meetinglist
class meetinginfo_meeting(mytest):

    # 会议详情（表单带模板数据）
    # @unittest.skip('暂时跳过')

    def test_meetinginfo(self):

        # 会议详情（表单带模板数据）

        del self.data[1]['meeting_id']
        self.data[1]['meeting_id'] = choice(Meetinglist())
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()
        

if __name__ == '__main__':
    unittest.main()