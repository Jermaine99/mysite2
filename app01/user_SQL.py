import pymysql



def login():
    while True:
        print("用户登录")
        userId = input("请输入账号： ")
        passWord = input("请输入密码： ")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="985738441", db="day0405")
        cursor = conn.cursor()
        cursor.execute("select * from user_info where userId = '{}' and passWord = '{}'".format(userId, passWord))
        result = cursor.fetchone()  # 去向MySql获取结果
        # fetchone, 如果指令指执行后获取了很多数据，只拿第一行
        #       没有：None
        #         有：获取第一行数据
        #  fetch
        if result:
            print("登陆成功")
            break
        else:
            print("账号或密码错误")


def register():
    while True:
        print("用户注册")
        userId = input("请输入账号： ")
        passWord = input("请输入密码： ")

        if userId != "" and passWord != "":
            conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="985738441", db="day0405")
            cursor = conn.cursor()
            sql = "insert into user_info(userId, passWord) value('{}','{}')".format(userId, passWord)
            cursor.execute(sql)
            conn.commit()

            cursor.close()
            conn.close()
            print("注册成功！")
            break
        print("请输入正确的形式")


if __name__ == '__main__':

    choice = input("注册输入1, 登录输入2： ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("输入错误")


