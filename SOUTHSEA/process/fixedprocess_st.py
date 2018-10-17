import unittest,time,random
from SOUTHSEA.process.public import *
from models import mytest
from models import MyYaml


class fixedprocess_process(mytest):
    # 固定流程
    # @unittest.skip('暂时跳过')
    def test_add_fix_route(self):
        # 固定流程——添加
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        t = get_list_process()
        y = get_member_id()
        if t[0] is not False:
            if y is not False:
                id_y = random.sample(y,5)
                id_t = random.sample(t,1)
                self.data[1]['fix_name'] = '新增名称{}'.format(random.randint(1, 100000) + time.time())
                self.data[1]['type_id'] = str(id_t)[1:-1]
                self.data[1]['used_range'] = str(id_y)[1:-1]
                self.data[1]['edit_auth'] = random.randint(1,2)
                r = requests.post(url, headers = self.headers, data = self.data[1])
                self.result = r.json()
            else:
                self.result = y[1]
        else:
            self.result = t[1]

    # # @unittest.skip('暂时跳过')
    # def test_fix_route_list(self):
    #     # 固定流程——列表
    #     url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
    #     r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
    #     self.result = r.json()
    #     print(self.result)


if __name__ == '__main__':
    unittest.main()



