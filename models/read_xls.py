# coding=utf-8
from pyexcel_xls import get_data
from bbs.test_case.models.configpath import readdata


def read_xls(xls_name='test_data.xlsx', sheet='login_data', start_r=2,
             row_l=15, statues=0):  # xls_name:文件名，sheet：表单名称，start_r从第几行读取，row_l截止到多少行
    u"""读取xls文件并返回测试数据"""
    try:
        if statues == 0:
            filename = readdata(xls_name)
        else:
            filename = xls_name
        data = get_data(filename, start_row=start_r, row_limit=row_l)
        json_list = data[sheet]
        for c in json_list:
            json_list[json_list.index(c)] = tuple(c)
        return json_list
    except Exception as msges:
        print(msges)


if __name__ == '__main__':
    a = read_xls(xls_name='send_to_email.xlsx', sheet='test')
    print(a)
