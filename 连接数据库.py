# 连接数据库
from pymysql import Connection

conn = Connection(
    host="wyhhxx.cn",
    port=3306,
    user="root",
    password="123456",
    autocommit=True    # 自动提交
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("student")
# 通过游标对象，执行命令
cursor.execute("create table test_001  (id int, name varchar(20), );")

cursor.execute("insert into class6 values(6,'刘佳峰',99,119,83,49,42,55,447,58,61,3); ")
# 通过commit 确认
conn.commit()  # 或者设置自动提交

cursor.execute("select * from class6;")
cursor.execute("SELECT * from class6 where  math > 90 ORDER BY english  DESC  limit 20;")

# print(conn.get_server_info())

results = cursor.fetchall()
# print(results)
for r in results:
    print(r)



# 关闭数据库
conn.close()





