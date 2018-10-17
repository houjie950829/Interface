# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
import time
from random import randint
from datetime import date,timedelta

class meetingconflict_meeting(mytest):

    # 判断冲突
    # @unittest.skip('暂时跳过')
    def test_meetingconflict(self):

        # 判断冲突

        start_data = date.today() + timedelta(days=+2)
        time_now = time.mktime(time.strptime(str(start_data), '%Y-%m-%d'))
        meeting_time_day = int(time.mktime(time.strptime(str(start_data), '%Y-%m-%d')))
        starttime = str(meeting_time_day + 77400)
        meeting_time_h_i = str(int(starttime) + 3600)
        datatime = "".join([starttime, ",", meeting_time_h_i])
        del self.data[1]['meeting_time_day'],self.data[1]['meeting_time_h_i']
        self.data[1]['meeting_time_day'] = meeting_time_day
        self.data[1]['meeting_time_h_i'] = datatime
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()
        

if __name__ == '__main__':
    unittest.main()