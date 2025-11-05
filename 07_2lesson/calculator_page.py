from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Упрощенные локаторы
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.button = "//span[text()='{}']"  # Универсальный локатор для всех кнопок

    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def click_calculator_button(self, button_text):
        """Универсальный метод для клика по любой кнопке калькулятора"""
        button_locator = (By.XPATH, self.button.format(button_text))
        self.driver.find_element(*button_locator).click()

    def get_result(self):
        """Получить результат вычислений"""
        return self.driver.find_element(*self.result_display).text
