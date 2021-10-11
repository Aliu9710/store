import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("小梁")
driver.find_element_by_xpath("//*[@id='password']").send_keys("7416478")
driver.find_element_by_xpath("//*[@id='submit']").click()
