# coding=utf-8
from models import read_ini
from models import MyYaml
import requests
from random import randint,choice
import random,os,re
import json
from datetime import date

def Addmeetingroom():
    print(os.path.dirname(__file__))
    # 添加会议室

    meeting_room_title = "会议室名称" + str(randint(0, 9999))
    address=str(randint(0, 9999)) + "街" + str(randint(0, 9999)) + "号"
    accommodate_number=str(randint(0, 100))
    headers = {'Authorization': read_ini()}
    alldata=MyYaml(name='public.yaml',interface='Addmeetingroom',dirName='meeting').readpublic
    r=json.loads(alldata[1]['data']['form_data'])
    del json.loads(alldata[1]['data']['form_data'])['meeting_room_title']
    json.loads(alldata[1]['data']['form_data'])['meeting_room_title'] = meeting_room_title
    print(json.loads(alldata[1]['data']['form_data'])['meeting_room_title'])
    l=json.dumps(json.loads(alldata[1]['data']['form_data']))
    print(l)
    url =MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    print(alldata[1]['data'])
    r = requests.post(url, headers=headers, data=alldata[1]['data'], stream=True)
    result = r.json()
    print(result)


q=Addmeetingroom()
