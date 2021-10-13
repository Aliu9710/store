# -*- codeing = utf-8 -*-
# @time : 2021/10/13 10:08
# @Author : 张刘生
# @File : main.py
# @Software: PyCharm
from HTMLTestRunner import HTMLTestRunner
import unittest
import os
tests =unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(

    title="HKR登录测试",
    description="HKR登录详细测试【成功，失败】",
    verbosity=1,
    stream=open("HKR测试报告.html",mode="w+",encoding="utf-8")
)
runner.run(tests)



