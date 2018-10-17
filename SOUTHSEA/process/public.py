import requests
from models import MyYaml
from models.read_write_ini import read_ini
from datetime import datetime


def get_public(data_get,l):
    data = []
    public_data = MyYaml(name='public.yaml',interface=str(data_get),dirName='process').readpublic
    for i in public_data:
        for _ in i['url']:
            data.append(_)
        data.append(i['bar'])
    return data[l]


def token():
    return {'Authorization': read_ini()}


def add_process():
    url = MyYaml('SOUTHSEA').baseUrl + get_public('addprocess',0)
    y = get_public('addprocess',1)
    y['type_name'] = '测试类型的名称{}'.format(str(datetime.now().strftime('%Y%m%d%H%M%S')))
    r = requests.post(url, headers = token(),data = y)
    if r.json().get('code') is 0:
        return True
    else:
        return r.json()

def get_list_process():
    url = MyYaml('SOUTHSEA').baseUrl + get_public('listprocess', 0)
    type_id = []
    r = requests.post(url, headers = token(), data = get_public('listprocess', 1))
    if r.json().get('code') is 0:
        y = r.json().get('data')
        if y:
            for i in range(len(y)):
                type_id.append(y[i].get('type_id'))
            return type_id
        else:
            t = add_process()
            if t is True:
                return get_list_process()
            else:
                print('\033[31m','固定流程类别添加失败...失败原因{}'.format(add_process()))
    else:
        return False,r.json()

def get_member_id():
    url = MyYaml('SOUTHSEA').baseUrl + get_public('getmemberid', 0)
    id = []
    r = requests.post(url, headers=token(), data=get_public('getmemberid', 1))
    if r.json().get('code') is 0:
        y = r.json().get('data')
        if y:
            for i in range(len(y)):
                id.append(y[i].get('member_id'))
            print(id)

if __name__ == '__main__':
    get_member_id()