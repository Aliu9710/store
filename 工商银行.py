import random
bank={
    "12345678":{"userName":"张三",
            "password":"123456",
          "country":"中国",
          "provic":"河南",
          "street":"周口",
          "number":"s001",
          "money":20000,

          },
    "123456":{"userName":"张三1",
                "password":"12345678",
              "country":"中国1",
              "provic":"河南1",
              "street":"周口1",
              "number":"s001",
              "money":30000,

              }

}#数据库以字典形式代替


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

#银行开户逻辑-------------------------
def bank_addUser(account,userName,password,country,provic,street,number,money):
      #判断数据库是否已满
    global bank
    if len(bank)>=100:
        return 3
    #判断是否有重复数据
    if userName in bank:
        return 2
    #正常开户
    bank[account]={
          "userName": userName,
          "password": password,
          "country": country,
          "provic": provic,
          "street": street,
          "number": number,
          "money": money,
          "bank_name": bank_Name
      }
    return 1





#用户开户逻辑---------------------------
def addUser():
    global bank
    userName=input("请输入您的姓名")
    password=input("请输入您的密码")
    country=input("请输入您的国籍")
    provic=input("请输入您的省份")
    street=input("请输入您的街道")
    number=input("请输入您的门牌号")
    money = int(input("请输入您的初始存款余额"))
    # 随机生成8位数账号
    account=random.randint(10000000, 99999999)
    stant=bank_addUser(account, userName, password, country, provic, street, number, money)
    if stant==3:
        print("数据库已满，请到其他银行")
    elif stant==2:
        print("该用户已存在")
    elif stant==1:
        print("开户成功")
        info = '''
        -------个人信息-------
        用户名 %s
        密码%s
        账号%s
        地址
            国籍 %s
            省份 %s
            街道 %s
            门牌号 %s
        余额 %s
        开户行地址 %s
        --------------------
        '''
        print(info %(userName, password,account, country, provic, street, number, money,bank_Name))



#存款逻辑------------------------------
def adddeposit():
    account: str=input("请输入账号")
    money = int(input("请输入您的存款金额"))
    if account in bank:
        bank[account]["money"] = bank[account]["money"] + money
        print(bank[account]["money"])
    else:
        print("你输入账号不存在")

#取款逻辑
def addwithdrawal():
    account:str=input("请输入账号")
    password:str=input("请输入密码")
    if password == bank[account]["password"]:
        money = int(input("请输入您的取款金额"))
        if account in bank:
            if bank[account]["money"]- money<0:
                print("账户余额不足")
            elif bank[account]["money"]- money>=0:
                bank[account]["money"] = bank[account]["money"] - money
                print("您的余额还剩：")
                print(bank[account]["money"])

        else:
            print("你输入账号不存在")
    else:
        print("你输入的密码不正确")


#转账逻辑------------------------------
#转出账号
def addtransfer():
    global bank
    account: str=input("请输入账号")
    password: str =input("请输入密码")
    if password == bank[account]["password"]:
        if account in bank:
            str= input("请输入转款账号：")
            if account in bank:
                money = int(input("请输入转账金额："))
                if bank[account]["money"]-money<0:
                    print("账户余额不足")
                elif  bank[account]["money"]-money>=0:
                    bank[account]["money"]=bank[account]["money"]-money
                    bank[str]["money"]=bank[str]["money"]+money
                    print("转账成功，你的余额还剩：")
                    print(bank[account]["money"])
                    print(bank)

            else:
                print("您输入的对方账号不存在")
        else:
            print("输入账号不存在")

    else:
        print("输入密码错误")

#查询
def addquer():
     global bank
     account=int(input("请输入查询账号"))
     if account in bank:
         password: str = input("请输入查询密码")
         if password==bank[account]["password"]:
             print("你的密码是：")
             print(bank[account]["password"])
             print("你的用户名是：")
             print(bank[account]["userName"])
             print("你的国家是：")
             print(bank[account]["country"])
             print("你的省份是：")
             print(bank[account]["provic"])
             print("你的街道是：")
             print(bank[account]["street"])
             print("你的门牌号是：")
             print(bank[account]["number"])
             print("你的开户行名称为：")
             print(bank_Name)



         else:
            print("您输入的密码不正确")
     else:
         print("你查询的账号不存在")

#退出
def bye():
    print("bye")




#欢迎页面
while True:
    welcome()
    chose=input("请输入您的业务")
    if chose=="1":
        addUser()
    elif chose=="2":
        adddeposit()
    elif chose=="3":
        addwithdrawal()
    elif chose=="4":
        addtransfer()
    elif chose=="5":
        addquer()
    elif chose == "6":
        bye()
        break
    else:
        print("您输入错误，请重新输入")



