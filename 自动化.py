# -*- codeing = utf-8 -*-
# @time : 2021/10/12 14:30
# @Author : 张刘生
# @File : 自动化.py
# @Software: PyCharm

'''
框架
    1. 数据类：专门用于封装登录的所有，参数化的数据在这地方
    2. 操作类：专门用于对模块的操作
    3. 用列类： 整合数据类和操作类的完成登录操作
    4. 入口程序： 专门生成测试报告

'''



from unittest import TestCase
from selenium import webdriver

class Demo(TestCase):
    def testLogin1(self):
        # 1.准备数据
        username = "jason"
        password = "1234567"
        expect = "Student Login1"  # 期望结果

        # 2.启动浏览器，输入数据
        driver = webdriver.Chrome()
        driver.get(r"http://localhost:8080/HKR")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        driver.find_element_by_xpath("//*[@id='submit']").click()

        # 3.断言
        #  获取浏览器的标题
        data = driver.title

        if expect !=  data:
            driver.save_screenshot("登陆失败！.jpg")
        else:
            print("登陆成功，用例通过！")

'''
# 1 准备数据
class Demo(TestCase):
    def testLogin1(self):
        username = "jason"
        password = "1234567"
        expect = "Student Login1" #期望结果
# 2 启动浏览器输入数据
        driver=webdriver.Chrome()
    #启动系统的地址
        driver.get(r"http://localhost:8080/HKR")
    #窗口最大化
        driver.maximize_window()
    #定位账户的ID
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
    #定位密码
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
    #定位登录ID 点击登录
        driver.find_element_by_xpath("//*[@id='submit']").click()


    #3 断言
    #获取浏览器的标题

        date=driver.title

        if expect != date:
            driver.save_screenshot("登录失败.jpg")
        else:
            print("登陆成功")

'''


