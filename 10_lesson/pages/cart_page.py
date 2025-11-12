from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class CartPage(BasePage):
    """
    Page Object для страницы корзины покупок SauceDemo.
    Обеспечивает взаимодействие с элементами корзины.
    """

    # Локаторы элементов страницы корзины
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def click_checkout(self) -> None:
        """Нажать кнопку Checkout для перехода к оформлению заказа."""
        self.click_element(self.CHECKOUT_BUTTON)

    def get_cart_items_count(self) -> int:
        """
        Получить количество товаров в корзине.

        Returns:
            int: Количество товарных позиций в корзине
        """
        return len(self.driver.find_elements(*self.CART_ITEMS))