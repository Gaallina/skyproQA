from selenium.webdriver.common.by import By
import allure


class formPage():
    allure.step("Открытие страницы: 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'")

    def __init__(self, driver: str):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    allure.step("Ввод в поле 'first name'")

    def first_name(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'last name'")

    def last_name(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'address'")

    def address(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'zip code'")

    def zip_code(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'city'")

    def city(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'country'")

    def country(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'email'")

    def e_mail(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'phone number'")

    def phone(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'job position'")

    def job_position(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]'
                                  ).send_keys(term)

    allure.step("Ввод в поле 'company'")

    def company(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]'
                                  ).send_keys(term)

    allure.step("Нажатие кнопки 'submit'")

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    allure.step("Проверка подсвеченности поля 'Zip code' красным цветом")

    def alert_danger(self) -> str:
        alert_danger = self._driver.find_element(
            By.CSS_SELECTOR, 'div.alert.py-2.alert-danger'
            ).value_of_css_property("background-color")
        return alert_danger

    allure.step("Проверка подсвеченности полей зелёным цветом")

    def alert_success(self) -> list:
        allert_success = self._driver.find_elements(
            By.CSS_SELECTOR, 'div.alert.py-2.alert-success')
        for form in allert_success:
            return form.value_of_css_property("background-color")
