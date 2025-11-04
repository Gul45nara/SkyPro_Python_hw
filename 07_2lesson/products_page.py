from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        # Простой поиск и добавление товара
        product_element = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/../..//button")
        product_element.click()

    def get_cart_count(self):
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge.text)
