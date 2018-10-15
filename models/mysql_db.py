# coding=utf-8

import pymysql.cursors
from bbs.test_case.models.configpath import read_xml_attribute_normal

try:
    ip = read_xml_attribute_normal('mysql',0,'ip',xml_path='config.xml')
    user = read_xml_attribute_normal('mysql',0,'user',xml_path='config.xml')
    pwd = read_xml_attribute_normal('mysql',0,'pwd',xml_path='config.xml')
    port = read_xml_attribute_normal('mysql', 0, 'port',xml_path='config.xml')
    library_xml = read_xml_attribute_normal('mysql',0,'library',xml_path='config.xml')
except Exception as msg:
    print(msg)
    print('数据库配置信息读取失败！')


# ======== MySql base operating ===================
class mysql_db:

    def __init__(self, library: object = library_xml) -> object:

        try:
            # Connect to the database
            self.connection = pymysql.connect(host=ip,
                                              port=int(port),
                                              user=user,
                                              password=pwd,
                                              db=library,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # perform sql

    def perform_sql(self, real_sql, status=0):
        # print(real_sql)
        result_all = []
        try:
            curs = self.connection.cursor()
            if status == 1:
                curs.execute(real_sql)
                for rec in curs.fetchall():
                    return rec
            elif status == 2:
                curs.execute(real_sql)
                for rec in curs.fetchall():
                    result_all.append(rec)
                return result_all
            else:
                curs.execute("SET FOREIGN_KEY_CHECKS=0;")
                curs.execute(real_sql)
            self.connection.commit()
        except Exception as msgs:
            print(msgs)
            print('执行sql语句失败！')

    def db_close(self):
        self.connection.close() # 断开连接


if __name__ == '__main__':

    db = mysql_db()
    sql_result = db.perform_sql("SELECT customer_name FROM operation_customer WHERE customer_id = 551117", status=1)
    print(sql_result)
