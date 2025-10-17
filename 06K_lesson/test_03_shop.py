import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestShop(unittest.TestCase):
    def setUp(self):
        # Настройка Firefox с указанием пути к бинарнику
        options = Options()
        # Можно явно указать путь к Firefox если нужно
        # options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_purchase_total(self):
        # Шаг 2: Авторизация
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Ждем загрузки инвентаря
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

        # Шаг 3: Добавляем товары в корзину
        products = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }

        for product_name, button_id in products.items():
            add_button = self.driver.find_element(By.ID, button_id)
            add_button.click()

        # Шаг 4: Переходим в корзину
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Шаг 5: Нажимаем Checkout
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # Шаг 6: Заполняем форму
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys("Иван")
        self.driver.find_element(By.ID, "last-name").send_keys("Петров")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")

        # Шаг 7: Нажимаем Continue
        self.driver.find_element(By.ID, "continue").click()

        # Шаг 8: Читаем итоговую стоимость
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text

        # Шаг 10: Проверяем итоговую сумму
        expected_total = "Total: $58.29"
        self.assertEqual(total_text, expected_total,
                         f"Ожидалась сумма '{expected_total}', но получили '{total_text}'")


if __name__ == "__main__":
    unittest.main()