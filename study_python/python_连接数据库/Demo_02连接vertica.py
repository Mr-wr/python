import vertica_python
import logging
#配置文件
dev_conn_info = {
             'host': '********',
             'port': 5433,
             'user': '*******',
             'password': '*********',
             'database': '**********',
             'log_level': logging.DEBUG,
             # 默认情况下会自动生成会话标签，
             'session_label': 'some_label',
             # 无效的UTF-8结果默认抛出错误
             'unicode_error': 'strict',
             # 默认情况下禁用SSL
             'ssl': False,
             # 默认情况下，禁用使用服务器端预处理语句
             'use_prepared_statements': False,
             # 默认情况下未启用连接超时
             # 套接字操作5秒超时（建立TCP连接或读/写操作）
             'connection_timeout': 5}

def conn_Vertcia(conn_info):
    # 使用后使用后自动关闭连接
    # 简单连接，手动关闭
    # COPY tablname FROM local dat文件(绝对路径) EXCEPTIONS '../**.log' DELIMITER '|' abort on error no commit ;
    # 使用copy的方式来插入
    copy = "copy {parame.schema}.test_{parame.table}({columnstr}) FROM STDIN DELIMITER ',' ENCLOSED BY '\"';"
    # copysql = f"copy {parame.schema}.test_{parame.table}({columnstr}) FROM STDIN DELIMITER ',' ENCLOSED BY '\"';"
    with vertica_python.connect(**conn_info) as connection:
        # 获取
        c = connection.cursor()
        with open('path', "rb") as fs:
            c.copy(copy,fs, buffer_size=65536)


