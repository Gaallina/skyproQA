from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

ff = webdriver.Firefox()

try:
    ff.get("http://the-internet.herokuapp.com/inputs")
    input_field = ff.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    sleep(2)
    input_field.clear()
    sleep(2)
    input_field.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)

ff.quit()
