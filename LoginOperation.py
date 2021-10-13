# -*- codeing = utf-8 -*-
# @time : 2021/10/12 15:57
# @Author : 张刘生
# @File : LoginOperation.py
# @Software: PyCharm

from selenium import  webdriver

class  LoginOpera:
    # driver 申明一个全局变量
    def __init__(self,driver):
        self.driver = driver  # 变成全局的driver浏览器对象

    # 就是登陆的实际操作
    def login(self,username,password):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    # 获取成功的实际结果
    def getSuccessResult(self):
        return self.driver.title

    # 获取登陆失败的实际结果
    def getErrorResult(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text
'''
class LoginOpera:
    #driver申明全局变量
    def __init__(self,driver):
        self.driver = driver # 变成全局的driver浏览器对象

    #登录实际操作
    def login(self,username,password):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()


    #获取成功的实际结果
    def getSuccessResult(self):
        return self.driver.title

    # 获取失败的实际结果
    def getErrorResult(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text

'''








