import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 50)

    def tearDown(self):
        self.driver.quit()

    def test_slow_calculator(self):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")

        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )

        actual_result = result_element.text
        self.assertEqual(
            actual_result, "15",
            f"Ожидался результат 15, но получили {actual_result}"
        )


if __name__ == "__main__":
    unittest.main()
