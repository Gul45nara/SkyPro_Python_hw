from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from typing import Dict, Tuple


class CalculatorPage(BasePage):
    """
    Page Object для страницы веб-калькулятора.
    """

    # Локаторы элементов калькулятора
    DELAY_INPUT = (By.ID, "delay")
    RESULT_DISPLAY = (By.CLASS_NAME, "display")

    # Словарь локаторов для кнопок калькулятора
    BUTTON_SELECTORS: Dict[str, Tuple[str, str]] = {
        "0": (By.XPATH, "//button[text()='0']"),
        "1": (By.XPATH, "//button[text()='1']"),
        "2": (By.XPATH, "//button[text()='2']"),
        "3": (By.XPATH, "//button[text()='3']"),
        "4": (By.XPATH, "//button[text()='4']"),
        "5": (By.XPATH, "//button[text()='5']"),
        "6": (By.XPATH, "//button[text()='6']"),
        "7": (By.XPATH, "//button[text()='7']"),
        "8": (By.XPATH, "//button[text()='8']"),
        "9": (By.XPATH, "//button[text()='9']"),
        "+": (By.XPATH, "//button[text()='+']"),
        "-": (By.XPATH, "//button[text()='-']"),
        "*": (By.XPATH, "//button[text()='×']"),
        "/": (By.XPATH, "//button[text()='÷']"),
        "=": (By.XPATH, "//button[text()='=']"),
        "C": (By.XPATH, "//button[text()='C']")
    }

    def set_delay(self, seconds: int) -> None:
        """Установить задержку вычислений."""
        delay_input = self.find_element(self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_calculator_button(self, button: str) -> None:
        """Нажать кнопку калькулятора."""
        if button in self.BUTTON_SELECTORS:
            self.click_element(self.BUTTON_SELECTORS[button])
        else:
            raise ValueError(f"Кнопка '{button}' не найдена")

    def get_result(self) -> str:
        """Получить результат вычислений."""
        result_element = self.find_element(self.RESULT_DISPLAY)
        return result_element.text.strip()