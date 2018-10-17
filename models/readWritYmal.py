# coding=utf-8
import yaml
from . configpath import readconfig, readapp, readpublic


class MyYaml:
    def __init__(self, interface='switch', name='config.yaml', dirName='marketing', encoding='utf-8'):
        self.name = name
        self.encoding = encoding
        self.interface = interface
        self.dirName = dirName

    @property
    def allYaml(self):
        """读取yaml里所有的内容"""
        path = readconfig(self.name)
        f = open(path, encoding=self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def allAppYaml(self):
        """读取yaml里所有的内容"""
        path = readapp('SOUTHSEA', self.name)
        f = open(path, encoding=self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def allPublicYaml(self):
        """读取yaml里所有的内容"""
        path = readpublic(self.dirName, self.name)
        f = open(path, encoding=self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def baseUrl(self):
        """读取请求地址"""
        return str(self.allYaml['base_url'][self.interface])

    @property
    def email(self):
        """email"""
        return self.allYaml['email'][self.interface]

    @property
    def baseData(self):
        """基础数据"""
        return self.allYaml['data']

    @property
    def baseSql(self):
        """sql"""
        return str(self.allYaml['sql'][self.interface])

    @property
    def configYaml(self):
        """读取config"""
        return self.allYaml['config'][self.interface]

    @property
    def interface_data(self):
        """获取接口数据"""
        return self.allAppYaml['interface']

    @property
    def return_keys(self):
        """按顺序返回yaml列表里所有的key，list"""
        return list(self.interface_data.keys())

    @property
    def readpublic(self):
        """读取public数据"""
        return self.allPublicYaml[self.interface]


if __name__ == '__main__':
    data = MyYaml(name='public.yaml',interface='interface').readpublic
    print(data)
