#高度Height, 容积volume, 颜色color, 材质material 水杯Water glass 液体liquid
class water:
    __Height=0
    __volume=0
    __color=""
    __material=""
    __liquid=""
    def setHeight(self,Height):
        if Height<0 or Height>25:
            print("此水杯高度不是水杯高度")
        else:
            self.__Height=Height
    def getHeight(self):
        return self.__Height

    def setvolume(self,volume):
        if volume<0 or volume>2000:
            print("此容量不是水杯范围")
        else:
            self.__volume = volume
    def getvolume(self):
        return self.__volume

    def setcolor(self,color):
        self.__color=color
    def getcolor(self,color):
        return self.__color


    def setmaterial(self,material):
        self.__material=material
    def getmaterial(self,material):
        return self.__material

    def setliquid(self,liquid):
        self.__liquid=liquid
    def getliquid(self,liquid):
        return self.__liquid


    def run(self):
        print(self.__material,"水杯,他有",self.__Height,"cm高","容积",self.__volume,"ml","里面装的是",self.__liquid)

c=water()
c.setHeight(5)
c.setvolume(500)
c.setcolor("红色")
c.setmaterial("玻璃")
c.setliquid("西果汁")
c.run()

