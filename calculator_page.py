from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")

        # Локаторы для кнопок калькулятора
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")

    def open(self):
        """Открыть страницу калькулятора."""
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.get(url)

    def set_delay(self, delay_value):
        """Установить значение задержки."""
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def click_button_7(self):
        """Нажать кнопку 7."""
        self.driver.find_element(*self.button_7).click()

    def click_button_8(self):
        """Нажать кнопку 8."""
        self.driver.find_element(*self.button_8).click()

    def click_plus(self):
        """Нажать кнопку плюс."""
        self.driver.find_element(*self.button_plus).click()

    def click_equals(self):
        """Нажать кнопку равно."""
        self.driver.find_element(*self.button_equals).click()

    def get_result(self, timeout=50):
        """Получить результат с ожиданием."""
        wait = WebDriverWait(self.driver, timeout)
        # Ждем, пока результат не станет равным 15
        wait.until(
            EC.text_to_be_present_in_element(self.result_display, "15")
        )
        return self.driver.find_element(*self.result_display).text

    def calculate_7_plus_8(self):
        """Выполнить операцию 7 + 8."""
        self.click_button_7()
        self.click_plus()
        self.click_button_8()
        self.click_equals()
