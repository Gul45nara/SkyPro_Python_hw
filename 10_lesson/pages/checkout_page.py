import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class CheckoutPage(BasePage):
    """
    Page Object для страницы оформления заказа SauceDemo.
    Обеспечивает взаимодействие с формой оформления заказа.

    Attributes:
        FIRST_NAME_FIELD: локатор поля имени
        LAST_NAME_FIELD: локатор поля фамилии
        POSTAL_CODE_FIELD: локатор поля почтового индекса
        CONTINUE_BUTTON: локатор кнопки продолжения
        TOTAL_LABEL: локатор итоговой суммы
        FINISH_BUTTON: локатор кнопки завершения
    """

    # Локаторы элементов страницы оформления заказа
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    @allure.step(
        "Заполнить информацию для оформления заказа: имя '{first_name}', фамилия '{last_name}', индекс '{postal_code}'")
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнить информацию о покупателе.

        Args:
            first_name (str): Имя покупателя
            last_name (str): Фамилия покупателя
            postal_code (str): Почтовый индекс

        Returns:
            None
        """
        self.input_text(self.FIRST_NAME_FIELD, first_name)
        self.input_text(self.LAST_NAME_FIELD, last_name)
        self.input_text(self.POSTAL_CODE_FIELD, postal_code)

    @allure.step("Нажать кнопку 'Continue'")
    def click_continue(self) -> None:
        """
        Нажать кнопку Continue для перехода к итогам заказа.

        Returns:
            None
        """
        self.click_element(self.CONTINUE_BUTTON)

    @allure.step("Нажать кнопку 'Finish'")
    def click_finish(self) -> None:
        """
        Нажать кнопку Finish для завершения заказа.

        Returns:
            None
        """
        self.click_element(self.FINISH_BUTTON)

    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получить итоговую сумму заказа.

        Returns:
            str: Итоговая сумма без префикса 'Total: $'
        """
        total_text = self.get_element_text(self.TOTAL_LABEL)
        return total_text.replace("Total: $", "")