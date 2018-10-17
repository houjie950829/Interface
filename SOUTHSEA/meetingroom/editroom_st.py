# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from random import randint,choice
from datetime import date,timedelta
import time
from .public import Meetingroomslist

class editroom_meetingroom(mytest):

    # 编辑会议室
    # @unittest.skip('暂时跳过')

    def test_editroom(self):

        # 编辑会议室
        meeting_time_day = str(int(time.time()))
        meeting_time_h_i = str(int(time.time() + 50000))
        datatime = "".join([meeting_time_day, ",", meeting_time_h_i])
        meeting_room_title = "编辑后的会议室名称" + str(randint(0, 9999))
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        value = self.data[1]['form_data'] % (meeting_room_title, datatime)
        editdata = {"meeting_id": choice(Meetingroomslist()), "form_data": value}
        r = requests.post(url, headers=self.headers, data= editdata , stream=True)
        self.result = r.json()

if __name__ == '__main__':
    unittest.main()