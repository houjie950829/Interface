# *-*coding:utf-8*-*

"""
@version: Python3.4.4
@author: Hszhang
@time: 2017/6/14 16:34

- 使用bottle来动态生成html
    - https://www.reddit.com/r/learnpython/comments/2sfeg0/using_template_engine_with_python_for_generating/

"""

from bottle import template
import webbrowser
# from models.readWritYmal import MyYaml
import sys

html_template = u"""
<?xml version="1.0" encoding="UTF-8"?>
<html>
<head>
    <title>接口测试报告</title>
    <meta name="generator" content="HTMLTestRunner 0.8.2.2"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>

    <!-- 引入 echarts.js -->
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts-all-3.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>

    <style type="text/css" media="screen">
        body {
            margin: 0;
            font-family: "Arial", "Microsoft YaHei", "黑体", "宋体", sans-serif;
            font-size: 18px;
            line-height: 1.5;
            line-height: 1.5;
            color: #333333;
        }

        .table {
            margin-bottom: 1px;
            width: 100%;
        }

        .hiddenRow {
            display: none;
        }

        .container-fluid {
            padding-right: 120px;
            padding-left: 120px;
        }

        .nav-tabs li {
            width: 186px;
            text-align: center;
        }
    </style>
</head>

<body >
    <script language="javascript" type="text/javascript">

    function showClassDetail(detail_id, hiddenRow_id, class_type) {
        console.log(document.getElementById(hiddenRow_id).className)

        if ('详细' ==  document.getElementById(detail_id).innerText) {
            if ('all' == class_type) {
                document.getElementById(hiddenRow_id).className = 'all';
            }
            else if ('success' == class_type) {
                document.getElementById(hiddenRow_id).className = 'success';
            }
            else if ('error' == class_type) {
                document.getElementById(hiddenRow_id).className = 'error';
            }
            else if ('fail' == class_type) {
                document.getElementById(hiddenRow_id).className = 'fail';
            }else if ('timeout_calss' == class_type) {
                document.getElementById(hiddenRow_id).className = 'timeout_calss';
            }else if ('fe_class' == class_type) {
                document.getElementById(hiddenRow_id).className = 'fe_class';
            }else{
                document.getElementById(hiddenRow_id).className = 'untreaded';
            }
            document.getElementById(detail_id).innerText = "收起"
        }
        else {
            document.getElementById(detail_id).innerText = "详细"
            document.getElementById(hiddenRow_id).className = 'hiddenRow';
        }
    }

    </script>

    <div class="container-fluid">
        <div class="page-header">
            <h1 class="text-primary" style="font-size:45px;line-height:75px">接口自动化测试报告({{env_sign}})</h1>
        </div>

        <div class="col-md-12">
            <div class="col-md-4" style="Background-Color:#F5F5F5; height:300px">
                <h3 style="line-height:25px">测试基本信息</h3>
                <table class="table table-hover table-bordered" style="width:100% height:11px">
                    <tbody>
                        <tr class="info">
                            <td class="text-center">开始时间</td>
                            <td class="text-center">{{start_time}}</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">结束时间</td>
                            <td class="text-center">{{end_time}}</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">测试用时</td>
                            <td class="text-center">{{used_time}}</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">最大响应时间</td>
                            <td class="text-center">{{maximum_time}}秒</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">平均响应时间</td>
                            <td class="text-center">{{average_time}}秒</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">最小响应时间</td>
                            <td class="text-center">{{minimum_time}}秒</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="col-md-8">
                <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
                <div id="main" style="height:300px;"></div>
                <script type="text/javascript">
                    var myChart = echarts.init(document.getElementById('main'));
                    var option = {
                      backgroundColor: '#F5F5F5', //背景色
                      title: {
                        text: '测试统计数据',
                        x: 'center'
                      },
                      legend: {
                        orient: 'vertical',
                        x: 'left',
                        data: ['全部','成功','失败/错误', '超时','跳过']
                      },
                      color: ['#FE9A2E','#FF4000','#3c763d', '#0099CC','#3c763d'],
                      calculable: true,
                      series: [{
                        name: '测试结果',
                        type: 'pie',
                        radius: '55%',
                        center: ['50%', '60%'],
                        startAngle: 135,
                        data: [{
                          value: {{fail_error_sum}},
                          name: '失败/错误',
                          itemStyle: {
                            normal: {
                              label: {
                                formatter: '{b} : {c} ({d}%)',
                                textStyle: {
                                  align: 'left',
                                  fontSize: 15,
                                }
                              },
                              labelLine: {
                                length: 40,
                              }
                            }
                          }
                        }, {
                          value: {{timeout_sum}},
                          name: '超时',
                          itemStyle: {
                            normal: {
                              label: {
                                formatter: '{b} : {c} ({d}%)',
                                textStyle: {
                                  align: 'right',
                                  fontSize: 15,
                                }
                              },
                              labelLine: {
                                length: 40,
                              }
                            }
                          }
                        }, {
                          value: {{right_sum}},
                          name: '成功',
                          itemStyle: {
                            normal: {
                              label: {
                                formatter: '{b} : {c} ({d}%)',
                                textStyle: {
                                  align: 'left',
                                  fontSize: 15,
                                }
                              },
                              labelLine: {
                                length: 40,
                              }
                            }
                          }
                        }, {
                          value: {{untreaded_sum}},
                          name: '跳过',
                          itemStyle: {
                            normal: {
                              label: {
                                formatter: '{b} : {c} ({d}%)',
                                textStyle: {
                                  align: 'left',
                                  fontSize: 15,
                                }
                              },
                              labelLine: {
                                length: 40,
                              }
                            }
                          }
                        }],
                      }]
                    };
                    // 为echarts对象加载数据
                    myChart.setOption(option);
                </script>
            </div>
        </div>    
"""

