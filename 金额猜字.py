import random
money= 5000#金额数
num =random.randint(1,30)#随机数的取值范围
count = 0#次数初始为零
while True:#循环
    count=count+1#执行后次数自动跳到下一次
    if count>10:#限制次数
        print("余额不足 ")
        break#结束
    chose = input("请输入你要猜的数字：")
    chose = int(chose)
    if chose > num:#输入的数字大于随机的数字
        print("大了!")
        money = money - 500#金额减10
        print("当前金币为：", money)
    elif chose < num:
        print("小了！")
        money=money-10
        print("当前金币为：",money)

    else:
        money = money + 5000
        print("恭喜猜中了， 你本次数字为：",num,"你本次输入了",count,"次","你的金额为：",money)


        #跳出循环
        break
