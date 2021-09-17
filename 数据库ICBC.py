#from DBUtils import up_date
#from DBUtils import select_date
import random
import pymysql

host="localhost"
user="root"
password="root"
database="bc"
def up_date(sql,param):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def select_date(sql,param):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()
    return cursor.fetchall()






bank_Name="中国工商银行昌平支行"
#开户的入口程序------------------------
def welcome():
    print("****************************")
    print("*      中国工商银行           *")
    print("*      账户管理系统           *")
    print("*        V0.1版本           *")
    print("* 1,开户                    *")
    print("* 2,存款                    *")
    print("* 3,取款                    *")
    print("* 4,转账                    *")
    print("* 5,查询                    *")
    print("* 6,bye                    *")
    print("****************************")

#开户逻辑
def a_adduser(account,username,password,country,provic,street,number,money,bank_Name):
    # 1.判断数据库是否已满
    sql = "select * from bank"
    date = select_date(sql, [])
    if len(date) >= 100:
        return 3
    # 2.判断用户是否存在
    elif account in date:
        return 2
    # 3.正常开户
    else:
        sql1 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param1 = [account,username,password,country,provic,street,number,money,bank_Name]
        up_date(sql1, param1)
        return 1



#用户开户
def adduser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍:")
    provic = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    number = input("请输入您的门牌号：")
    brank = "中国工商银行"
    money = float(input("请输入您的开户余额："))  # 将输入的余额换成int类型
    # 随机产生8位数字
    account = random.randint(10000000, 99999999)
    status = a_adduser(account,username,password,country,provic,street,number,money,bank_Name)
    if status == 3:
        print("对不起，用户库已满，请携带证件到其他行办理")
    elif status ==2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status== 1:
        # bank[username].append({"账号":account,"密码":password,"余额":money,"国籍":country,"居住省份":province,"街道":street,"门牌号":gate})
        print("开户成功！以下是您的个人开户信息")
        info = '''
               -------个人信息-------
               账号%s
               用户名 %s
               密码%s
               地址
                   国籍 %s
                   省份 %s
                   街道 %s
                   门牌号 %s
               余额 %s
               开户行地址 %s
               --------------------
               '''
        print(info % (account,username,password,country,provic,street,number,money,bank_Name))


#存款逻辑
def adddeposit():
    # 判断账号是否在数据库里
    account=input("请输入账号")
    sql1="select account from bank where account=%s"
    param1=[account]
    date1= select_date(sql1,param1)
    if len(date1)>0:
        money = float(input("请输入存款金额"))
        sql2="UPDATE bank SET money = money + %s where account = %s"
        param2=(money,account)
        up_date(sql2,param2)
        print("存款成功")
        aa = "select money from bank where account = %s"
        bb = select_date(aa, account)
        print("账号余额为：", bb[0][0])
        return True
    else:
        print("账号不存在！")
        return False
#取款
def addwithdrawal():
    #判断账号是否在数据库
    account=input("请输入取款账号")
    sql1="select * from bank where account=%s"
    param1=[account]
    date1=select_date(sql1,param1)
    if len(date1)>0:
        password = input("请输入密码")
        password = int(password)
        if password==date1[0][2]:
            money = float(input("请输入取款金额"))
            if money<date1[0][7]:
                sql4 = "update bank set money=money -%s  where account=%s"
                param4 = [money,account]
                up_date(sql4,param4)
                print("取款成功")
                aa="select money from bank where account =%s"
                bb=select_date(aa,account)
                print("您的余额为：",bb[0][0])
            else:
                print("你的余额不足！请存入再来")
                return 3
        else:
            print("输入密码不正确")
            return 2
    else:
        print("输入的账号不存在")
        return 1
#银行转账
def addtransfer():
    #判断账号是不是在数据库
    account1=input("请输入转出账号")
    account2=input("请输入转入账号")
    sql1="select * form bank where account=%s"
    param1=[account1]
    date1=select_date(sql1,param1)
    sql2="select * form bank where account=%s"
    param2=[account2]
    date2=select_date(sql2,param2)
    if len(date1)>0 and len(date2)>0:
        password=input("请输入转出账号密码")
        if password==date1[0][2]:
            money=float(input("请输入转账金额："))
            if money<date2[2][7]:
                sql3="update bank set money=money -%s  where account=%s"
                param3=[money,account1]
                up_date(sql3,param3)
                sql4="update bank set money=money +%s  where account=%s"
                param4 = [money, account2]
                up_date(sql4, param4)
                print("转账成功")
                aa="select money from bank where account= %s"
                bb=select_date(aa,account1)
                print("您转出账户的余额为：",bb[0][0])
            else:
                print("您转出的金额大于余额")
                return 3
        else:
            print("你输入的密码不正确")
            return 2
    else:
        print("你输入的账号不存在")
        return 1

    #查询
def addquery():
    # 判断账号是不是在数据库
    account1 = input("请输入查询账号")
    sql1="select * from bank where account=%s"
    param1=[account1]
    tabe1=select_date(sql1,param1)
    if len(tabe1)>0:
        password=input("请输入密码")
        password = int(password)
        if password==tabe1[0][2]:
            info = '''
                           -------个人信息-------
                           账号%s
                           用户名 %s
                           地址
                               国籍 %s
                               省份 %s
                               街道 %s
                               门牌号 %s
                           余额 %s
                           开户行地址 %s
                           --------------------
                           '''
            print(info % (tabe1[0][0],tabe1[0][1],tabe1[0][3],tabe1[0][4],tabe1[0][5],tabe1[0][6],tabe1[0][7], "中国工商银行昌平支行"))
        else:
            print("你输入密码错误")
            return 2
    else:
        print("你输入的账号不存在")
        return 1

def addbaby():
    print("欢迎下次再来")




while True:
    welcome()
    chose = input("请输入你的业务")
    if chose=="1":
        adduser()
    elif chose=="2":
        adddeposit()
    elif chose=="3":
        addwithdrawal()
    elif chose=="4":
        addtransfer()
    elif chose=="5":
        addquery()
    elif chose=="6":
        addbaby()
    else:
        print("请重新输入")