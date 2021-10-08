from selenium import webdriver
import  time

# 创建谷歌浏览器对象
ders=webdriver.Chrome()

# 打开百度网址
ders.get("http://www.baidu.com")
# 窗口最大化
ders.maximize_window()
#寻找搜索输入框
ders.find_element_by_id("kw").send_keys("京东商城")
# 点击百度一下按钮
ders.find_element_by_id("su").click()
time.sleep(3)
ders.get("http://www.jd.com")
time.sleep(3)
ders.find_element_by_xpath("//*[@id ='key' and @type='text' and @class='text']").send_keys("电脑")
#点击搜素
time.sleep(2)
ders.find_element_by_xpath("//*[@class='button']").click()
time.sleep(2)
#ders.find_element_by_xpath("//*[@src='//img12.360buyimg.com/n7/jfs/t1/72714/34/17164/77978/61357df0Efda73af8/85ed82272847713e.jpg']").click()
#ders.find_element_by_xpath("//*[@class='gl-warp clearfix' @data-tp1='1']").send_keys()
#ders.find_element_by_xpath("//*[@data-sku='10015691164' and @date-spu='100015691164' @ware-type='10' @class='gl-item']").click()
ders.find_element_by_xpath("//*[@src='//img14.360buyimg.com/n2/jfs/t1/188134/26/12631/345405/60ed66a2E07ca9c2e/1425dee17628e748.jpg']").click()

# 退出浏览器
#ders.quit()






