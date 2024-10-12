from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


def test_saucedeme():
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    user_log = driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')
    user_log.send_keys("standard_user")
    pass_log = driver.find_element(By.CSS_SELECTOR, '#password')
    pass_log.send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(
        By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    f_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    f_name.send_keys("Alex")
    l_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    l_name.send_keys("Trofimov")
    l_name = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    l_name.send_keys("153000")
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    assert total == "Total: $58.29"

    driver.quit()
    