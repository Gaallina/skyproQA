from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import formPage
import allure


@allure.title("Заполнение формы")
@allure.description("Проверка подсвеченности обязательных полей")
@allure.feature("READ")
@allure.severity("blocker")
@allure.suite("Тесты на работу формы с заполнением персональных данных")
def test_form():
    with allure.step("Открываем браузер"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Открытие страницы: 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'"):
        input_form = formPage(browser)

    with allure.step("Ввод в поле 'first name'"):
        input_form.first_name('Иван')

    with allure.step("Ввод в поле 'last name'"):
        input_form.last_name('Петров')

    with allure.step("Ввод в поле 'address'"):
        input_form.address('Ленина, 55-3')

    with allure.step("Ввод в поле 'email'"):
        input_form.e_mail('test@skypro.com')

    with allure.step("Ввод в поле 'phone'"):
        input_form.phone('+7985899998787')

    with allure.step("Ввод в поле 'Zip Code'"):
        input_form.zip_code('')

    with allure.step("Ввод в поле 'city'"):
        input_form.city('Москва')

    with allure.step("Ввод в поле 'country'"):
        input_form.country('Россия')

    with allure.step("Ввод в поле 'job position'"):
        input_form.job_position('QA')

    with allure.step("Ввод в поле 'company'"):
        input_form.company('SkyPro')

    with allure.step("Нажатие кнопки 'submit'"):
        input_form.submit()

    with allure.step("Проверка подсвеченности поля 'Zip code' красным цветом"):
        alert_danger = input_form.alert_danger()

        assert alert_danger == "rgba(248, 215, 218, 1)"

    with allure.step("Проверка подсвеченности полей зелёным цветом"):
        alert_succes = input_form.alert_success()

        assert alert_succes == "rgba(209, 231, 221, 1)"

    with allure.step("Закрытие браузера"):
        browser.quit()
