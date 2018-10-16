# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml
from .public import Arealist
from random import choice
class areadelete_meetingroom(mytest):

    # 删除区域
    # @unittest.skip('暂时跳过')

    def test_areadelete(self):

        # 删除区域
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        deldata={"actual_area_ids" :"[" + str(choice(Arealist())) + "]"}
        r = requests.post(url, headers=self.headers, data=deldata, stream=True)
        if "不允许删除使用中的区域" in str(r.json()):
            self.result = {"code" : 0}
        else:
            self.result = r.json()


if __name__ == '__main__':
    unittest.main()