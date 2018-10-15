import sqlite3
from models.configpath import readconfig
from models.readWritYmal import MyYaml


class DB:
    def __init__(self, sql=None, db='gouuse.db'):
        self.db = db
        self.sql = sql

    def sql_db(self):
        try:
            db_path = readconfig(self.db)
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(self.sql)
            values = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            return values
        except Exception as msgs:
            print(msgs)


if __name__ == '__main__':
    DB(sql="INSERT INTO error_case_log ('case_id','log') VALUES ('test_login_phone_error',VHJhY2ViYWNrIChtb3N0IHJlY2VudCBjYWxsIGxhc3QpOgogIEZpbGUgIkQ6XE15V29ya3NwYWNlXEdvdXVzZVRlc3RVaVx0ZXN0X2Nhc2VccGFnZV9zdGFcbG9naW5cbG9naW5fc3RhLnB5IiwgbGluZSAzNywgaW4gdGVzdF9sb2dpbl9waG9uZV9lcnJvcgogICAgcHJpbnQoYSkKTmFtZUVycm9yOiBuYW1lICdhJyBpcyBub3QgZGVmaW5lZAo=);").sql_db()