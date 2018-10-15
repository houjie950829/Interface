# coding=utf-8
import paramiko
from bbs.test_case.models.configpath import read_xml_attribute_normal


class ConnectSSH:
    """远程连接linux服务器"""
    def __init__(self):
        self.host = read_xml_attribute_normal('ssh',0,'host',xml_path='config.xml')
        self.username = read_xml_attribute_normal('ssh',0,'username',xml_path='config.xml')
        self.password = read_xml_attribute_normal('ssh',0,'password',xml_path='config.xml')

    def connectSSH(self):
        """返回一个连接对象"""
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.host,username=self.username,password=self.password,allow_agent=True)
            return ssh
        except Exception as msgs:
            print(msgs)
            return None

    def exec_commands(self, cmd="echo 'flush_all' | nc 192.168.5.219 11211"):
        """执行命令"""
        conn = self.connectSSH()
        stdin, stdout, stderr = conn.exec_command(cmd)
        results = stdout.read()
        results = results.decode('utf-8') # 将二进制解码为str
        print(results)
        return results


if __name__ == '__main__':
    ConnectSSH().exec_commands()
