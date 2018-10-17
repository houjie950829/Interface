import unittest
from models import mytest
from SOUTHSEA.process.public import *


class Fixedprocessserver_process(mytest):
    # 流程服务
    # @unittest.skip('暂时跳过')
    def test_do_add_ann(self):
        # 固定流程服务——添加类型
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()

    # @unittest.skip('暂时跳过')
    def test_type_list(self):
        # 固定流程服务——列表类型
        url=MyYaml('SOUTHSEA').baseUrl+self.data[1][0]
        r=requests.post(url,headers=self.headers,data=self.data[1][1],stream=True)
        self.result=r.json()

    # @unittest.skip('暂时跳过')
    def test_del_fix_route_type(self):
        # 固定流程服务——删除类型
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
        t = get_list_process()
        if t[0] is not False:
            for i in range(len(t)):
                self.data[1][1]['type_id'] = t[i]
                r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
                self.result = r.json()
                if i is 2:
                    break
        else:
            self.result = t[1]

    # @unittest.skip('暂时跳过')
    def test_edit_fix_route_type(self):
        # 固定流程服务——编辑类型
        url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
        t = get_list_process()
        if t[0] is not False:
            for i in range(len(t)):
                self.data[1][1]['type_id'] = t[i]
                r = requests.post(url, headers=self.headers, data=self.data[1][1], stream=True)
                self.result = r.json()
                if i is 2:
                    break
        else:
            self.result = t[1]

if __name__ == '__main__':
    unittest.main()


