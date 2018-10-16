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
def Addmeetingroom():

    # 添加会议室
    meeting_time_day = str(int(time.time()))
    meeting_time_h_i = str(int(time.time() + 50000))
    datatime = "".join([meeting_time_day, ",", meeting_time_h_i])
    meeting_room_title = "会议室名称" + str(randint(0, 9999))
    headers = {'Authorization': read_ini()}
    alldata=MyYaml(name='public.yaml',interface='Addmeetingroom',dirName='meeting').readpublic
    value=alldata[1]['data']['form_data']%(meeting_room_title,datatime)
    url =MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    r = requests.post(url, headers=headers, data={"form_data":value}, stream=True)
    result = r.json()
    return result['meeting_room_id']


def Addmeeting():

        # 新增会议

    meeting_title = "会议主题" + str(randint(0,9999))
    start_data = date.today() + timedelta(days=+2)
    time_now = time.mktime(time.strptime(str(start_data), '%Y-%m-%d'))
    meeting_time_day = int(time.mktime(time.strptime(str(start_data), '%Y-%m-%d')))
    starttime= str(meeting_time_day+77400)
    meeting_time_h_i = str(int(starttime)+3600)
    datatime = "".join([starttime,",",meeting_time_h_i])
    alldata = MyYaml(name='public.yaml', interface='Addmeeting', dirName='meeting').readpublic
    url = MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    headers = {'Authorization': read_ini()}
    value = alldata[1]['data']['form_data']%(meeting_title,str(meeting_time_day),datatime,Addmeetingroom())
    r = requests.post(url, headers=headers, data={"form_data":value}, stream=True)
    result = r.json()
    return result['data']['meeting_id']

def Meetinglist():

        # 会议列表

    alldata = MyYaml(name='public.yaml', interface='Meetinglist', dirName='meeting').readpublic
    url = MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    headers = {'Authorization': read_ini()}
    r = requests.post(url, headers=headers, data= alldata[1]['data'], stream=True)
    result = r.json()
    meetingidlist = []
    for i in range(0,len(result['data']['list'])):
        meetingidlist.append(result['data']['list'][i]['meeting_id'])
    if len(meetingidlist) == 0:
        Addmeeting()
        alldata = MyYaml(name='public.yaml', interface='Meetinglist', dirName='meeting').readpublic
        url = MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
        headers = {'Authorization': read_ini()}
        r = requests.post(url, headers=headers, data=alldata[1]['data'], stream=True)
        result = r.json()
        for i in range(0, len(result['data']['list'])):
            meetingidlist.append(result['data']['list'][i]['meeting_id'])
    return meetingidlist
