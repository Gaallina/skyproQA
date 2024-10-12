from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
name = driver.find_element(By.ID, "username").send_keys("tomsmith")
password = driver.find_element(
    By.ID, "password").send_keys("SuperSecretPassword!")
button = driver.find_element(By.TAG_NAME, "button").click()
sleep(5)

driver.quit()
