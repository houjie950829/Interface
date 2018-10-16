# coding=utf-8
from models import read_ini
from models import MyYaml
import requests
from random import randint,choice
import random,os,re
import json
import unittest
import requests
from models import mytest
from models import MyYaml
import time
from random import randint
from datetime import date,timedelta

def Addschedule():

    # 添加日程

    schedule_title = "日程标题" + str(randint(0, 9999))
    start_data = date.today() + timedelta(days=+2)
    meeting_time_day = int(time.mktime(time.strptime(str(start_data), '%Y-%m-%d')))
    starttime = str(meeting_time_day + 77400)
    meeting_time_h_i = str(int(starttime) + 3600)
    datatime = "".join([starttime, ",", meeting_time_h_i])
    headers = {'Authorization': read_ini()}
    alldata = MyYaml(name='public.yaml', interface='Addschedule', dirName='schedule').readpublic
    value = alldata[1]['data']['form_data']%(schedule_title,datatime)
    url = MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    r = requests.post(url, headers=headers, data={"form_data": value}, stream=True)
    result = r.json()
    return result['data']['follow_id']



# q= Addschedule()

