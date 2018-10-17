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
    alldata=MyYaml(name='public.yaml',interface='Addmeetingroom',dirName='meetingroom').readpublic
    value=alldata[1]['data']['form_data']%(meeting_room_title,datatime)
    url =MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    r = requests.post(url, headers=headers, data={"form_data":value}, stream=True)
    result = r.json()

def Meetingroomslist():

    # 会议室列表
    alldata=MyYaml(name='public.yaml',interface='Meetingroomslist',dirName='meetingroom').readpublic
    headers = {'Authorization': read_ini()}
    url =MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    r = requests.post(url, headers=headers, data= alldata[1]['data'], stream=True)
    result = r.json()
    roomidlist = []
    for i in range(0,len(result['data']['data'])):
        roomidlist.append(result['data']['data'][i]['meeting_room_id'])
    if len(roomidlist) == 0:
        Addmeetingroom()
        alldata = MyYaml(name='public.yaml', interface='Meetingroomslist', dirName='meetingroom').readpublic
        headers = {'Authorization': read_ini()}
        url = MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
        r = requests.post(url, headers=headers, data=alldata[1]['data'], stream=True)
        result = r.json()
        for i in range(0, len(result['data']['data'])):
            roomidlist.append(result['data']['data'][i]['meeting_room_id'])
    return roomidlist

def Arealist():

    # 区域列表
    alldata=MyYaml(name='public.yaml',interface='Arealist',dirName='meetingroom').readpublic
    headers = {'Authorization': read_ini()}
    url =MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    r = requests.post(url, headers=headers, data= alldata[1]['data'], stream=True)
    result = r.json()
    areaidlist = []
    for i in range(0,len(result['data']['list'])):
        areaidlist.append(result['data']['list'][i]['actual_area_id'])
    if len(areaidlist) == 0:
        Areaupdate()
        alldata = MyYaml(name='public.yaml', interface='Meetingroomslist', dirName='meetingroom').readpublic
        headers = {'Authorization': read_ini()}
        url = MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
        r = requests.post(url, headers=headers, data=alldata[1]['data'], stream=True)
        result = r.json()
        for i in range(0, len(result['data']['data'])):
            areaidlist.append(result['data']['data'][i]['meeting_room_id'])
    return areaidlist

def Areaupdate():

    # 区域添加
    actual_area_name = "区域名称" + str(randint(0, 9999))
    alldata=MyYaml(name='public.yaml',interface='Areaupdate',dirName='meetingroom').readpublic
    headers = {'Authorization': read_ini()}
    del alldata[1]['data']['actual_area_name']
    alldata[1]['data']['actual_area_name'] = actual_area_name
    url =MyYaml('SOUTHSEA').baseUrl + alldata[0]['url']
    r = requests.post(url, headers=headers, data= alldata[1]['data'], stream=True)
    result = r.json()

q=Arealist()