# coding=utf-8
import unittest
import time
import json
import socket
from models.readWritYmal import MyYaml
from models.MyDB import DB
import base64
import requests
from models.sendMail import Mail


class RunAll(object):
    def __init__(self):
        base_data = MyYaml().baseData
        dumps_data = json.dumps(base_data)
        encodestr = (base64.b64encode(dumps_data.encode('utf-8'))).decode('utf-8')
        insert_sql = MyYaml('insert_results').baseSql % encodestr
        self.select_sql = MyYaml('search_results').baseSql
        del_sql = MyYaml('del_results').baseSql
        self.up_sql = MyYaml('update_results').baseSql
        DB(del_sql).sql_db()
        DB(insert_sql).sql_db()
        data = DB(self.select_sql).sql_db()[0][0]
        self.dmp = json.loads((base64.b64decode(data)).decode('utf-8'))
        self.all_case_fun = []   # 所有测试用例方法名
        self.projectName = MyYaml('projectName').configYaml
        self.moudleName = MyYaml('moudleName').configYaml
        if self.moudleName is None:
            self.moudleName = ''
        self.matching = MyYaml('matching').configYaml
        self.ip = MyYaml('ip').configYaml
        self.port = MyYaml('port').configYaml
        self.ip_mobile = None
        self.all_cases = []  # 所有测试用例信息
        self.right_cases = []  # 正确的cases
        self.fail_cases = []  # 失败的cases
        self.error_cases = []  # 失败的cases
        self.skip_cases = []  # 跳过的cases
        self.app_config = MyYaml().interface_data
        self.insert_response = MyYaml('insert_response').baseSql
        self.search_response = MyYaml('search_response').baseSql
        self.del_response = MyYaml('del_response').baseSql
        self.insert_response = MyYaml('insert_response').baseSql
        DB(self.del_response).sql_db()

    def check_status(self):
        """ip检查"""
        hostname = socket.gethostname()
        my_ip = socket.gethostbyname(hostname)
        if self.ip is None:
            self.ip_mobile = my_ip
            return True
        elif self.ip == '127.0.0.1':
            self.ip_mobile = self.ip
            return True
        elif self.ip != my_ip:
            print('请检查填写ip和当前ip是否一致！')
            return False
        else:
            self.ip_mobile = my_ip
            return True

    def run_server(self):
        """启动django服务"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip_mobile, self.port))
            s.shutdown(2)
            # 利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
            # 该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
            print('%d is open' % self.port)
            return True
        except Exception:
            print('%d is down' % self.port)
            return False

    def run_case(self):
        if self.check_status():
            if self.run_server():
                startTime = time.time()
                now_time = time.strftime('%Y-%m-%d %H:%M:%S')
                discover = unittest.defaultTestLoader.discover('./{}/{}'.format(self.projectName, self.moudleName),
                                                               pattern=self.matching,
                                                               top_level_dir=None)
                for i in str(discover).split('testMethod='):
                    for j in i.split('>'):
                        if 'test_' in j:
                            self.all_case_fun.append(j)
                runner = unittest.TextTestRunner(verbosity=1)
                result = runner.run(discover)
                stopTime = time.time()
                end_time = time.strftime('%Y-%m-%d %H:%M:%S')
                timeTaken = '%d秒' % (stopTime - startTime)
                test_info = [now_time, end_time, timeTaken, result.testsRun, result.testsRun - len(result.skipped),
                             len(result.skipped)]
                self.dmp['test_info'] = test_info
                keys = list(self.app_config.keys())
                all_fun_data = []  # 所有测试用例的数据
                for a in keys:
                    for b in self.app_config[a]:
                        for c in b['funName']:
                            c['url'] = b['url']
                            all_fun_data.append(c)
                for case_id in self.all_case_fun:
                    case_info = {
                        'case_name': '',
                        'mode': '',
                        'api_url': '',
                        'statues': '',
                        'info': '',
                    }
                    for d in all_fun_data:
                        if case_id in list(d.keys()):
                            case_info['case_name'] = d[case_id]['case_name']
                            case_info['mode'] = d[case_id]['mode']
                            case_info['api_url'] = d['url']
                            break
                    for e in result.failures:
                        if case_id == str(e[0]).split(' (')[0]:
                            case_info['statues'] = 'fail'
                    for f in result.errors:
                        if case_id == str(f[0]).split(' (')[0]:
                            case_info['statues'] = 'error'
                            case_info['info'] = str(f[1])
                            break
                    for h in result.skipped:
                        if case_id == str(h[0]).split(' (')[0]:
                            case_info['statues'] = 'skip'
                            case_info['info'] = 'No Response'
                            break
                    if case_info['statues'] == '':
                        case_info['statues'] = 'pass'
                    case_data = DB(self.search_response).sql_db()
                    for i in case_data:
                        if i[0] == case_id:
                            case_info['info'] = base64.b64decode(i[1]).decode('utf-8')
                    case_infos = [
                        self.projectName,
                        case_id,
                        case_info['case_name'],
                        case_info['api_url'],
                        case_info['mode'],
                        case_info['statues'],
                        '详细',
                        case_info['info'],
                    ]
                    self.all_cases.append(case_infos)
                for g in self.all_cases:
                    if g[-3] == 'pass':
                        self.right_cases.append(g)
                    elif g[-3] == 'fail':
                        self.fail_cases.append(g)
                    elif g[-3] == 'error':
                        self.error_cases.append(g)
                    else:
                        self.skip_cases.append(g)
                self.dmp['report_cases']['all_cases'] = self.all_cases
                self.dmp['report_cases']['right_cases'] = self.right_cases
                self.dmp['report_cases']['fail_cases'] = self.fail_cases
                self.dmp['report_cases']['error_cases'] = self.error_cases
                self.dmp['report_cases']['untreaded_cases'] = self.skip_cases
                r = requests.post('http://{}:{}/polls/get_report/'.format(self.ip_mobile, self.port), json=self.dmp, stream=True)
                result = r.json()
                if result['code'] == 0:
                    mail = Mail(result['data']['report_dir'], './img/{}.png'.format(result['data']['report_name'].split('.')[0]), result['data']['report_url'])
                    mail.reportImg()
                    mail.send_mail()
            else:
                print('django服务没有启动！')
        else:
            print('请检查本机ip和配置ip是否一致！')


if __name__ == '__main__':
    RunAll().run_case()