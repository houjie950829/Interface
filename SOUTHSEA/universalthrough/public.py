import requests
from models import MyYaml
from models.read_write_ini import read_ini


def get_public(data_get):
    data = []
    public_data = MyYaml(name='public.yaml',interface=str(data_get),dirName='universalthrough').readpublic
    for i in public_data:
        for _ in i['url']:
            data.append(_)
        data.append(i['bar'])
    return data


def token():
    return {'Authorization': read_ini()}


def add_universal_through():
    url = MyYaml('SOUTHSEA').baseUrl + get_public('adduniversalthrough')[0]
    r = requests.post(url, headers=token(), data=get_public('adduniversalthrough')[1])
    if r.json().get('code') is 0:
        return True
    else:
        return r.json()


def get_universal_through_list():
    url = MyYaml('SOUTHSEA').baseUrl + get_public('listuniversalthrough')[0]
    r = requests.post(url, headers=token(), data=get_public('listuniversalthrough')[1])
    list_id = []
    if r.json().get('code') is 0:
        y = r.json().get('data')
        if y:
            for i in range(len(y)):
                list_id.append(y[i].get('announce_id'))
            return list_id
        else:
            t = add_universal_through()
            if t is True:
                return get_universal_through_list()
            else:
                print('\033[31m','百事通未能添加成功..原因{}'.format(t))
    else:
        return False,r.json()

def self_list_id():
    url = MyYaml('SOUTHSEA').baseUrl + get_public('selfuniversalthrough')[0]
    r = requests.post(url, headers=token(), data=get_public('selfuniversalthrough')[1])
    list_id = []
    if r.json().get('code') is 0:
        y = r.json().get('data')
        if y:
            for i in range(len(y)):
                list_id.append(y[i].get('announce_id'))
            return list_id
        else:
            t = add_universal_through()
            if t is True:
                return get_universal_through_list()
            else:
                print('\033[31m', '百事通未能添加成功..原因{}'.format(t))
    else:
        return False, r.json()

def del_universal_through(announce_id):
    url = MyYaml('SOUTHSEA').baseUrl + get_public('deluniversalthrough')[0]
    r = requests.post(url, headers=token(), data={"announce_id":announce_id})
    if r.json().get('code') is 0:
        return True
    else:
        return r.json()

if __name__ == '__main__':
    # print(get_universal_through_list())
    # print(self_list_id())
    print(del_universal_through(2605))