from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=ChromeService(
   ChromeDriverManager().install()))
driver.maximize_window()
try:
    for a in range(3):
        driver.get("http://uitestingplayground.com/classattr")
        b_b = driver.find_element(
            'xpath', "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        b_b.click()
        sleep(5)
        driver.switch_to.alert.accept()
except Exception as ex:
    print(ex)

sleep(2)

driver.quit()
