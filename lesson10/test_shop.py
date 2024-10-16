from selenium import webdriver
from shop_page import ShopPage
import allure
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.description("Тест сравнивает сумму добавленных в корзину товаров с конкретным значением")
@allure.feature("Онлайн магазин")
@allure.severity("blocker")
@allure.suite("Тесты на работу с интернет-магазином")
def test_online_shop():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    with allure.step("Переход на страницу интернет-магазина"):
        driver = webdriver.Chrome()
        shop_page = ShopPage(driver)

    with allure.step("Авторизация"):
        shop_page.authorisation("standard_user", "secret_sauce")
        shop_page.info_and_buttons()

    with allure.step("Добавление товаров в корзину"):
        shop_page.add_items_to_cart(
        "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie")

    with allure.step("Ввод данных покупателя"):
        shop_page.place_order("Galina", "Sergeevna", "675000")

    with allure.step("Получение итоговой стоимости товаров"):
        total = shop_page.get_result_price()

    with allure.step("Проверить, что ожидаемая и фактическая стоимость равны"):
        assert total == "Total: $58.29"
        shop_page._driver.quit()
