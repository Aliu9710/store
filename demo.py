

# 程序结构
#     顺序结构
#     选择结构：if...else
#     循环结构：
#         while : 条件循环
#         for


# import random
# num=random.randint(0,100)
# print(num)
'''
猜数字：
    需求：系统随机产生一个数字，让用户从键盘输入你需要的数字，
        1.如果猜中，则恭喜
        2.如果猜的数字比系统的数字大，温馨提示：大了
        3.如果猜小了，稳性提示小了
        一直到用户猜中为止
    技术选型：
        1.random
        2.input
        3.if....else
        4.while
    金币功能：
    1.玩家初始化5000金币， 猜错扣500，金币不够，系统锁定
    2.猜中， 奖励10000
'''
#1.实现步骤
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






