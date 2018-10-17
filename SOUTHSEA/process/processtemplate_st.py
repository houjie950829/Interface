import unittest
import requests
from models import mytest
from models import MyYaml


class processtemplate_process(mytest):
    # 流程模板
    # @unittest.skip('暂时跳过')
    def test_process_tpl_list(self):
        # 流程模板——列表
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.result = r.json()

    # # @unittest.skip('暂时跳过')
    # def test_add_process_tpl(self):
    #     # 流程模板——添加
    #     url = MyYaml('SOUTHSEA').baseUrl + self.data[1][0]
    #     r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
    #     self.result = r.json()



if __name__ == '__main__':
    unittest.main()

