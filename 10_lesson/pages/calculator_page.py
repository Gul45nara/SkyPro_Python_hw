from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CalculatorPage(BasePage):
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver экземпляр
            timeout: время ожидания в секундах
        """
        super().__init__(driver, timeout)

        # Локаторы элементов калькулятора
        self.delay_input = (By.ID, "delay")
        self.result_display = (By.ID, "result")
        self.button_selectors = {
            "0": (By.ID, "btn-0"),
            "1": (By.ID, "btn-1"),
            "2": (By.ID, "btn-2"),
            "3": (By.ID, "btn-3"),
            "4": (By.ID, "btn-4"),
            "5": (By.ID, "btn-5"),
            "6": (By.ID, "btn-6"),
            "7": (By.ID, "btn-7"),
            "8": (By.ID, "btn-8"),
            "9": (By.ID, "btn-9"),
            "+": (By.ID, "btn-+"),
            "-": (By.ID, "btn--"),
            "*": (By.ID, "btn-*"),
            "/": (By.ID, "btn-/"),
            "=": (By.ID, "btn-="),
            "C": (By.ID, "btn-C")
        }

    def set_delay(self, delay_seconds: int) -> None:
        """
        Установить задержку вычислений.

        Args:
            delay_seconds: количество секунд задержки
        """
        self.enter_text(self.delay_input, str(delay_seconds))

    def click_calculator_button(self, button: str) -> None:
        """
        Нажать кнопку калькулятора.

        Args:
            button: символ кнопки ('0'-'9', '+', '-', '*', '/', '=', 'C')

        Raises:
            ValueError: если передан неизвестный символ кнопки
        """
        if button not in self.button_selectors:
            raise ValueError(f"Неизвестная кнопка: {button}")

        self.click_element(self.button_selectors[button])

    def get_result(self) -> str:
        """
        Получить результат вычислений.

        Returns:
            str: текст из поля результата
        """
        result_element = self.find_element(self.result_display)
        return result_element.get_attribute("value")

    def clear_calculator(self) -> None:
        """
        Очистить калькулятор.
        """
        self.click_calculator_button("C")
