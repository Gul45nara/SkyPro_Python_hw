from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_saucedemo_checkout():
    """Тест оформления заказа в интернет-магазине."""
    driver = webdriver.Chrome()

    try:
        print("🚀 Запуск теста интернет-магазина...")

        # Создаем объекты страниц
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Шаг 1: Открыть сайт и авторизоваться
        print("1. Открываем сайт и авторизуемся...")
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Шаг 2: Добавить товары в корзину
        print("2. Добавляем товары в корзину...")
        products_page.add_all_required_products()

        # Шаг 3: Перейти в корзину
        print("3. Переходим в корзину...")
        products_page.go_to_cart()

        # Шаг 4: Начать оформление заказа
        print("4. Начинаем оформление заказа...")
        cart_page.click_checkout()

        # Шаг 5: Заполнить информацию для заказа
        print("5. Заполняем информацию для заказа...")
        checkout_page.fill_checkout_info("John", "Doe", "12345")

        # Шаг 6: Получить итоговую сумму
        print("6. Получаем итоговую сумму...")
        total_text = checkout_page.get_total_amount()
        print(f"Итоговая сумма: {total_text}")

        # Извлекаем числовое значение из текста
        total_amount = total_text.replace("Total: $", "")

        # Шаг 7: Проверить итоговую сумму
        expected_total = "58.29"
        print(f"Ожидаемая сумма: ${expected_total}")
        print(f"Фактическая сумма: ${total_amount}")

        if total_amount == expected_total:
            print("✅ ТЕСТ ПРОЙДЕН УСПЕШНО! Итоговая сумма корректна.")
            return True
        else:
            error_msg = (
                f"Ожидалось ${expected_total}, получено ${total_amount}"
            )
            print(f"❌ ТЕСТ НЕ ПРОЙДЕН! {error_msg}")
            return False

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return False

    finally:
        print("7. Закрываем браузер...")
        driver.quit()


if __name__ == "__main__":
    success = test_saucedemo_checkout()
    exit(0 if success else 1)
