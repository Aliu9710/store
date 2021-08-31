'''
    1.用金钱
    2.空的购物车
    3.有足够商品
    4.正常购物
        是否有这个商品
        金钱是否足够
            添加购物车
    技术选型：
        1.判断
        2.循环
        3.容器技术
        4.输入input
        5.打印
    任务1：
        10张联想优惠券，0.5
        20张老干妈优惠券：0.6
        10张乌江榨菜优惠券，0.9
    最后使用优惠券来结算。
'''
# 1.准备一个商品柜
import random
shop = [
    ["联想电脑",4500],
    ["Mac Pc",12000],
    ["HUA WEI WATCH",1200],
    ["海尔洗衣机",5000],
    ["卫龙辣条",3.5],
    ["老干妈",15],
    ["乌江榨菜",1.5]
]
zhekou = [
    ['电脑联想'],
    ['老干妈'],
    ['榨菜']
]
chouqu=random.randint(0,2)
print("恭喜你抽取到了",chouqu,"的折扣优惠券")
money=input("请输入你的初始金额：")
money=int(money)
print('您的余额为',money,'元')
mycart = []
while True:
    # 展示商品
    for key,value in enumerate(shop):
        print(key,value)
    # 买东西
    chose = input("亲输入您要的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        #  这个商品是否存在
        if chose >= len(shop): # len(shop) = 7
            print("该商品不存在！别瞎弄！请重新输入：")
        else:
            # 看钱够不够
            if money < shop[chose][1]:
                print("对不起，您的余额不足，穷鬼，请到其他地方购买！")
            else:

                mycart.append(shop[chose])
                if chose==0 and chouqu==0:

                    money = money - shop[chose][1]*0.5
                    print("恭喜，添加购物车成功！您的余额还剩：",money,"!")
                elif chose==5 and chouqu==1:
                    money = money - shop[chose][1]*0.6
                    print("恭喜，添加购物车成功！您的余额还剩：",money,"!")
                elif chose==6 and chouqu==2:
                    money = money - shop[chose][1]*0.9
                    print("恭喜，添加购物车成功！您的余额还剩：",money,"!")
                else:
                    money = money - shop[chose][1]
                    print("恭喜，添加购物车成功！您的余额还剩：",money,"!")
                print('')
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("输入非法！别瞎弄！请重新输入：")

# 结算,打印购物小条
print("以下是您的购物小条，请查收：")
print("----------------------------")
for key,value in enumerate(mycart):
    print(key,value)
print("您本次余额还剩：￥",money)
print("----------------------------")