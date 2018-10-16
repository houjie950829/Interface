# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
import time
from random import randint
from datetime import date,timedelta

class addschedule_schedule(mytest):
    # 添加日程
    # @unittest.skip('暂时跳过')
    def test_addschedule(self):
        # 添加日程
        schedule_title = "日程标题" + str(randint(0, 9999))
        start_data = date.today() + timedelta(days=+2)
        meeting_time_day = int(time.mktime(time.strptime(str(start_data), '%Y-%m-%d')))
        starttime = str(meeting_time_day + 77400)
        meeting_time_h_i = str(int(starttime) + 3600)
        datatime = "".join([starttime, ",", meeting_time_h_i])
        value = self.data[1]['form_data'] % (schedule_title, datatime)
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data={"form_data":value}, stream=True)
        self.result = r.json()
        

if __name__ == '__main__':
    unittest.main()