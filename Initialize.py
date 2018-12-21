# coding=utf-8
from models import MyYaml
import os

login = """# coding=utf-8
import unittest
import requests
from models import mytest, write_ini, MyYaml


class {}(mytest):
    # {}

    def {}(self):
        # {}
        url = MyYaml('{}').baseUrl + self.data[0]
        if isinstance(self.data[1], list):
            for num in range(len(self.data[1])):
                self.log.debug('登录账号：%s' % self.data[1][num])
                r = requests.{}(url, {}=self.data[1][num], stream=True)
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
            r = requests.{}(url, {}=self.data[1], stream=True)
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
"""

interface_title = """# coding=utf-8
import unittest
import requests
from models import mytest
from models import MyYaml


class {}(mytest):
    # {}"""

interface_body = """
    # @unittest.skip('暂时跳过')
    def {}(self):
        # {}
        url = MyYaml('{}').baseUrl + self.data[0]
        r = requests.{}(url, headers=self.headers, {}=self.data[1], stream=True)
        self.usetime = '%.2f' % r.elapsed.total_seconds ()
        self.result = r.json()
        """

interface_end = """

if __name__ == '__main__':
    unittest.main()"""


class GetFile(object):
    def __init__(self):
        self.projectName = MyYaml('projectName').configYaml
        self.base_dir = os.getcwd() + '/{}/'.format(self.projectName)
        self.base_yaml = self.base_dir + 'config.yaml'
        if os.path.exists(self.base_yaml):
            self.data = MyYaml().interface_data
            self.keys = list(self.data.keys())
            self.result_list_login = []
            self.result_list = []
            self.file_list_login = []
            self.file_list = []

    def initialization_data(self):
        if os.path.exists(self.base_yaml):
            for key in self.keys:
                for a in self.data[key]:
                    if 'Login' in a['className'] or 'login' in a['className']:
                        for b in a['funName']:
                            funName = list(b.items())
                            del a['funName']
                            a['funName'] = funName
                            self.result_list_login.append(a)
                    else:
                        for b in a['funName']:
                            funName = list(b.items())
                            del a['funName']
                            a['funName'] = funName
                            self.result_list.append(a)
            for i in self.result_list_login:
                for j in i['funName']:
                    file = login.format(i['className'], i['name'], j[0], j[1]['case_name'], self.projectName, j[1]['mode'], j[1]['re_bar'],
                                        j[1]['mode'], j[1]['re_bar'])
                    dir_name = i['className'].split('_')[1]
                    file_name = 'A_login_st.py'
                    base_ini = self.base_dir + 'config.ini'
                    dir_dir = os.getcwd() + '/{}/{}/'.format(self.projectName, dir_name)
                    dir_file = dir_dir + file_name
                    dir_init = dir_dir + '__init__.py'
                    dir_public = dir_dir + 'public.py'
                    if not os.path.exists(self.base_dir):
                        os.mkdir(self.base_dir)

                    if not os.path.exists(base_ini):
                        with open(base_ini.split('.')[0] + '.txt', 'w', encoding='utf-8') as f:
                            f.write('[session]')
                        f.close()
                        os.rename(base_ini.split('.')[0] + '.txt', base_ini)

                    if not os.path.exists(dir_dir):
                        os.mkdir(dir_dir)

                    if not os.path.exists(dir_file):
                        with open(dir_file.split('.')[0] + '.txt', 'w', encoding='utf-8') as f:
                            f.write(file)
                        f.close()
                        os.rename(dir_file.split('.')[0] + '.txt', dir_file)

                    if not os.path.exists(dir_init):
                        t = open(dir_init, 'w')
                        t.close()

                    if not os.path.exists(dir_public):
                        g = open(dir_public, 'w')
                        g.close()

            for i in self.result_list:
                file_title = interface_title.format(i['className'], i['name'])
                file_end = interface_end
                file_list = ''
                for j in i['funName']:
                    file_body = interface_body.format(j[0], j[1]['case_name'], self.projectName, j[1]['mode'], j[1]['re_bar'])
                    file_list = file_list + file_body
                body = file_title + file_list + file_end
                dir_name = i['className'].split('_')[1]
                file_name = '{}_st.py'.format(i['className'].split('_')[0])
                dir_dir = os.getcwd() + '/{}/{}/'.format(self.projectName, dir_name)
                dir_file = dir_dir + file_name
                if not os.path.exists(dir_file):
                    with open(dir_file.split('.')[0] + '.txt', 'w', encoding='utf-8') as f:
                        f.write(body)
                    f.close()
                    os.rename(dir_file.split('.')[0] + '.txt', dir_file)

                elif os.path.exists(dir_file):
                    with open(dir_file, encoding='utf-8') as k:
                        r = k.read()
                        import re
                        _re = re.findall('def.*test_.*',file_list)
                        yx = ''.join(file_list.strip().split())
                        for _ in _re:
                            if str(_) not in r:
                                yo = ''.join(str(_).strip().split())
                                if str(yo) in yx:
                                    def_name = str(_)
                                    case_name = yx.split(str(yo))[1][:-134]
                                    url = yx.split(str(yo))[1][-134:-91]
                                    requests  = yx.split(str(yo))[1][-91:-20]
                                    result = yx.split(str(yo))[1][-20:]
                                    data = '    ' + "# @unittest.skip('暂时跳过')" + '\n' + '    ' + def_name + '\n' +\
                                           '        ' + case_name + '\n' + '        ' + url + '\n'  + '        ' + \
                                           requests + '\n' + '        ' + result
                                    with open(dir_file , 'at' , encoding='utf-8') as f:
                                        f.writelines(data)
                                    f.close()



        else:
            print('请先创建config.yaml文件！')


if __name__ == '__main__':
    GetFile().initialization_data()