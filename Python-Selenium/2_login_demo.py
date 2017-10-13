from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = "asdfads@sadfas.com"
pwd = "scah"

driver = webdriver.Chrome()
driver.get("http://demo.guru99.com/")
assert "99" in driver.title

elem = driver.find_element_by_name("emailid")
elem.send_keys(user)
elem = driver.find_element_by_name("btnLogin")
elem.click()

# close the browser
driver.close()
