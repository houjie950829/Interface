# coding=utf-8
import unittest
import requests
from models import mytest, write_ini, MyYaml


class TestLogin_skydrive(mytest):
    # 登录

    def test_login_skydrive(self):
        # 正常登录
        url = MyYaml('SOUTHSEA').baseUrl + self.data[0]
        if isinstance(self.data[1], list):
            for num in range(len(self.data[1])):
                self.log.debug('登录账号：%s' % self.data[1][num])
                r = requests.post(url, data=self.data[1][num], stream=True)
                self.usetime = '%.2f' % r.elapsed.total_seconds ()
                self.result = r.json()
                self.log.debug('登录返回信息：%s' % self.result)
                if self.result['code'] == self.data[2][0]:
                    try:
                        result_list = self.result['data']['token']
                        write_ini(child='token%s' % str(num), content=result_list)  # 写入配置文件
                    except Exception as msgs:
                        print(msgs)
                else:
                    self.log.debug('登录失败：%s' % self.result)
        else:
            r = requests.post(url, data=self.data[1], stream=True)
            self.usetime = '%.2f' % r.elapsed.total_seconds ()
            self.result = r.json()
            if self.result['code'] == self.data[2][0]:
                try:
                    result_list = self.result['self.data']['token']
                    write_ini(content=result_list)  # 写入配置文件
                except Exception:
                    pass
            else:
                self.log.debug('登录失败：%s' % self.result)


if __name__ == '__main__':
    unittest.main()
