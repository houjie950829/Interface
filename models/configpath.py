# coding=utf-8
import os


def readconfig(file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件的上上级路径
    base_dir = str(base_dir)
    file_path = base_dir + '/config/{}'.format(file_name)  # 配置config文件路径
    return file_path


def readapp(dir_name, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件的上上级路径
    base_dir = str(base_dir)
    file_path = base_dir + '/{}/{}'.format(dir_name, file_name)  # 配置config文件路径
    return file_path


def readlog(file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件的上上级路径
    base_dir = str(base_dir)
    file_path = base_dir + '/log/{}'.format(file_name)  # 配置config文件路径
    return file_path


def readpublic(dir_name, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件的上上级路径
    base_dir = str(base_dir)
    file_path = base_dir + '/SOUTHSEA/{}/{}'.format(dir_name, file_name)  # 配置config文件路径
    return file_path
