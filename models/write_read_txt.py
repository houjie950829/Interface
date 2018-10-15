# coding=utf-8
from bbs.test_case.models.configpath import readtoken


def write_txt(filename, data):
    u"""写入txt文件"""
    try:
        file_path = readtoken(filename)  # 获取路径
        file_object = open(file_path, 'w')
        file_object.write(str(data))
        file_object.close()
    except Exception as msg:
        print('写入txt文件失败！')
        print(msg)


def read_txt(filename):
    u"""读取txt文件"""
    try:
        file_path = readtoken(filename)  # 获取路径
        f = open(file_path)
        try:
            lines = f.readlines()  # 读取全部内容
            barc = '.'.join(lines)  # 将列表转换为字符串
            return str(barc)
        finally:
            f.close()
    except Exception as msg:
        print(msg)


if __name__ == '__main__':
    write_txt('token.txt', '123456')
    read_txt('token.txt')
