# coding=utf-8
from models import read_ini
from models import MyYaml
import requests
from random import randint,choice
import random,os,re
from datetime import date

def  regular(template,content):
    p1 = r"\" \":\"(.+?)\","  # 模板
    pattern1 = re.compile(p1)
    b = pattern1.findall(content)

def Addmeetingroom():
    print(os.path.dirname(__file__))
    # 添加会议室

    meeting_room_title = "会议室名称" + str(randint(0, 9999))
    address=str(randint(0, 9999)) + "街" + str(randint(0, 9999)) + "号"
    accommodate_number=str(randint(0, 100))

    headers = {'Authorization': read_ini()}
    alldata=MyYaml(name='public.yaml',interface='Addmeetingroom',dirName='meeting').readpublic
    print(alldata)

    url =MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    print(type(alldata[1]['data']['form_data']))

    r = requests.post(url, headers=headers, data=alldata[1]['data'], stream=True)
    result = r.json()
    print(result)

q=Addmeetingroom()
