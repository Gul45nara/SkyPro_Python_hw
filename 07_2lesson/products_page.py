from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

        # Кортеж локаторов для кнопок добавления товаров
        self.add_product_buttons = (
            (By.ID, "add-to-cart-sauce-labs-backpack"),
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            (By.ID, "add-to-cart-sauce-labs-onesie")
        )

    def go_to_cart(self):
        """Перейти в корзину."""
        self.driver.find_element(*self.cart_link).click()

    def add_product_to_cart(self, product_index):
        """Добавить конкретный товар в корзину по индексу"""
        self.driver.find_element(*self.add_product_buttons[product_index]).click()

    def add_all_required_products(self):
        """Добавить все необходимые товары в корзину (цикл по кортежу)"""
        for button_locator in self.add_product_buttons:
            self.driver.find_element(*button_locator).click()

    def get_cart_count(self):
        """Получить количество товаров в корзине"""
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge.text)
