
# n = 10
# nums = []
# for i in range(n):
#     num = int(input("输入任意整数以"))
# nums.append(num)
# # 获取最大值和最小值
# imax = 0
# imin = 0
# for num in nums:
#     if imax < num:
#      imax = num
#
#     if imin > num:
#         imin = num
# # 采用 str.format() 打印结果
# print("输入生成的10个数字为{}，最大值为{}，最小值为{}".format(num,imax,imin))

# n = 10
# imax = 0
# imin = 0
# for i in range(n):
#     num = int(input("输入任意整数>>>"))
# if num > imax:
#     imax = num
# if num < imin:
#     imin = num
# print("10次输入获取的数字中，最大值为{}，最小值为{}".format(imax,imin))



# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
max = 0#赋值
sum = 0
avg = 0
for num in range(10):#限制输入次数
    str = int(input("请输入第{}个数：".format(num+1)))
    sum += float(str)
    avg = sum / 10
    if str > max:
        max=str
print("最大数是：{}".format(max))
print("十个数的和是：{}".format(sum))
print("十个数的平均数是：{}".format(avg))