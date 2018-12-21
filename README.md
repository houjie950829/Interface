# SCRM接口自动化测试
<div align=center><img src="https://marketing.scrm365.cn/static/lib/image/logo.png"/></div>
## 框架说明
        1、本框架主要为做接口测试准备的自动化测试框架
        2、框架使用requests作为接口请求
        3、框架对unittest进行定制
        4、采用全新模版引擎，增加报表和返回结果，使测试结果更直观
        5、结合django使框架更具扩展性
## 用例实例

```
# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml


class contacts_contact(mytest):
    # 联系人列
    # @unittest.skip('暂时跳过')
    def test_contacts(self):
        # 联系人列
        url = MyYaml('SCRM').baseUrl + self.data[0]
        r = requests.post(url, headers=self.headers, data=self.data[1], stream=True)
        self.usetime = '%.2f' % r.elapsed.total_seconds ()
        self.result = r.json()


if __name__ == '__main__':
    unittest.main()
```
1、环境所需模块：requests、django、selenium、PyYAML、bottle、pillow
2、Lib中添加.pth(内容为项目路径)
