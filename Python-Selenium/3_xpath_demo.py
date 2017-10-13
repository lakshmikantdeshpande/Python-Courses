from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "asdfads@sadfas.com"

driver = webdriver.Chrome("/usr/local/chromedriver-Linux64")
driver.get("http://demo.guru99.com/")
assert "99" in driver.title

elem = driver.find_element(By.XPATH, "//input[@name='emailid']")
elem.send_keys(user)
elem = driver.find_element(By.XPATH, "//input[@name='btnLogin']")
elem.click()

# close the browser
driver.close()
