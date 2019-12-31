#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyodbc
class MSSQL:
    """
    封装pyodbc
    """
    def __init__(self,host,user,pwd,db="master", charset="utf8"):
        self._host = host
        self._user = user
        self._pwd = pwd
        self._db = db
        self._charset = charset
    
    def __get_connect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self._db:
            raise(NameError,"没有设置数据库信息")
        conn_info = "DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s" % (self._db, self._host, self._user, self._pwd)
        self.conn = pyodbc.connect(conn_info, charset=self._charset)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur
    
    def __exec_query(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__get_connect()
        cur.execute(sql)
        resList = cur.fetchall()
    
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList
    
    def exec_query_tuple(self, sql):
        """结果集以元组返回"""
        return self.__exec_query(sql)
    
    def exec_query_dict(self, sql):
        result = []
        for row in self.__exec_query(sql):
            result.append( dict([(desc[0], row[index]) for index, desc in enumerate(row.cursor_description)]) )
        
        return result
    
    def exec_nonquery(self,sql):
        """
        执行非查询语句
        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__get_connect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
        
    
if __name__ == "__main__":
    conn = MSSQL("192.168.1.124", "sa", "Password", "Demo", "GBK")
    print(conn.exec_query_dict("select * from Staff where code=0001"))