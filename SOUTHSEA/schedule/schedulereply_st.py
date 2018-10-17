# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from .public import Addschedule
from random import randint
class schedulereply_schedule(mytest):

    # 日程回复
    # @unittest.skip('暂时跳过')

    def test_schedulereply(self):

        # 日程回复
        contents = "回复内容数据" + str(randint(0,9999))
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        del self.data[1]['follow_id'],self.data[1]['content']
        self.data[1]['follow_id'] = Addschedule()
        self.data[1]['content'] = contents
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()


if __name__ == '__main__':
    unittest.main()