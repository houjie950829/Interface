# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from datetime import date,timedelta
import time
from random import randint,choice
from .public import Addschedule

class editschedule_schedule(mytest):
    # 编辑日程
    # @unittest.skip('暂时跳过')
    def test_editschedule(self):
        # 编辑日程

        schedule_title = "编辑后的日程标题" + str(randint(0, 9999))
        start_data = date.today() + timedelta(days=+2)
        meeting_time_day = int(time.mktime(time.strptime(str(start_data), '%Y-%m-%d')))
        starttime = str(meeting_time_day + 77400)
        meeting_time_h_i = str(int(starttime) + 3600)
        datatime = "".join([starttime, ",", meeting_time_h_i])
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        value = self.data[1]['form_data'] % (schedule_title, datatime)
        editdata = {"follow_id": Addschedule(), "form_data": value}
        r = requests.post(url, headers=self.headers, data=editdata, stream=True)
        self.result = r.json()



if __name__ == '__main__':
    unittest.main()