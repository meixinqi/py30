"""
1、连接数据库，创建游标
2、执行sql语句
3、获取执行结果
4、关闭游标，关闭数据库
"""
import pymysql
from common.handle_ini import conf#从ini文件中读取数据库配置信息

class Handle_db:
    def __init__(self):
        """
        1、对数据库进行初始化操作，连接数据库，创建游标
        2、将数据库信息进行文件配置化，这样仅需修改配置文件即可，即数据分离
        """
        self.conn=pymysql.connect(
            host=conf.get("mysql","host"),
            port=int(conf.get("mysql","port")),
            user=conf.get("mysql","user"),
            password=conf.get("mysql","password"),
            database=conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor#保证返回数据是字典对象
        )
        self.curs=self.conn.cursor()
    def select_one_data(self,sql):
        self.conn.commit()
        self.curs.execute(sql)
        return self.curs.fetchone()
    def select_all_data(self,sql):
        self.conn.commit()
        self.curs.execute(sql)
        return self.curs.fetchall()
    def count_data(self,sql):
        self.conn.commit()
        return self.curs.execute(sql)
    def update(self,sql):
        """
        :param sql: 对数据进行增删改的操作
        :return:
        """
        self.curs.execute(sql)
        self.conn.commit()#往数据库进行提交
    def db_close(self):
        self.curs.close()
        self.conn.close()
db=Handle_db()
if __name__ == '__main__':
    db=Handle_db()
    sql= 'select * from member where mobile_phone="18600001120"'
    print(db.select_all_data(sql))
    db.db_close()
    #print(dict(Handle_db.__dict__.items()))