REPORT_TMPL_Lable = '''
    <div><span>&nbsp;</span></div>

    <div class="col-md-12">
        <div class="tabbable" id="tabs-957640">
            <ul class="nav nav-tabs">
                <li class="active">
                    <a href="#panel-0" data-toggle="tab" style="Background-Color: #428bca; color: #fff;">全  部 ({})</a>
                </li>
                <li>
                    <a href="#panel-1" data-toggle="tab" style="Background-Color: #3c763d; color: #fff;">成  功 ({})</a>
                </li>
                
                <li>
                    <a href="#panel-2" data-toggle="tab" style="Background-Color: #FE9A2E; color: #fff;">失  败/错  误 ({})</a>
                </li>
                <li>
                    <a href="#panel-3" data-toggle="tab" style="Background-Color: #FF4000; color: #fff;">响应超时 ({})</a>
                </li>
                 <li>
                    <a href="#panel-4" data-toggle="tab" style="Background-Color: #0099CC; color: #fff;">跳  过 ({})</a>
                </li>
            </ul>
        </div>
        <div class="tab-content">
            <div class="tab-pane active" id="panel-0">
                <table class="table table-hover table-bordered">
{}
                </table>
            </div>

            <div class="tab-pane" id="panel-1">
                <table class="table table-hover table-bordered">
{}
                </table>
            </div>
            <div class="tab-pane" id="panel-2">
                <table class="table table-hover table-bordered">
{}
                </table>
            </div>
            <div class="tab-pane" id="panel-3">
                <table class="table table-hover table-bordered">
{}
                </table>
            </div>
            <div class="tab-pane" id="panel-4">
                <table class="table table-hover table-bordered">
{}
                </table>
            </div>

        </div>
    </div>


</div>
</body>
</html>
'''

REPORT_TMPL_Title = '''
            <table class="table table-hover table-bordered" style="Background-Color:#dff0d8">
                <thead>
                    <colgroup>
{}
                    </colgroup>
                    <tr>
{}
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
 '''

REPORT_Title_Width = '''                         <col width='{}%'/>
'''

REPORT_Title_Lable = '''                         <td class="text-center"  style="Background-Color:#dff0d8">{}</td>
'''

REPORT_Table_Data = '''                           <td class="text-center">{}</td>
'''

REPORT_Table_Detail = '''                           <td class="text-center"><a href="javascript:showClassDetail('{}','{}', '{}')" class="detail" id = "{}">详细</a></td>
'''

