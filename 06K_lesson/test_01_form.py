import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        self.driver.quit()

    def test_form_validation(self):
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

        for field_name, value in fields_data.items():
            selector = f'input[name="{field_name}"]'
            field = self.driver.find_element(By.CSS_SELECTOR, selector)
            field.clear()
            field.send_keys(value)

        submit_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        )
        submit_btn.click()

        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )

        zip_field = self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="zip-code"]'
        )
        self.assertIn(
            "is-invalid", zip_field.get_attribute("class"),
            "Поле Zip code должно быть красным"
        )

        for field_name in fields_data.keys():
            selector = f'input[name="{field_name}"]'
            field = self.driver.find_element(By.CSS_SELECTOR, selector)
            self.assertIn(
                "is-valid", field.get_attribute("class"),
                f"Поле {field_name} должно быть зеленым"
            )


if __name__ == "__main__":
    unittest.main()
