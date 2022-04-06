import pymysql

# 连接MySQL(socket)
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="985738441")

cursor = conn.cursor()

# 1.查看数据集
# 发送指令

cursor.execute("show databases")
# 获取指令结果 通过 fetchall()方法
result = cursor.fetchall()
print(result)

# 2.创建数据库(新增、删除、修改) 需要 commit()方法
# 发送指令
#cursor.execute("create database day25 DEFAULT CHARSET utf8 collate  utf8_general_ci")
#conn.commit()

# 3.查看数据库
# 发送指令

cursor.execute("show databases")
result = cursor.fetchall()
print(result)

# 5.进入数据库

cursor.execute("use day25")
cursor.execute("show tables")
result = cursor.fetchall()
print(result)

# 关闭连接
cursor.close()
conn.close()