'''
三个厨师同时造蛋挞放进篮子里 篮子只能存500
六个客户每个人有3000元同时买蛋挞每一个两元
篮子里500个买完之后需要停3秒然后在买直到把3000元用完



'''
from threading import Thread
import time
bread=0
class make(Thread):
    chef = ""  # 厨师
    amount = 0  # 制造蛋挞数量
    def run(self) -> None:
        global bread
        while True:
            if bread<500:
                bread=bread+1
                self.amount=self.amount+1
                print(self.chef,"制造出",self.amount,"个蛋挞")
            elif bread==500:
                print(time.sleep(3))

class tart(Thread):
    client=""#购买者
    count=0 #购买数量
    def run (self) -> None:
        money = 3000
        global bread
        while True:
            if money>0:
                money=money-2
                bread=bread-1
                self.count=self.count+1
                print(self.client, "总共抢了", self.count, "蛋挞")
            elif money<0:
                print("余额不足")
                break



c1=make()
c2=make()
c3=make()

c1.chef="主厨1"
c2.chef="主厨2"
c3.chef="主厨3"

c1.start()
c2.start()
c3.start()


p1 = tart()
p2 = tart()
p3 = tart()
p4 = tart()
p5 = tart()
p6 = tart()

p1.client="张三"
p2.client="李四"
p3.client="王五"
p4.client="麻子"
p5.client="狗剩"
p6.client="拐子"

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()


