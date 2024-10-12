from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for a in range(1, 6):
    click_button = driver.find_element(
        By.CSS_SELECTOR, ("[onclick='addElement()']")).click()

delete_button = driver.find_elements(
    By.XPATH, "//button[@onclick='deleteElement()']")
print(f'Размер списка кнопок Delete: {len(delete_button)}')

sleep(6)
