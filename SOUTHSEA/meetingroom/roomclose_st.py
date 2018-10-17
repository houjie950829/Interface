# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from .public import Meetingroomslist
from random import choice

class roomclose_meetingroom(mytest):
    # 关闭会议室
    # @unittest.skip('暂时跳过')
    def test_roomclose(self):
        # 关闭会议室

        del self.data[1]['meeting_room_id']
        self.data[1]['meeting_room_id'] = choice(Meetingroomslist())
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()
        

if __name__ == '__main__':
    unittest.main()