import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        self.driver.quit()

    def test_form_validation(self):
        # Заполняем форму
        fields_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        # Заполняем все поля кроме zip-code
        for field_name, value in fields_data.items():
            field = self.driver.find_element(By.CSS_SELECTOR, f'input[name="{field_name}"]')
            field.clear()
            field.send_keys(value)

        # Нажимаем Submit
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_btn.click()

        # Ждем появления результатов - проверяем наличие текста "Zip code" и "N/A"
        self.wait.until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Zip code")
        )
        self.wait.until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "N/A")
        )

        # Проверяем что поле Zip code показывает "N/A" (не заполнено)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Zip code", body_text)
        self.assertIn("N/A", body_text)

        # Проверяем что остальные поля заполнены корректно
        expected_values = {
            "First name": "Иван",
            "Last name": "Петров",
            "Address": "Ленина, 55-3",
            "E-mail": "test@skypro.com",
            "Phone number": "+7985899998787",
            "City": "Москва",
            "Country": "Россия",
            "Job position": "QA",
            "Company": "SkyPro"
        }

        for field_name, expected_value in expected_values.items():
            self.assertIn(expected_value, body_text,
                          f"Текст '{expected_value}' для поля {field_name} не найден на странице")


if __name__ == "__main__":
    unittest.main()
