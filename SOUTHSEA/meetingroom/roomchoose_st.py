# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from datetime import date

class roomchoose_meetingroom(mytest):

    # 选择会议室--获取会议列表
    # @unittest.skip('暂时跳过')
    def test_roomchoose(self):

        # 选择会议室--获取会议列表
        meeting_time_day = date.today()
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        del self.data[1]['meeting_time_day']
        self.data[1]['meeting_time_day'] = str(meeting_time_day)
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()
        

if __name__ == '__main__':
    unittest.main()