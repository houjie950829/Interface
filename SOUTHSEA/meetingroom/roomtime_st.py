# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from .public import Meetingroomslist
from random import choice
from datetime import date
class roomtime_meetingroom(mytest):

    # 检查会议室占用情况
    # @unittest.skip('暂时跳过')

    def test_roomtime(self):

        # 检查会议室占用情况
        end_data = date.today()
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        del self.data[1]['meeting_room_id'],self.data[1]['date']
        self.data[1]['meeting_room_id'] = choice(Meetingroomslist())
        self.data[1]['date'] = str(end_data)
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()

if __name__ == '__main__':
    unittest.main()