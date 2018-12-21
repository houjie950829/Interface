#coding=utf-8
from locust import task,HttpLocust,TaskSet
import json
from random import choice

def returnCode(responContent):
    #返回code
    Json = json.loads(str (responContent)[2:-1])
    return Json['code']

def returnUser():
    # 返回用户名密码
    userData = []
    with open ("data/userData.csv", "r") as file:
        for line in file.readlines ():
            userData.append (line.strip ())
        return userData
class locustFile_task(TaskSet):
    @task()
    def on_start(self):
        userInfo = choice(returnUser())
        user = userInfo.split(',')
        print ("账号："+user[0]+"       "+"密码："+user[1])
        url = '/api/auth_center/v3/login'
        data = {
            "account":user[0],
            "password":user[1]
        }
        header = {'charset': 'UTF-8'}
        self.client.headers.update (header)
        with self.client.post(url,data = data,name="登录") as response:
            code = returnCode(response.content)
            assert code == '0'

    @task()
    def getCalendarlist(self):
        url = '/api/schedule/v3/m/calendar_list'

        with self.client.post(url,name="获取日程列表") as response:
            print (response.content)
            code = returnCode(response.content)
            assert code==1005104102


class locustFile_locust(HttpLocust):
    task_set = locustFile_task
    host = 'https://testwxweb.app.gouuse.cn'
    min_wait = 1000
    max_wait = 3000


