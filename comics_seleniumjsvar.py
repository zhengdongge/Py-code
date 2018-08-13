from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://18h.mm-cg.com/18H_5717.html')
large_cgurl = driver.find_element_by_name('script language="javascript"')
print(large_cgurl)

