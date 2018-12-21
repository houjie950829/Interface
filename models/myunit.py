# coding=utf-8
import unittest
import json
from . Myloging import Loging
from . readWritYmal import MyYaml
from . read_write_ini import read_ini
from . results import results
from . MyDB import DB
import base64


# noinspection PyGlobalUndefined,PyGlobalUndefined
def case_id():
    global case_count
    case_count += 1
    if case_count <= 9:
        count = "00" + str(case_count)
    elif case_count <= 99:
        count = "0" + str(case_count)
    else:
        count = str(case_count)
    return count

# noinspection PyRedeclaration,PyRedeclaration,PyGlobalUndefined


class mytest(unittest.TestCase):
    log = Loging()

    global case_count
    case_count = 0

    # noinspection PyGlobalUndefined
    global image_count
    image_count = 0

    # 计算测试用例的个数，用于显示在测试报告中
    @classmethod
    def setUpClass(self):
        try:
            self.token = read_ini()  # 从配置文件获取token
        except Exception:
            self.token = '0'
        self.headers = {'Authorization': self.token,
                        'charset': 'UTF-8'
                        }

    @classmethod
    def tearDownClass(cls):
        # print('测试类运行结束！')
        return

    def setUp(self):
        # print("开始执行用例:case_" + str(case_id()))
        self.className = self.__class__.__name__
        self.case_info = self._testMethodName
        self.key = self.className.split('_')[1]
        self.datas = MyYaml().interface_data[self.key]
        self.insert_response = MyYaml('insert_response').baseSql
        self.data = []
        for i in self.datas:
            if i['className'] == self.className:
                self.data.append(i['url'])   #  0
                for j in i['funName']:
                    for k in j.keys():
                        if k == self.case_info:
                            self.data.append(j[self.case_info]['bar'])  # 参数    1
                            self.data.append(j[self.case_info]['result'])  # 预期结果      2
                            self.data.append(j[self.case_info]['test_data'])  # 预期结果       3

    def tearDown(self):
        Resonse = results (
            expected=self.data[2][0],
            actual=self.result['code'],
            parameter=self.data[1],
            Results=self.result,
            time_count=self.usetime
            # usetime=self.usetime,
        )
        Resonse = json.dumps(Resonse, indent=4)
        Resonse = (base64.b64encode(Resonse.encode('utf-8'))).decode('utf-8')
        DB(self.insert_response % (self.case_info, Resonse)).sql_db()
        self.log.debug('%s->%s：%s' % (self.className, self.case_info, self.result))
        self.assertEqual(self.result['code'], self.data[2][0], msg=self.result.get('msg'))
        # print("用例执行结束。。。")

