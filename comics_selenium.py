from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://18h.mm-cg.com/18H_5717.html')
large_cgurl = driver.execute_script("return Large_cgurl")
print(large_cgurl)
