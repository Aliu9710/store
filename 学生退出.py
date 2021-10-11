import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("小梁")
driver.find_element_by_xpath("//*[@id='password']").send_keys("7416478")
driver.find_element_by_xpath("//*[@id='submit']").click()
driver.find_element_by_xpath("//*[@id='img']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='ul_pic']/li[4]/img").click()  # 选择已有头像
time.sleep(2)
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()  # 关闭更换头像小窗口

time.sleep(3)
driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
time.sleep(3)
driver.quit()