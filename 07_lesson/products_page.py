from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

        # Локаторы для кнопок добавления товаров
        self.add_backpack_btn = (
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        self.add_bolt_tshirt_btn = (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        self.add_onesie_btn = (
            By.ID, "add-to-cart-sauce-labs-onesie"
        )

    def add_backpack_to_cart(self):
        """Добавить Sauce Labs Backpack в корзину."""
        self.driver.find_element(*self.add_backpack_btn).click()

    def add_bolt_tshirt_to_cart(self):
        """Добавить Sauce Labs Bolt T-Shirt в корзину."""
        self.driver.find_element(*self.add_bolt_tshirt_btn).click()

    def add_onesie_to_cart(self):
        """Добавить Sauce Labs Onesie в корзину."""
        self.driver.find_element(*self.add_onesie_btn).click()

    def go_to_cart(self):
        """Перейти в корзину."""
        self.driver.find_element(*self.cart_link).click()

    def add_all_required_products(self):
        """Добавить все требуемые товары в корзину."""
        self.add_backpack_to_cart()
        self.add_bolt_tshirt_to_cart()
        self.add_onesie_to_cart()
