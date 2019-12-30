import pymssql #引入pymssql模块


def conn():
    connect = pymssql.connect('(local)', 'sa', '*******', 'test') #服务器名,账户,密码,数据库名
    if connect:
        rowlist = []
        print("连接成功!")
        sql = "select * from tset_create"
        cursor = connect.cursor()
        cursor.execute(sql)
        # 查询数据不需要提交不然会报错
        # cursor.commit()
        rows = cursor.fetchone()
        while rows:
            # print(rows)
            rowlist.append(rows)
            #没有写这一个就是无限循环应该是不断的获取下一条数据
            rows = cursor.fetchone()
        cursor.close()
        connect.close()
    return rowlist


if __name__ == '__main__':
    rows = conn()
    for row in rows:
        print(row)
    
