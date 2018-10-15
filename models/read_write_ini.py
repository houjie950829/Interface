# coding=utf-8

import configparser
from . configpath import readapp


def write_ini(dir='SOUTHSEA', node='session', child='token0', content=None):
    """写入ini文件"""
    path = readapp(dir, 'config.ini')  # 获取配置文件路径
    config=configparser.ConfigParser()
    config.read(path, encoding='utf-8')

    try:
        # config.add_section("session") #增加节点
        config.set(node, child, content)
    except configparser.DuplicateSectionError:
        print("ini配置文件写入失败")

    f = open(path, "w", encoding='utf-8')
    config.write(f)
    f.close()


def read_ini(dir='SOUTHSEA', node='session', child='token0'):
    """读取ini文件"""
    path = readapp(dir, 'config.ini')  # 获取配置文件路径
    config=configparser.ConfigParser()
    config.read(path, encoding='utf-8')

    try:
        content = config.get(node, child)
        # print(content)
        return content
    except configparser.DuplicateSectionError:
        print("ini配置文件读取失败！")

if __name__ == '__main__':
    # read_ini()
    write_ini(node='data', child='name_mobile', content="{'name': '小强', 'mobile': 13718411080}")