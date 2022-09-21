from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = webdriver.Chrome()
driver.get("http://192.168.0.1/")

#enter your password here
password = ''

inputElement = driver.find_element_by_id("pcPassword")
inputElement.send_keys(password)
inputElement.send_keys(Keys.ENTER)
sleep(1)

driver.switch_to.default_content()
driver.switch_to.frame('bottomLeftFrame')

driver.find_element_by_xpath('/html/body/menu/ol[49]/li/a/span').click()

# driver.find_element(By.XPATH, '/html/body/menu/ol[49]/li/a/span').click()

sleep(1)
driver.find_element_by_xpath('/html/body/menu/ol[56]/li/a').click()
sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame('mainFrame')
driver.find_element_by_id('reboot').click()

sleep(1)
ale = driver.switch_to.alert
sleep(1)
ale.accept()
sleep(4)
driver.close()