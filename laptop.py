#Screen size屏幕大小, price价格, CPU model CPU型号, memory size内存大小, battery life待机时长
class top:
    __size = 0
    __price=''
    __cpu=0
    __memory=''
    __life=''
    def setsize(self,size):
        if size<0 or size>15.6:
            print("此物品不是笔记本电脑")
        else:
            self.__size=size
    def getsize(self,size):
        return self.__size


    def setprice(self,price):
        self.__price=price
    def getprice(self,price):
        return self.__price


    def setcpu(self,cpu):
        self.__cpu=cpu
    def getcpu(self,cpu):
        return self.__cpu

    def setmemory(self,memory):
        if memory<0:
            print("内存太小请安装内存")
        else:
            self.__memory=memory
    def getmemory(self,menory):
        return self.__memory


    def setlife(self,life):
        if life<0:
            print("此电脑有问题")
        else:
            self.__life=life
    def getlife(self,life):
        return self.__life
    def run(self):
        print("此电脑cpu型号为",self.__cpu,"屏幕大小为：",self.__size,"内存大小为：",self.__memory,"待机时长为：",self.__life,"购买价格为：",self.__price)


b=top()
b.setcpu(79)
b.setsize(15.6)
b.setmemory(24800)
b.setlife(48)
b.setprice("7800￥")
b.run()





