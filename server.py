# coding=utf-8

import os
import socket
from models.readWritYmal import MyYaml

class RunServer:
    def __init__(self):
        self.ip = MyYaml('ip').configYaml
        self.port = MyYaml('port').configYaml
        hostname = socket.gethostname()
        self.my_ip = socket.gethostbyname(hostname)
        self.python = MyYaml('python').configYaml

    def check_status(self):
        """ip检查"""
        if self.ip is None:
            os.system('{} ./mysite/manage.py runserver {}:{}'.format(self.python, self.my_ip, self.port))
        elif self.ip == '127.0.0.1':
            os.system('{} ./mysite/manage.py runserver 127.0.0.1:{}'.format(self.python, self.port))
        elif self.ip != self.my_ip:
            print('请检查填写ip和当前ip是否一致！')
        else:
            os.system('{} ./mysite/manage.py runserver {}:{}'.format(self.python, self.my_ip, self.port))


if __name__ == '__main__':
    RunServer().check_status()