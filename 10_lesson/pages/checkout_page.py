from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Класс для работы со страницей оформления заказа SauceDemo."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver экземпляр
            timeout: время ожидания в секундах
        """
        super().__init__(driver, timeout)

        # Локаторы элементов страницы
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self, first_name: str) -> None:
        """
        Ввести имя.

        Args:
            first_name: имя покупателя
        """
        self.enter_text(self.first_name_field, first_name)

    def enter_last_name(self, last_name: str) -> None:
        """
        Ввести фамилию.

        Args:
            last_name: фамилия покупателя
        """
        self.enter_text(self.last_name_field, last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """
        Ввести почтовый индекс.

        Args:
            postal_code: почтовый индекс
        """
        self.enter_text(self.postal_code_field, postal_code)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнить информацию о покупателе.

        Args:
            first_name: имя покупателя
            last_name: фамилия покупателя
            postal_code: почтовый индекс
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self) -> None:
        """
        Нажать кнопку Continue.
        """
        self.click_element(self.continue_button)

    def click_finish(self) -> None:
        """
        Нажать кнопку Finish.
        """
        self.click_element(self.finish_button)

    def get_total_amount(self) -> str:
        """
        Получить итоговую сумму.

        Returns:
            str: текст с итоговой суммой
        """
        total_element = self.find_element(self.total_label)
        return total_element.text

    def is_order_complete(self) -> bool:
        """
        Проверить успешность оформления заказа.

        Returns:
            bool: True если заказ успешно оформлен, иначе False
        """
        try:
            complete_element = self.find_element(self.complete_header)
            return "Thank you for your order" in complete_element.text
        except Exception:
            return False
