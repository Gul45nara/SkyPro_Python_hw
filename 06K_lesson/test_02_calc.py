import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.wait = WebDriverWait(self.driver, 50)  # 45 секунд + запас

    def tearDown(self):
        self.driver.quit()

    def test_slow_calculator(self):
        # Вводим задержку 45 секунд
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопки: 7 + 8 =
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ждем пока результат станет равным 15 (максимум 50 секунд)
        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")

        # Ожидаем появления результата 15
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

        # Проверяем что результат действительно 15
        actual_result = result_element.text
        self.assertEqual(actual_result, "15", f"Ожидался результат 15, но получили {actual_result}")


if __name__ == "__main__":
    unittest.main()