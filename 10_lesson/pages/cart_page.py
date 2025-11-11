from .base_page import BasePage


class CartPage(BasePage):
    """Page object for cart page"""

    def click_checkout(self):
        """Click checkout button"""
        checkout_btn = self.find_element(("id", "checkout"))
        checkout_btn.click()
