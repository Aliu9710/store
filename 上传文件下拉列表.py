from selenium import webdriver
import time
#创建谷歌浏览器对象
serd=webdriver.Chrome()
#打开浏览器地址
serd.get(r"D:\Rjcs\python自动化测试\综合项目\python\python\python自动化\day01\任务\练习的html\上传文件和下拉列表/autotest.html")
#窗口最大化
serd.maximize_window()

#寻找输入框
serd.find_element_by_xpath("//*[@id='accountID' and @type='text' and @name='account']" ).send_keys("梓轩")

time.sleep(2)
serd.find_element_by_xpath("//*[@id='passwordID' and @type='password' and @name='password']" ).send_keys("123456")

time.sleep(2)
serd.find_element_by_xpath("//*[@id='areaID' and @class = 'u17']" ).send_keys("北京市")

time.sleep(2)
serd.find_element_by_xpath("//*[@name='u2' and  @id='sexID1' and @type='radio' ]" ).click()
time.sleep(2)
serd.find_element_by_xpath("//*[@value =  'spring'  ]" ).click()

time.sleep(2)
serd.find_element_by_xpath("//*[ @value = 'Auterm']" ).click()

time.sleep(3)

serd.find_element_by_xpath("//*[ @type='file' and @name='file']" ).send_keys(r"D:\软件下载\微软下载软件\OneDrive\Pictures\本机照片\王秋紫  明星 高清4k电脑壁纸 4k手机壁纸_1920x1080_4kbizhi.com(1).jpg")

serd.quit()