EXPORT_Detali_text = '''                   <tr class='hiddenRow' id="{}" >
                       <td colspan='{}'>
                           <div>
                               <pre class="text-left">
{}
                               </pre>
                           </div>
                       </td>
                   </tr> 
'''


class HTML_REPORT:
    def __init__(self, html_title, env_sign, pie_theme, test_info, report_table_title, report_cases):
        '''
        @parameter html_title:HTML标题，字符串类型，如html_title = u'接口测试报告'
        @parameter pie_theme:，饼图名称，字符串类型，pie_theme = u'接口数据统计'
        @parameter test_info:，饼图数据统计，列表类型，长度 = 6，如test_info = ['2016-12-02 15:59:17', '2016-12-02 16:10:22', '11 分 4 秒', len(report_cases['all_cases']), len(report_cases['right_cases']) + len(report_cases['error_cases']), len(report_cases['untreaded_cases'])]
        @parameter report_table_title:接口表格标题,列表类型，可以自定义，report_cases = ['项目名称', '用例编号', '用例名称', '接口地址', '接口方法', '测试结果', '详细信息']
        @parameter report_cases:接口测试结果记录，字典格式且key不能变，report_cases = {'all_cases':[['WEB理财', '1', '登录', 'login', 'post', 'pass', '详细信息', ''],['WEB理财', '2', '产品列表', 'list', 'post', 'error', '详细信息', '']],
                                                                            'right_cases':[['WEB理财', '1', '登录', 'login', 'post', 'pass', '详细信息', '']],
                                                                            'error_cases':[['WEB理财', '2', '产品列表', 'list', 'post', 'error', '详细信息', '']],
                                                                            'untreaded_cases':[['WEB理财', '3', '测试', 'login', 'post', '/', '详细信息', '']]
                                                                            }
        '''
        if isinstance(html_title, str) and len(html_title) > 0:
            self.html_title = html_title
        else:
            self.html_title = u'接口测试报告'
        if isinstance(env_sign, str) and len(env_sign) > 0:
            self.env_sign = env_sign
        else:
            self.html_title = u'接口测试报告'
        if isinstance(pie_theme, str) and len(pie_theme) > 0:
            self.pie_theme = pie_theme
        else:
            self.theme = u'接口数据统计'
        if isinstance(report_table_title, list) and len(report_table_title) > 0:
            self.report_table_title = report_table_title
        else:
            print('nothing of report_table_title.')
            sys.exit(0)

        if isinstance(test_info, list) and 9 == len(test_info):
            self.test_info = test_info
        else:
            print('nothing of test_info.')
            sys.exit(0)
        if isinstance(report_cases, dict) and len(report_cases) > 0:
            self.report_cases = report_cases
            self.pie_sum_number = {'right_sum': len(report_cases['right_cases']),
                                   # 'fail_sum': len(report_cases['fail_cases']),
                                   # 'error_sum': len(report_cases['error_cases']),
                                   'untreaded_sum': len(report_cases['untreaded_cases']),
                                   'fail_error_sum': len(report_cases['fail_error_cases']),
                                   'timeout_sum': len(report_cases['timeout_cases']),
                                   'all_sum': len (report_cases['all_cases'])
                                   }

        else:
            print('nothing of report_cases or length is not 6.')
            sys.exit(0)

    def packagedCases(self, export_lable_title, data_key, class_name, pannel_num):
        cases_num = 1
        cases_packaged = ''
        cases_packaged = ''.join([cases_packaged,
                                  '                   <tr class="{}">\n'.format(class_name),
                                  export_lable_title,
                                  '                   </tr>\n'])
        for data_case in self.report_cases[data_key]:
            detail_id = ''.join([pannel_num, '-detail-', str(cases_num)])
            hidden_id = ''.join([pannel_num, '-hidden-', str(cases_num)])
            cases_num += 1
            cases_packaged = ''.join([cases_packaged, '                   <tr class="{}">\n'.format(class_name)])
            for data in data_case[:-1]:
                if '详细' == data:
                    cases_packaged = ''.join(
                        [cases_packaged, REPORT_Table_Detail.format(detail_id, hidden_id, 'success', detail_id)])
                else:
                    cases_packaged = ''.join([cases_packaged, REPORT_Table_Data.format(data)])
            cases_packaged = ''.join([cases_packaged, '                   </tr>\n'])
            cases_packaged = ''.join(

                [cases_packaged, EXPORT_Detali_text.format(hidden_id, len(data_case) - 1, data_case[-1])])
        return cases_packaged

    def genHtmlReport(self, html_template):
        export_lable_title = ''
        for lable_tile in self.report_table_title:
            export_lable_title = ''.join([export_lable_title, REPORT_Title_Lable.format(lable_tile)])

        str_right_datas = ''
        str_untreaded_cases = ''
        # str_fail_cases = ''
        # str_error_cases = ''
        str_all_cases = ''

        # bij
        str_fail_error_cases = ''
        str_timeout_cases = ''
        for data_key in self.report_cases.keys():
            if 'right_cases' == data_key:
                str_right_datas = self.packagedCases(export_lable_title, data_key, 'success', 'panel1')
            elif 'untreaded_cases' == data_key:
                str_untreaded_cases = self.packagedCases(export_lable_title, data_key, 'untreaded', 'panel4')
            # elif 'error_cases' == data_key:
            #     str_error_cases = self.packagedCases(export_lable_title, data_key, 'error', 'panel3')
            # elif 'fail_cases' == data_key:
            #    str_fail_cases = self.packagedCases(export_lable_title, data_key, 'fail', 'panel2')
            elif 'fail_error_cases' == data_key:
                str_fail_error_cases = self.packagedCases(export_lable_title, data_key, 'fe_class', 'panel2')
            elif 'timeout_cases' == data_key:
                str_timeout_cases = self.packagedCases(export_lable_title, data_key, 'timeout_calss', 'panel3')
            else:
                str_all_cases = self.packagedCases(export_lable_title, data_key, 'all', 'panel0')

        export_lable_datas = REPORT_TMPL_Lable.format(
            len(self.report_cases['all_cases']),
            len(self.report_cases['right_cases']),
            len(self.report_cases['fail_error_cases']),
            len(self.report_cases['timeout_cases']),
            len(self.report_cases['untreaded_cases']),
            # len(self.report_cases['fail_cases']),
            # len(self.report_cases['error_cases']),
            str(str_all_cases[0:-1]),
            str(str_right_datas[0:-1]),
            str(str_fail_error_cases[0:-1]),
            str(str_timeout_cases[0:-1]),
            str(str_untreaded_cases[0:-1])
            # str(str_fail_cases[0:-1]),
            # str(str_error_cases[0:-1]),
        )

        html_template = ''.join([html_template, export_lable_datas])

        html = template(html_template,
                        report_title=self.html_title,
                        theme=self.pie_theme,
                        env_sign=self.env_sign,
                        start_time=self.test_info[0],
                        end_time=self.test_info[1],
                        used_time=self.test_info[2],
                        sum_all_cases=self.test_info[3],
                        sum_executed_cases=self.test_info[4],
                        sum_untreaded_cases=self.test_info[5],
                        maximum_time=self.test_info[6],
                        average_time=self.test_info[7],
                        minimum_time=self.test_info[8],
                        all_sum=self.pie_sum_number['all_sum'],
                        right_sum=self.pie_sum_number['right_sum'],
                        # fail_sum=self.pie_sum_number['fail_sum'],
                        # error_sum=self.pie_sum_number['error_sum'],
                        # timeout_sum=self.pie_sum_number['right_sum'],
                        untreaded_sum=self.pie_sum_number['untreaded_sum'],

                        # bij
                        fail_error_sum=self.pie_sum_number['fail_error_sum'],
                        timeout_sum=self.pie_sum_number['timeout_sum'])

        return html


