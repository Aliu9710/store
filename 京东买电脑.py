from selenium import webdriver
import time

zhang = webdriver.Chrome()

zhang.get("https://www.jd.com/")
zhang.maximize_window()


#zhang.find_element_by_xpath("").send_keys()
