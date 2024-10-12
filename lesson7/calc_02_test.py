from pages.calculator import Calculator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_calculator():
    
    driver =webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    calculator = Calculator(driver)
    calculator.clear_waits()
    calculator.put_new_waits(45)
    calculator.click_7()
    calculator.click_plus()
    calculator.click_8()
    calculator.click_equals()
    calculator.wait_time(driver, "15")
    calculator.watch_answer()
    answer = calculator.watch_answer()
    assert answer == "15"