if __name__ == '__main__':
    report_title = u'接口测试报告'
    theme = u'接口数据统计'

    report_table_title = ['项目名称', '用例编号', '用例名称', '接口地址', '接口方法', '响应时间','测试结果', '详细信息']

    case_detail = '''
sim_card_service.get_flow_by_serial Test failure!
Because of : Data check failure,AssertionError!
Data Should : sim_card_service.get_flow_by_serial
Data Actually : sim_card_service.get_flow_by_serial , 6.4413928985596


Response Json tree:
{
    "msg": {
        "message": "failed",
        "code": -1,
        "data": "该号码不存在"
    },
    "code": -1,
    "trace": "sim_card_service.get_flow_by_serial , 6.4413928985596"
}
'''
    report_cases = {'all_cases': [
        ['理财', '1', '登录', 'l44gin', 'post', 'Pass', '详细',case_detail],
        ['WEB理财', '2', '产品列表', 'list', 'post', 'Fail', '详细', case_detail],
        ['理财', '3', '测试', 'login', 'pot', '/', '详细', case_detail]],
        'right_cases': [['理财3', '1', '登录', 'login', 'st', 'Pass', '详细', case_detail]],
        'fail_cases': [['理财2', '2', '产品列表', 'list', '55t', 'Fail', '详细', case_detail]],
        'error_cases': [['理财4', '2', '产品列表', 'list', '55t', 'Fail', '详细', case_detail], ['理财5', '2', '产品列表', 'list', '55t', 'Fail', '详细', case_detail]],
        'untreaded_cases': [
            ['WEB理财', '3', '测试', 'login', 't', '/', '详细', case_detail]]
    }

    test_info = ['2016-12-02 15:59:17', '2016-12-02 16:10:22', '11 分 4 秒', len(report_cases['all_cases']),
                 len(report_cases['right_cases']) + len(report_cases['error_cases']),
                 len(report_cases['untreaded_cases'])]

    alldata = {
        'report_title': '接口测试报告',
        'theme': '接口数据统计',
        'env_sign': 'SCRM线上环境',
        'report_table_title': ['项目名称', '用例编号', '用例名称', '接口地址', '接口方法', '响应时间', '测试结果', '详细信息'],
        'report_cases': {
            'all_cases': [['理财3', '1', '登录', 'login', 'st',0.01, 'Pass', '详细', case_detail],
                          ['理财4', '2', '产品列表', 'list', '55t', 0.01,'Error', '详细', case_detail],
                          ['理财2', '2', '产品列表', 'list', '55t', 0.01,'Fail', '详细', case_detail],
                          ['WEB理财', '3', '测试', 'login', 't',0.01, '/', '详细', case_detail],
                          ['SCRM', 'test_documents_contacts', '类型为联系人、来源为发出去', '/api/scrm/documents', 'post',
                           '0.512734','pass',
                           '详细',
                           '{    "expected": 0,    "actual": 0,    "parameter": {        "type": 0,        "source": 0    },    "time_count": "0.512734",    "Results": {        "code": 0,        "data": {            "data": [],            "count": 2,            "all": 0,            "contacts": [],            "file_ext": []        },        "debug": {            "run_time": 0.12318611145019531,            "sql_count": 4,            "rpc_count": 2,            "memory_use": "14.24M",            "include_files": 375,            "request_id": "102020181125204911138",            "optimization_list": [                "execute time:0.020222902297974s;OperationCenter->UpgradePromptLib->upgradeMsg():http://bj-et-gouuse-api.online.local/operation_center/v3/rpc",                "execute time:0.082733869552612s;UserCenter->AccountLib->check():http://bj-et-gouuse-api.online.local/user_center/v3/rpc",                "OOPS, FOUND FULLTABLE SCAN!execute time:2ms;select COLUMN_NAME,COLUMN_KEY from                 INFORMATION_SCHEMA.COLUMNS where table_name =contacts and  table_schema =scrm",                "OOPS, FOUND FULLTABLE SCAN!execute time:2ms;select COLUMN_NAME,COLUMN_KEY from                 INFORMATION_SCHEMA.COLUMNS where table_name =contacts and  table_schema =scrm",                "OOPS, FOUND FULLTABLE SCAN!execute time:1ms;select COLUMN_NAME,COLUMN_KEY from                 INFORMATION_SCHEMA.COLUMNS where table_name =files_relate and  table_schema =scrm",                "OOPS, FOUND FULLTABLE SCAN!execute time:1ms;select COLUMN_NAME,COLUMN_KEY from                 INFORMATION_SCHEMA.COLUMNS where table_name =files_relate and  table_schema =scrm"            ]        }    }}'],

                          ],
            'right_cases': [['理财3', '1', '登录', 'login', 'st', 0.01,'Pass', '详细', case_detail]],
            # 'fail_cases': [['理财2', '2', '产品列表', 'list', '55t',0.01, 'Fail', '详细', case_detail]],
            # 'error_cases': [['理财4', '2', '产品列表', 'list', '55t', 0.01,'Error', '详细', case_detail]],
            'untreaded_cases': [['WEB理财', '3', '测试', 'login', 't', 0.01,'/', '详细', case_detail]],
            'fail_error_cases': [
                ['SCRM', 'test_actionsListT', '新增联系人、行为记录', '/api/scrm/actionsList', 'post', '0.479861', 'fail', '详细',
                 '{    "expected": 0,    "actual": 1020020013,    "parameter": {        "contacts_id": " ",        "start_time": "2018-08-23",        "system_type": "scrm",        "end_time": "2018-09-21"    },    "time_count": "0.479861",    "Results": {        "code": 1020020013,        "debug": {            "run_time": 0.0680701732635498,            "sql_count": 0,            "rpc_count": 2,            "memory_use": "14.36M",            "include_files": 367,            "request_id": "102020181125205018659",            "optimization_list": [                "execute time:0.021180152893066s;OperationCenter->UpgradePromptLib->upgradeMsg():http://bj-et-gouuse-api.online.local/operation_center/v3/rpc",                "execute time:0.044340133666992s;UserCenter->AccountLib->check():http://bj-et-gouuse-api.online.local/user_center/v3/rpc"            ]        },        "msg": "参数错误"    }}']
            ],
            'timeout_cases': [
                ['SCRM', 'test_documents_contacts', '类型为联系人、来源为发出去', '/api/scrm/documents', 'post', '0.512734','pass',
                 '详细',
                 '{    "expected": 0,    "actual": 0,    "parameter": {        "type": 0,        "source": 0    },    "time_count": "0.512734",    "Results": {        "code": 0,        "data": {            "data": [],            "count": 2,            "all": 0,            "contacts": [],            "file_ext": []        },        "debug": {            "run_time": 0.12318611145019531,            "sql_count": 4,            "rpc_count": 2,            "memory_use": "14.24M",            "include_files": 375,            "request_id": "102020181125204911138",            "optimization_list": [                "execute time:0.020222902297974s;OperationCenter->UpgradePromptLib->upgradeMsg():http://bj-et-gouuse-api.online.local/operation_center/v3/rpc",                "execute time:0.082733869552612s;UserCenter->AccountLib->check():http://bj-et-gouuse-api.online.local/user_center/v3/rpc",                "OOPS, FOUND FULLTABLE SCAN!execute time:2ms;select COLUMN_NAME,COLUMN_KEY from                 INFORMATION_SCHEMA.COLUMNS where table_name =contacts and  table_schema =scrm",                "OOPS, FOUND FULLTABLE SCAN!execute time:2ms;select COLUMN_NAME,COLUMN_KEY from                 INFORMATION_SCHEMA.COLUMNS where table_name =contacts and  table_schema =scrm",                "OOPS, FOUND FULLTABLE SCAN!execute time:1ms;select COLUMN_NAME,COLUMN_KEY from                 INFORMATION_SCHEMA.COLUMNS where table_name =files_relate and  table_schema =scrm",                "OOPS, FOUND FULLTABLE SCAN!execute time:1ms;select COLUMN_NAME,COLUMN_KEY from                 INFORMATION_SCHEMA.COLUMNS where table_name =files_relate and  table_schema =scrm"            ]        }    }}'],

            ]
        },
        'test_info': ['2018-11-25 21:36:11', '2018-11-25 21:36:18', '6秒', 5, 5, 0, 0.485253, 0.3589254, 0.2]
    }

    html_report_object = HTML_REPORT(alldata["report_title"], alldata["env_sign"], alldata["theme"],
                                     alldata["test_info"], alldata["report_table_title"], alldata["report_cases"])

    # html_report_object = HTML_REPORT(report_title, theme, test_info, report_table_title, report_cases)

    html = html_report_object.genHtmlReport(html_template)

    with open("test_demo.html", 'wb') as f:
        f.write (html.encode ('utf-8'))

    # 使用浏览器打开html
    webbrowser.open("test_demo.html")


