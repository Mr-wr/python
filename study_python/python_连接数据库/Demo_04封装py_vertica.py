import vertica_python, re, json, time, pandas as pd, numpy as np
import datetime
from time import time
class Vertica:
    def __init__(self,**conn_info):
        """传入配置信息"""
        self._conn_info = conn_info

    def __get_connect(self):
        """获取连接"""
        self.connection = vertica_python.connect(**self._conn_info)
        cur = self.connection.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def __sqltodf(self,sql_code = ''):
        """处理查询语句"""
        sql_code = re.sub('--.*?\n', '\n', sql_code) 
        # 删除SQL代码里的注释行
        sql_list = ''.join(sql_code.replace('\n','').split()).split(';')
        return sql_list
        #     cur.execute(sql_list[s_i]+";")
        #     e = time.time()
        #     print(sql_list[s_i])
        #     print("execute time: "+str(round((e-s)/60, 2))+" min")
        # del sql_list, s_i
        # print('SQL Done...')
        # return pd.Dataframe(cur.fetchall())

    def __exec_query(self,sql):
        """执行查询语句"""
        cur = self.__get_connect()
        cur.execute(sql)
        resList = cur.fetchall()
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def exec_query_dict(self, sql):
        """把查询的数据变成dict返回"""
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
    
    def exce_copy(self,copysql,path):
        """使用copy的语法"""
        cur = self.__get_connect()
        with open(path, "rb") as fs:
            cur.copy(copysql,fs, buffer_size=65536)

