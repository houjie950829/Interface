# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
import time
from random import randint
from datetime import date,timedelta

class addroom_meetingroom(mytest):

    # 添加会议室
    # @unittest.skip('暂时跳过')

    def test_addroom(self):

        # 添加会议室
        meeting_time_day = str(int(time.time()))
        meeting_time_h_i = str(int(time.time() + 50000))
        datatime = "".join([meeting_time_day, ",", meeting_time_h_i])
        meeting_room_title = "会议室名称" + str(randint(0, 9999))
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        value = self.data[1]['form_data'] % (meeting_room_title, datatime)
        r = requests.post(url, headers=self.headers, data={"form_data": value}, stream=True)
        self.result = r.json()
        

if __name__ == '__main__':
    unittest.main()