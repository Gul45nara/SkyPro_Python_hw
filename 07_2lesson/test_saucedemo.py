import pytest
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

def test_saucedemo_purchase_flow():
    driver = webdriver.Chrome()

    try:
        # Шаг 1: Открыть страницу логина и войти
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Шаг 2: Добавить товары в корзину
        products_page = ProductsPage(driver)
        products_page.add_all_required_products()

        # Шаг 3: Перейти в корзину
        products_page.go_to_cart()

        # Шаг 4: Подтвердить корзину
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        # Шаг 5: Заполнить информацию о покупателе
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.click_continue()

        # Шаг 6: Получить итоговую сумму
        total_text = checkout_page.get_total_amount()
        total_amount = total_text.replace("Total: $", "")

        # Шаг 7: Проверить итоговую сумму
        expected_total = "58.29"
        assert total_amount == expected_total, f"Ожидаемая сумма должна быть ${expected_total}, но получили ${total_amount}"

        # Шаг 8: Завершить покупку
        checkout_page.click_finish()

    finally:
        driver.quit()
