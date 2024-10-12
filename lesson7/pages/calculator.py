from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def clear_waits(self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    def put_new_waits(self, wait: int):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(wait)

    def click_7(self):
        self.driver.find_element(
            By.XPATH, '//span[text()="7"]').click()

    def click_plus(self):
        self.driver.find_element(
            By.XPATH, '//span[text()="+"]').click()

    def click_8(self):
        self.driver.find_element(
            By.XPATH, '//span[text()="8"]').click()

    def click_equals(self):
        self.driver.find_element(
            By.XPATH, '//span[text()="="]').click()

    def wait_time(celf, driver, answer : str):
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), answer))
        
    def watch_answer(self) -> str:
        answer = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return answer

    def quit(self):
        self.driver.quit()    
